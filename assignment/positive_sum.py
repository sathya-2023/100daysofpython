# 1. Write a function that takes a list of number and returns the sum of only the positive numbers
# def total(num_list):
#     sum_of_pos = 0
#     for i in num:
#         if i > 0:
#             sum_of_pos += i
#     return sum_of_pos
# num = [2,5,1,-1,-33,-2,1,4,2]
# print(total(num))

#2. Create a function that takes a string and returns the number of vowels in it.
# def count_vowels(s):
#     vowels = "aeiou"
#     count = 0
#     for char in s.lower():
#         if char in vowels:
#             count += 1
#     return count
# print(count_vowels("Sathya Narayanan"))

#3. Write a function that takes 2 parameters: a list and a value and returns how many times the value appears in the list.
# def count_values(list,value):
#     total = 0
#     for i in list:
#         if i == value:
#             total += 1
#     return total
# print(count_values(['apple','orange','grape','banana','banana','apple','banana'], "banana"))

#4. Define a function that returns the largest number from a list without using the built-in function max().
# def largest_num(num):
#     largest = 0
#     for i in num:
#         if i > largest:
#             largest = i
#     return largest
# num  = [4,1,5,3,22,1,4,21]
# print(largest_num(num))

#5. Write a function that takes a list of integers and return a new list containing only unique values.
# def unique_values(l):
#     new_l = []
#     for item in l:
#         if item in new_l:
#             continue
#         else:
#             new_l.append(item)
#
#     new_l = list(set(l))
#     return new_l
# num = [4,2,5,1,66,3,3,4,1,2]
# print(unique_values(num))

#6. Given a list of words, write code to create a dictionary where keys are words and the length of the word are values.
# def word_len(dic):
#     dic = {}
#     for word in words:
#         dic[word] = len(word)
#         # dic.update({word:len(word)})
#     return dic
# words = ['Hello', 'World','this','is','python']
# print(word_len(words))

#7. Write a program that counts how many times a number appears in a list and stores the result in a dictionary.
# #used AI for this, to find the logic
# def num_counter(l):
#     counts = {n:num.count(n) for n in num}
#     return counts
# num = [2,1,4,2,4,5,2,3,2,33,2,3,2,23]
# print(f"The number of times each number appeared in the list is {num_counter(num)})

#8. Given a dictionary of student and their scores, write a program to calculate the average score.
# def avg_score(data):
#     return(sum(data.values()))/len(data.keys())
# student = {"English": 87, "Maths": 71, "Science": 77, "History": 65, "Geography": 64, "Hindi": 55, "Marathi": 35}
# print(f"The Average score of the Student is {avg_score(student):.2f}")

#9. Write a program to merge 2 Dictionaries, if a Key exists in both then sum their values.
# stud1 = {"English": 87, "Maths": 71}
# stud2 = {"English": 67, "Chemistry": 71}
# merged = stud1.copy()
# for key,value in stud2.items():
#     print(merged.get(key, 0))
#     merged[key] = merged.get(key, 0) +value
# print(merged)

#10. Given a list of dictionaries with product, write code to find the product with highest price.
# produce = [
#     {"name":"tomato","price":20,"stock":15},
#     {'name':'onion','price':30,'stock':30},
#     {'name':'potato','price':25,'stock':40}
# ]
# # prices = []
# # for p in produce:
# #     prices.append((p["price"]))
# # print(max(prices))
# highest_price = max(p['price'] for p in produce)
# print(highest_price)

#11. Write a program that reads a text file and prints the number of lines in the file.
# file_path = "text.txt"  #Give file path here
# count = 0
# with open(file_path, 'r') as file:
#     for line in file:
#         count += 1
# print(count)

# 12. Create a program that reads a file and stores each line as an element in a list.
# file_path = "/Users/sa40132171/Desktop/text.txt"
# # line_list = []
# with open(file_path,'r') as file:
#     line_list = [line.strip() for line in file]
# print(line_list)

# Write a program that copies the contents of one file into another file.
# with open("/Users/sa40132171/Desktop/text.txt",'r') as file:
#     with open("/Users/sa40132171/Desktop/text2.txt",'w') as file2:
#         file2.write(file.read())

# txt_data = "This is created just now\n"
# # f_src = "/Users/sa40132171/Desktop/text.txt"
# # f_dst = "/Users/sa40132171/Desktop/text2.txt"
#
# with open("/Users/sa40132171/Desktop/text.txt", 'r') as f_src, open("/Users/sa40132171/Desktop/text2.txt",'w') as f_dst :
#     f_dst.write(f_src.read())

# Read a file of comma separated values and store the data in an appropriate data structure


#Write a code that safely converts user input to integer and handles invalid inputs.
# try:
#    num = int(input("Enter a num: "))
#    print(num)
# except ValueError:
#    print("Enter only numbers")

# Write a code that handles division by zero without stopping the program.
# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     print(numerator/denominator)
# except ValueError:
#     print("entered value is not an Integer")
# except ZeroDivisionError:
#     print("Can't divide by Zero!")

# Create a program that reads numbers from the file and skips any invalid entries.

# Create a student class with attributes name age, and a method to display the student details.

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(self.name)
#         print(self.age)
# student_1 = Student("Sathya", 25)
# student_1.display()

# Write a class representing a rectangle with attributes width and height and a method to calculate the area.
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def __str__(self):
#         return f"The area of the rectangle with width: {self.width} and height: {self.height} is {self.width*self.height}"
#
# rect = Rectangle(22,11)
# print(rect)

# Write a class book with attribute title and author and a method that returns a formatted description.

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self. author = author
#     def get_description(self):
#         return f"{self.title} by {self.author}"
#
# book = Book("Wings of Fire", "Dr.APJ Abdul Kalam")
# print(book.get_description())

# Create a class bank account that initializes account holder name and balance in a constructer

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
# account = BankAccount("Sathya", 99000000)
# print(account.balance)

# Create a class that assigns a default to an attribute if none is provided.
# class BankAccount:
#     def __init__(self, name, balance = 0):  #default value of Balance is set to 0
#         self.name = name
#         self.balance = balance
#
# acc1 = BankAccount("Sathya", 99000000)
# acc2 = BankAccount("Narayanan")
# print(f"{acc1.name}: {acc1.balance}")
# print(f"{acc2.name}: {acc2.balance}")

# Create a class with public methods that modify private instance variables
# class BankAccount:
#     def __init__(self, name, balance = 0):  #default value of Balance is set to 0
#         self.name = name
#         self._balance = balance     #private variable
#     def deposit(self, amount):      #public method that modifies private variable
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited: {amount}, new balance: {self._balance}")
#         else:
#             print("Deposit amount must be positive")
#     def get_balance(self):
#         return f"Account balance: {self._balance}"
#     def __str__(self):
#         return f"Account owner: {self.name}"
#
# acc1 = BankAccount("Dhanush", 200)
# acc1.deposit(300)
# print(acc1,"\n",acc1.get_balance())

# Write a class that prevents direct access to sensitive data using naming conventions.