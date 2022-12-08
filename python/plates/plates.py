def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    count_letters = 0
    if not s[0:1].isalpha():
        return False
    elif len(s) > 6 or len(s) < 2:
        return False
    for char in s:
        if not char.isalpha() or not char.isdigit():
            return False
        
