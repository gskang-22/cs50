cost = 50
print(f"Amount Due: {cost}")

while cost > 0:
    coin = input("Insert Coin: ")
    if coin == "25" or coin == "10" or coin == "5":
        cost -= int(coin)
        if cost > 0:
            print(f"Amount Due: {cost}")
        elif cost <= 0:
            print(f"Change owed: {-cost}")
    else:
        print(f"Amount Due: {cost}")
