with open("new_log1.txt", "w", encoding="utf-8") as p:
    with open("nginx_logs.txt", "r", encoding="utf-8") as n:
        content = (f"{line.split()} {line.split()[5][1:]} {line.split()[6]}" for line in n)
        for i in content:
            print(i, file=p)