camel = input("camelCase: ")
list = list(camel)

for i in range(len(list)):
    list[i].lower()
    

list = ''.join(list)

print(list)