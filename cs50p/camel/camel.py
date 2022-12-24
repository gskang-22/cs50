camel = input("camelCase: ")
new = ""

for letter in camel:
    if letter.isupper():
        new = new + "_" + letter.lower()
    else:
        new += letter

print(new)