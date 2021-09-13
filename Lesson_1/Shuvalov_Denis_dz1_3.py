# procent = int(input('введите число'))

for i in range(1, 101):
    my_str = str(i)
    my_list = list(my_str)
    if int(my_list[-1]) == 1 and i != 11:
        print('{} процент'.format(i))
    elif int(my_list[-1]) > 1 and int(my_list[-1]) <= 4:
        if i > 10 and i <= 14:
            print('{} процентов'.format(i))
        else:
            print('{} процента'.format(i))
    else:
        print('{} процентов'.format(i))
