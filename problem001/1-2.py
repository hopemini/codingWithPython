amount = 1260

coin_types = [500, 100, 50, 10]
total = 0

for coin in coin_types:
    total += amount // coin
    amount %= coin

print(total)
