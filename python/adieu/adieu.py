import inflect
p = inflect.engine()
list = []

while True:
    try:
        x = input("Name: ")
        list.append(x)

    except EOFError:
        
        print(f"Adieu, adieu, to {}")
        break