enter_names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
               'директор аэлита']

for i in enter_names:
    i = i.title()
    name = i.rpartition(' ')
    print('Привет,', name[-1]+'!', sep=" ")