def main():
    x = input("Input: ").lower()
    word = shorten(x)
    print(f"Output: {word}")


def shorten(word):
    word_new = ""
    for char in word():
        if char.lower() != "a" and char.lower() != "e" and char.lower() != "i" and char.lower() != "o" and char.lower() != "u":
            word_new += char
    return word_new


if __name__ == "__main__":
    main()