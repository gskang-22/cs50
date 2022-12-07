input = input("Expression: ")
x, y, z = input.split(" ")
x = int(x)
z = int(z)
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)