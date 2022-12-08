cost = 50
print(f"Amount Due: {cost}")

while cost > 0:
    input = input("Insert Coin: ")
    if input == "25" or input == "10" or input == "5":
        cost -= int(input)
        print(f"Amount Due: {cost}")


print(f"Change owed: {-cost}")