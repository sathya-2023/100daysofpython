# Netflix Clone - Complete AWS CI/CD Deployment Guide

This guide provides step-by-step instructions for deploying a Netflix clone application using AWS services with a complete CI/CD pipeline.

## 🎯 Project Overview

- **Application**: React-based Netflix clone with TMDB API integration
- **Tech Stack**: React 18, TypeScript, Material-UI, Vite
- **Container**: Docker (multi-stage build with Node.js + Nginx)
- **CI/CD**: AWS CodeCommit + CodeBuild
- **Hosting**: AWS EC2 with Docker
- **Registry**: Docker Hub

## 📋 Prerequisites

### Required Accounts
- AWS Account with admin access
- Docker Hub account
- TMDB API account (free tier)
- GitHub account (optional - for source control)

### Local Tools
- Git installed
- AWS CLI installed and configured
- SSH client
- Node.js 16+ (for local testing)

## 🚀 Step-by-Step Setup

### Step 1: Get TMDB API Key

1. Go to [The Movie Database (TMDB)](https://www.themoviedb.org/)
2. Create a free account
3. Navigate to Settings > API
4. Request an API key (choose Developer option)
5. Save your API key (v3 auth): `0b65b4097252045f60d92f358f6f83f3` (example)

### Step 2: Set Up AWS IAM User

1. **Create IAM User** for DevOps:
   ```
   User name: netlfix-devops
   Access type: Programmatic access + AWS Management Console access
   ```

2. **Attach Policies**:
   - `AWSCodeCommitFullAccess`
   - `AWSCodeBuildAdminAccess`
   - `AmazonEC2FullAccess`
   - `AmazonSSMFullAccess` (for Parameter Store)

3. **Download Credentials**:
   - Save Access Key ID and Secret Access Key
   - Configure AWS CLI:
     ```bash
     aws configure --profile netflix-devops
     ```

### Step 3: Store Secrets in AWS Parameter Store

Store sensitive credentials securely in AWS Systems Manager Parameter Store:

```bash
# Set your AWS region
export AWS_REGION=us-east-1

# Store Docker Hub username
aws ssm put-parameter \
  --name /dockerhub/username \
  --value "your-dockerhub-username" \
  --type String \
  --region $AWS_REGION

# Store Docker Hub password
aws ssm put-parameter \
  --name /dockerhub/password \
  --value "your-dockerhub-password" \
  --type SecureString \
  --region $AWS_REGION

# Store TMDB API key
aws ssm put-parameter \
  --name /dockerhub/api-key \
  --value "your-tmdb-api-key" \
  --type SecureString \
  --region $AWS_REGION
```

**Verify parameters**:
```bash
aws ssm get-parameter --name /dockerhub/api-key --with-decryption --region $AWS_REGION
```

### Step 4: Set Up CodeCommit Repository

1. **Create CodeCommit repository**:
   ```bash
   aws codecommit create-repository \
     --repository-name netflix-devops-project \
     --repository-description "Netflix clone CI/CD project" \
     --region us-east-1
   ```

2. **Configure Git credentials** for CodeCommit:
   - Go to IAM Console > Users > netlfix-devops
   - Security credentials > HTTPS Git credentials for CodeCommit
   - Generate credentials and save them

3. **Clone your source repository**:
   ```bash
   git clone https://github.com/sathya-2023/netlfix-clone-aws.git
   cd netlfix-clone-aws
   ```

4. **Add CodeCommit as remote**:
   ```bash
   git remote add codecommit https://git-codecommit.us-east-1.amazonaws.com/v1/repos/netflix-devops-project
   ```

### Step 5: Fix TypeScript Interface Conflicts

**Important**: The original code has a TypeScript conflict that prevents compilation. Fix before deploying.

**Issue**: `PlayButton` component uses `id` prop which conflicts with HTML button's native `id` attribute.

**Fix** - Rename `id` to `movieId` in these files:

**1. src/components/PlayButton.tsx**:
```typescript
// Change this:
export interface PlayButtonProps {
  id?: number;
}

// To this:
export interface PlayButtonProps {
  movieId?: number;
}

// Update function:
export const PlayButton: React.FC<PlayButtonProps> = ({ movieId }) => {
  const navigate = useNavigate();
  return (
    <Button
      onClick={() => navigate(`/watch/${movieId}`)}
      // ... rest of code
    />
  );
};
```

**2. src/pages/WatchPage.tsx**:
```typescript
// Change parameter name:
export const WatchPage = () => {
  const { movieId } = useParams();
  
  // Update key:
  key={`video-${movieId}`}
```

**3. src/components/HeroSection.tsx**:
```typescript
// Update prop name:
<PlayButton movieId={video.id} />
```

**4. src/components/VideoCardPortal.tsx**:
```typescript
// Update navigation:
navigate(`/watch/${movieId}`);
```

**5. src/components/DetailModal.tsx**:
```typescript
// Update prop name:
<PlayButton movieId={video.id} />
```

### Step 6: Configure Docker Build Files

#### 6.1 Update Dockerfile

Ensure your `Dockerfile` has proper API key handling:

```dockerfile
# Build stage
FROM node:16.17.0-alpine as builder
WORKDIR /app
COPY ./package.json .
COPY ./yarn.lock .
RUN yarn install
COPY . .

# Accept API key as build argument
ARG TMDB_V3_API_KEY

# Debug output (optional)
RUN echo "Building with API key configured"
RUN test -n "$TMDB_V3_API_KEY" && echo "API key received" || echo "WARNING: API key is empty!"

# Set environment variables for Vite build
ENV VITE_APP_TMDB_V3_API_KEY=${TMDB_V3_API_KEY}
ENV VITE_APP_API_ENDPOINT_URL="https://api.themoviedb.org/3"

RUN yarn build

# Production stage
FROM nginx:stable-alpine
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /app/dist .
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

#### 6.2 Create buildspec.yaml

Create `buildspec.yaml` in the project root with **POSIX-compliant syntax**:

```yaml
version: 0.2

env:
  parameter-store:
    USERNAME: /dockerhub/username
    PASSWORD: /dockerhub/password
    KEY: /dockerhub/api-key

phases:
  install:
    runtime-versions:
      nodejs: 16
    commands:
      - node --version
      - echo "Node.js installed"

  pre_build:
    commands:
      - npm install
      - echo "Dependencies installed"
      - echo "Logging into DockerHub"
      - docker login -u $USERNAME -p $PASSWORD

  build:
    commands:
      - echo "Building with API key configured"
      - echo $KEY | cut -c 1-10
      - docker build . -t sathya1101/netflix-clone:latest --build-arg TMDB_V3_API_KEY="$KEY"
      - echo "Docker image built successfully"

  post_build:
    commands:
      - docker push sathya1101/netflix-clone:latest
      - echo "Image pushed to DockerHub"

artifacts:
  files:
    - '**/*'
```

**Critical Notes**:
- Use `echo $KEY | cut -c 1-10` NOT `${KEY:0:10}` (CodeBuild uses `/bin/sh`, not bash)
- Docker login MUST be in `pre_build` phase (before pulling base images)
- Quote the API key in build-arg: `"$KEY"`

### Step 7: Create CodeBuild Project

1. **Navigate to AWS CodeBuild Console**
2. **Create build project**:
   - Project name: `netflix-codebuild-project`
   - Source provider: AWS CodeCommit
   - Repository: `netflix-devops-project`
   - Branch: `main`

3. **Environment**:
   - Environment image: Managed image
   - Operating system: Amazon Linux 2
   - Runtime: Standard
   - Image: `aws/codebuild/amazonlinux2-x86_64-standard:5.0`
   - Privileged: ✅ **Enable** (required for Docker builds)
   - Service role: Create new (or use existing with proper permissions)

4. **Buildspec**:
   - Build specifications: Use a buildspec file
   - Buildspec name: `buildspec.yaml`

5. **Logs**:
   - CloudWatch logs: Enable (optional but recommended)

6. **Create build project**

### Step 8: Grant CodeBuild IAM Permissions

The CodeBuild service role needs access to Parameter Store:

```bash
# Get the role name from CodeBuild project settings
ROLE_NAME="codebuild-netflix-codebuild-project-service-role"

# Attach SSM policy
aws iam attach-role-policy \
  --role-name $ROLE_NAME \
  --policy-arn arn:aws:iam::aws:policy/AmazonSSMReadOnlyAccess
```

Or manually add this inline policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ssm:GetParameter",
        "ssm:GetParameters"
      ],
      "Resource": "arn:aws:ssm:us-east-1:*:parameter/dockerhub/*"
    }
  ]
}
```

### Step 9: Set Up EC2 Instance

#### 9.1 Launch EC2 Instance

1. **Go to EC2 Console** > Launch Instance
2. **Configure**:
   - Name: `netflix-app-server`
   - AMI: Amazon Linux 2023
   - Instance type: `t2.micro` (free tier eligible)
   - Key pair: Create new or use existing (save `.pem` file)
   - Network settings:
     - Allow SSH (port 22) from your IP
     - Allow HTTP (port 80) from anywhere (0.0.0.0/0)
   - Storage: 8 GB default

3. **Launch instance** and note the public IP address

#### 9.2 Install Docker on EC2

Connect to your EC2 instance:
```bash
chmod 400 netflix-keypair.pem
ssh -i netflix-keypair.pem ec2-user@YOUR_EC2_PUBLIC_IP
```

Install Docker:
```bash
# Update system
sudo yum update -y

# Install Docker
sudo yum install docker -y

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add ec2-user to docker group
sudo usermod -aG docker ec2-user

# Verify installation
docker --version

# Log out and back in for group changes to take effect
exit
```

### Step 10: Push Code and Trigger Build

1. **Commit all changes**:
   ```bash
   git add .
   git commit -m "Configure CI/CD pipeline with buildspec.yaml"
   ```

2. **Push to CodeCommit**:
   ```bash
   git push codecommit main
   ```

3. **Also push to GitHub** (optional):
   ```bash
   git push origin main
   ```

4. **Trigger build manually**:
   - Go to CodeBuild Console
   - Select `netflix-codebuild-project`
   - Click "Start build"
   - Monitor the build logs

### Step 11: Deploy to EC2

Once build succeeds and image is pushed to Docker Hub, deploy:

```bash
ssh -i ~/Downloads/netflix-keypair.pem ec2-user@YOUR_EC2_IP "\
  sudo docker stop \$(sudo docker ps -q); \
  sudo docker rm \$(sudo docker ps -aq); \
  sudo docker pull sathya1101/netflix-clone:latest && \
  sudo docker run -d -p 80:80 sathya1101/netflix-clone:latest && \
  echo 'Deployment successful!'"
```

**What this does**:
- Stops all running containers
- Removes all stopped containers
- Pulls latest image from Docker Hub
- Runs new container on port 80

### Step 12: Access Your Application

Open browser and navigate to:
```
http://YOUR_EC2_PUBLIC_IP
```

You should see the Netflix clone with movie data loaded from TMDB API!

## 🔧 Common Issues and Solutions

### Issue 1: TypeScript Compilation Error
**Error**: `Interface 'PlayButtonProps' incompatible`

**Solution**: Follow Step 5 to rename `id` to `movieId` across all components.

### Issue 2: Docker Hub Rate Limit (429 Error)
**Error**: "You have reached your unauthenticated pull rate limit"

**Solution**: Ensure `docker login` is in the `pre_build` phase of buildspec.yaml, NOT in `post_build`.

### Issue 3: Bad Substitution Error
**Error**: "Bad substitution" in CodeBuild logs

**Solution**: CodeBuild uses `/bin/sh` (POSIX shell), not bash. Use:
```bash
echo $KEY | cut -c 1-10
```
Instead of:
```bash
${KEY:0:10}
```

### Issue 4: Blank Movie Cards
**Error**: No movies displayed, 401 errors in browser console

**Causes**:
- API key not properly embedded in Docker build
- Environment variable not set correctly

**Solution**: 
- Verify API key in Parameter Store
- Ensure build logs show "API key received"
- Check `--build-arg TMDB_V3_API_KEY="$KEY"` is properly quoted

### Issue 5: CodeBuild Can't Access Parameter Store
**Error**: "AccessDeniedException" when fetching parameters

**Solution**: Attach `AmazonSSMReadOnlyAccess` policy to CodeBuild service role (see Step 8).

### Issue 6: EC2 Can't Connect
**Error**: Connection timeout

**Solution**:
- Verify security group allows SSH (port 22) from your IP
- Verify security group allows HTTP (port 80) from 0.0.0.0/0
- Check that instance is running
- Verify you're using the correct key pair

## 🔄 Deployment Workflow

### For Code Changes:

1. Make changes locally
2. Test locally: `npm run dev`
3. Commit changes: `git add . && git commit -m "Description"`
4. Push to repositories:
   ```bash
   git push origin main && git push codecommit main
   ```
5. Trigger CodeBuild manually in AWS Console
6. Wait for build to complete
7. Deploy to EC2:
   ```bash
   ssh -i ~/Downloads/netflix-keypair.pem ec2-user@YOUR_EC2_IP "\
     sudo docker stop \$(sudo docker ps -q); \
     sudo docker rm \$(sudo docker ps -aq); \
     sudo docker pull sathya1101/netflix-clone:latest && \
     sudo docker run -d -p 80:80 sathya1101/netflix-clone:latest"
   ```

### For UI-Only Changes:

If only changing React components (no API changes):
1. Follow steps 1-7 above
2. No need to rebuild Docker image if API key unchanged

## 📊 Architecture Overview

```
Developer → Git Push → CodeCommit
                           ↓
                      CodeBuild
                           ↓
                  (Build Docker Image)
                           ↓
                  (Parameter Store for secrets)
                           ↓
                      Docker Hub
                           ↓
                    EC2 Instance
                           ↓
                     User Browser
```

## 🔐 Security Best Practices

1. **Never commit secrets** to Git repositories
2. **Use Parameter Store** for all sensitive data
3. **Use SecureString** type for passwords and API keys
4. **Restrict IAM permissions** to minimum required
5. **Use security groups** to limit EC2 access
6. **Rotate credentials** regularly
7. **Use HTTPS** in production (add SSL/TLS certificate)

## 🎨 Optional Enhancements

### Remove Developer Attribution Footer

If you want to remove the "Developed by Crazy Man" footer:

Edit `src/components/layouts/MainLayout.tsx` and remove this section:
```typescript
<Box
  sx={{
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    py: 2,
  }}
>
  <Typography sx={{ color: "text.secondary" }}>
    Developed by{" "}
    <Link href="https://github.com/crazy-man22" target="_blank">
      Crazy Man
    </Link>
  </Typography>
</Box>
```

### Set Up Webhook Automation (Advanced)

For automatic builds on every push, you can set up EventBridge rules to trigger CodeBuild. This requires additional IAM configuration.

## 📚 Resources

- [TMDB API Documentation](https://developers.themoviedb.org/3)
- [AWS CodeBuild User Guide](https://docs.aws.amazon.com/codebuild/)
- [Docker Documentation](https://docs.docker.com/)
- [React Documentation](https://react.dev/)

## 🤝 Contributing

Feel free to fork this project and customize it for your needs!

## 📝 License

This project is for educational purposes.

## 🙏 Credits

- Original Netflix Clone Template: [crazy-man22](https://github.com/crazy-man22)
- Movie Data: [The Movie Database (TMDB)](https://www.themoviedb.org/)
- Deployment Guide: Your AWS DevOps Journey

---

**Project Repository**: https://github.com/sathya-2023/netlfix-clone-aws/

**Live Demo**: http://52.90.115.87 (if still running)

**Last Updated**: March 2026
