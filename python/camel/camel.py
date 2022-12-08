camel = input("camelCase: ")
for i in range(len(camel)):
    if camel[i].isupper():
        camel[i].lower()
        camel.insert(i, "_")
print(camel)