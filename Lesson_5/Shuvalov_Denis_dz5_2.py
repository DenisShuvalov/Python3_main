x = int(input("число до: "))

print(*[y for y in range(1, x) if y % 2])