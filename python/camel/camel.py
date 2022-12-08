camel = input("camelCase: ")
for i in range(len(camel)):
    if camel[i] == "_":
        camel[i] = " "