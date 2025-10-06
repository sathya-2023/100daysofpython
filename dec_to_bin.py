def dec_to_bin(num):
    if num > 1:
        dec_to_bin(num//2)
    print(num%2, end=" ")

dec_to_bin(23)