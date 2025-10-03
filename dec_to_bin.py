#-------decimal to binary using recursive function-----#
def bin(num):
    if num > 1:
        bin(num//2)
    print(num%2, end="")

bin(23)