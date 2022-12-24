input = input("Expression: ")
x, y, z = input.split(" ")
x = float(x)
z = float(z)
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(round((x * z), 2))
elif y == "/":
    print(round((x / z), 2))