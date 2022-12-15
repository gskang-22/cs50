from validator_collection import validators

def main():
    print(validate(input("What's your email address? ")))

def validate(s):
    if is_email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()