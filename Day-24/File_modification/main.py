# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", "a") as file:
    file.write("New Text")
