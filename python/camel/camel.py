camel = input("camelCase: ")
list = []

for letter in camel:
    list.append(letter)

for i in range(len(list)):
    if list[i].isupper():
        list[i].lower()
        list.insert(i, " ")

print()