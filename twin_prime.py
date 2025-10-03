def check_prime(num):
    for i in range (2, num):
        if num % i == 0:
            return False
    return True
# if check_prime(num):
#     print("prime")
# else:
#     print("not prime")

def twin_prime(num):
    for first_num in range (2, num):
        second_num = first_num + 2
        if (check_prime(first_num) and check_prime(second_num)):
            print(f"{first_num} and {second_num}")

twin_prime(int(input("Enter a num:")))