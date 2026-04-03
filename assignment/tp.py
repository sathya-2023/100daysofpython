# txt_data = "Created a new file,\n"
#
# file_path = "/Users/sa40132171/Desktop/text.txt"
# count = 0
# with open(file_path, 'r') as file:
#     for line in file:
#         count += 1
# print(count)

# import re
#
# text = "Weather at Amsterdam"
# match = re.search('Amsterdam', text)
# print(True if match else "not found")
#
# def fib():
#     a = 0
#     b = 1
#     while True:
#         yield a
#         a,b = b, a+b
# counter = 0
# for n in fib():
#     print(n)
#     counter += 1
#     if counter == 10:
#         break

# print(counter)

# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_lengths = []
# for word in words:
#       if word != "the":
#           word_lengths.append(len(word))
# print(words)
# print(word_lengths)


# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# newlist = [int(i) for i in numbers if i>0]
# print(newlist)

# numbers = [1, 2, 3, 4, 5, 6]
#
# # Lambda checks if x % 2 is not 0 (which means it's odd)
# is_odd = map(lambda x: x % 2 != 0, numbers)
#
# # Convert the map object to a list and print
# print(list(is_odd))

new_list = ["Sathya",1,435,2,'A',"Wipro",40]
