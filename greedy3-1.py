price = int(input("Enter Price : "))

coin_list = [500, 100, 50, 10]

for coin in coin_list :
    print(f"{coin}$ : {price//coin}")
    price = price%coin