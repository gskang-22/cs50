# TODO
import cs50

text = cs50.get_string("Text: ")

letters = 0
words = 1
sentences = 0

for char in text:
    if char.isalpha() == True:
        letters += 1
    elif char == ' ':
        words += 1
    elif char == '.' or char == '!' or char == '?':
        sentences += 1

index = 0.0588 * (letters / words * 100) - 0.296 * (sentences / words * 100) - 15.8
index = round(index)

if index > 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")