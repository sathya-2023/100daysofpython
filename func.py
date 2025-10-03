num = int(input("Enter a num: "))

def new_func():
    if num%2 == 0:
        print("Even")
    else:
        print("odd")

for i in range(10):
    new_func()
    num = num + 1