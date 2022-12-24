x = input("Input: ")
new = ""

for letter in x:
    if letter.lower() != "a" and letter.lower() != "e" and letter.lower() != "i" and letter.lower() != "o" and letter.lower() != "u":
        new += letter

print(f"Output: {new}")