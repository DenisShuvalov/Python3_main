price = [57.8, 46.51, 97, 7, 61.4, 99, 55.44, 12, 14.4, 891,
         55.2, 69, 13, 19.14, 44, 22.8]

print(id(price))

for i in price:
    r, k = str(f"{i:.2f}").split(".")
    print(r, "руб.", f"{int(k):02} коп.,", end=" ")



print(f"\n\n\n{'-' * 50} B\n")

price.sort()
print(price)
print(id(price))

print(f"\n\n\n{'-' * 50} C&D\n")

price_rev = price[::-1]
print(price_rev)
print(id(price_rev))

print(price_rev[:5])