def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:1].isalpha():
        return False

    elif len(s) > 6 or len(s) < 2:
        return False

    for char in s:
        if not char.isalpha() and not char.isdigit():
            return False

    for i in range(len(s)):
        if s[i].isdigit() and not s[i:len(s)].isdigit():
            return False

    return True

main()
