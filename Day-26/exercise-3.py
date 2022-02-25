with open('file1.txt') as file:
    file1 = file.readlines()
    print(file1)

with open('file2.txt') as file:
    file2 = file.readlines()
    print(file2)

result = [int(n) for n in file1 if n in file2]
print(result)