x = input("Input: ")
new = ""

for letter in x:
    if letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u":
        new += letter

print(f"Output: {new}")