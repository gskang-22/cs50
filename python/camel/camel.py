camel = input("camelCase: ")
list = list(camel)

for i in range(len(list)):
    list[i].lower()
    list.insert(i, "_")

list = ''.join(list)

print(list)