camel = input("camelCase: ")
list = list(camel)

for i in range(len(list)):
    if list[i].isupper():
        list[i].lower()
        list.insert(i, "_")

list = ''.join(list)

print(list)