dict = {}

while True:
    try:
        item = input("").upper

        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1

    except EOFError:
        for key in dict:
            print(f"{dict[key]} {key}")

        break