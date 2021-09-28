from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Кирилл', 'Федор']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result = ((t, k) for t, k in zip_longest(tutors, klasses))

print(*result, sep=' ')
print(type(result))
# print(next(result))
