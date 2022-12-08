x = input("Input: ")
new = ""

for letter in x:
    if letter.lower() != "a" or "e" or "i" or "o" or "u":
        new += letter

print(new)