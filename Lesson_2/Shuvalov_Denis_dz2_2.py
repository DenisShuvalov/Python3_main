uncorrect_list = ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05',
                  '"', 'градусов']
# print(id(uncorrect_list))
correct_list = []

for i in uncorrect_list:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            correct_list.append(f"{int(i):02}")
        else:
            correct_list.append(f"{i[0]}{int(i[1:]):02}")
    else:
        correct_list.append(i)

print(" ".join(correct_list))
