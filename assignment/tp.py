txt_data = "Created a new file,\n"

file_path = "/Users/sa40132171/Desktop/text.txt"
count = 0
with open(file_path, 'r') as file:
    for line in file:
        count += 1
print(count)