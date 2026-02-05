from operator import itemgetter, attrgetter

colors = ['red', 'yellow', 'green', 'black']
color = ['blue','orange', 'black', 'white']
# print(colors[1])
# print(len(colors))
# add = 0
# for i in colors:
#     add += len(i)
#
# print(add)

# if 'green' in colors:
#     print(True)
#
# colors.append('maroon')                 #to add new element
# colors.insert(2,'maroon')               #to add new element in a specific place
# colors.extend(color)                    #to add 2 lists together
# print(colors.index('green'))            #to find the index number
# colors.remove('maroon' and 'black')     #to remove an element
# colors.sort()                           #to sort the list
# print(colors[0:3])                      #to print some of the elements
# print(colors)


print(sorted(colors, reverse = True))     #sorting and printing the list in reverse

alpha = ['aaa','BB','cc', 'DDDD']
print(sorted(alpha, key= str.lower))

## Say we have a list of strings we want to sort by the last letter of the string.
strs = ['xc', 'zb', 'yd', 'wa']


## Write a little function that takes a string, and returns its last letter.
## This will be the key function (takes in 1 value, returns 1 value).
def myfn(s):
    return s[-1]

## Now pass key=MyFn to sorted() to sort by the last letter:
print(sorted(strs, key=myfn, reverse=True))  ## ['wa', 'zb', 'xc', 'yd']



students = [('Sathya','Nadar',24), ('David','Malan',44), ('Harris','khan',27)]

print(sorted(students, key=itemgetter(2)))

class Student:
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

Student_Objects = [
    Student('Sathya','A',24),
    Student('Anil','B',25),
    Student('Sonu','A',23)]

print(sorted(Student_Objects, key=attrgetter('name')))