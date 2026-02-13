# def twoSum(num, target):

num = [3,3]
target = 6

for i in range(len(num)):
    for j in num:
        if i + j == target:
            # print(i)
            print([num.index(i), num.index(j)])


        