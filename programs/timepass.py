# def least_difference(a, b, c):
#     diff1 = abs(a - b)
#     diff2 = abs(b - c)
#     diff3 = abs(a - c)
#     return min(diff1, diff2, diff3)
#
# print(
#     least_difference(1, 10, 100),
#     least_difference(1, 10, 10),
#     least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
# )
#
# help(least_difference(1,10,100))

def calculate_love_score():
    name_1 = input("Enter 1st name: ")
    name_2 = input("Enter 2nd name: ")
    print(name_2, name_1)


calculate_love_score()