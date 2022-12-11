def main():
    x = input("Input: ").lower()
    word = shorten(x)
    print(f"Output: {word}")


def shorten(word):
    word_new = ""
    for char in word:
        if char != "a" and char != "e" and char != "i" and char != "o" and char != "u":
            word_new += char
            return word_new


if __name__ == "__main__":
    main()