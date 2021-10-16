from pprint import pprint


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([f"{itm:03}" for itm in line]) for line in self.data)

    def __add__(self, other):
        try:
            m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                 for line in range(len(self.data))]
            return Matrix(m)
        except IndexError:
            return f'Error matrix dimension'


m_1 = [[3, 1, 44], [12, 4, 1], [2, -44, -7]]
m_2 = [[12, 12, 1], [2, 4, 12], [-12, 4, 3]]

# mtrx_1 = Matrix(m_1)
# mtrx_2 = Matrix(m_2)
# main_matrix = mtrx_2 + mtrx_1
#
# # pprint(main_matrix)

stroki = int(input('Количеств строк и столбцов  '))
stoplbi = stroki

matrix1 = Matrix([[i * j for j in range(stroki)] for i in range(stoplbi)])
matrix2 = Matrix([[i * j for j in range(stroki)] for i in range(stoplbi)])

print('1st matrix:\n', matrix1, end='\n\n')
print('2nd matrix:\n', matrix1, end='\n\n')
print('Summ of 1st and 2nd maxtrix:\n', matrix1 + matrix2)
