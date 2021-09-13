list_of_cubes = []
list_of_cubes_new = []
all_sum = 0

for i in range(1, 1000, 2):
    list_of_cubes.append(i ** 3)

for ind, val in enumerate(list_of_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits = sum_digits + val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum = all_sum + list_of_cubes[ind]

print(all_sum)

for m in list_of_cubes:
    list_of_cubes_new.append(m + 17)

all_sum = 0
for ind, val in enumerate(list_of_cubes_new):
    sum_digits = 0
    while val > 0:
        sum_digits = sum_digits + val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum = all_sum + list_of_cubes_new[ind]

print(all_sum)