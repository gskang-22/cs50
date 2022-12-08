cost = 50
print(f"Amount Due: {cost}")

while cost > 0:
    coin = input("Insert Coin: ")
    if coin == "25" or coin == "10" or coin == "5":
        cost -= int(coin)
        print(f"Amount Due: {cost}")


print(f"Change owed: {-cost}")