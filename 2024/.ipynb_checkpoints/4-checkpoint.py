count_xmas = 0
words_to_find = ['XMAS', 'SAMX']
with open('inputs/4.txt') as data:
    data_l = [row.strip() for row in data]
for row in data_l:
    for i in range(len(row)-3):
        count_xmas += row[i:i+4] in words_to_find
for column in zip(*data_l):
    for i in range(len(column)-3):
        count_xmas += ''.join(column[i:i+4]) in words_to_find
for row in range(len(data_l)-3):
    for col in range(len(data_l[0])-3):
        x_diag_1 = ''.join([data_l[row][col],data_l[row+1][col+1],data_l[row+2][col+2],data_l[row+3][col+3]])
        x_diag_2 = ''.join([data_l[row+3][col],data_l[row+2][col+1],data_l[row+1][col+2],data_l[row][col+3]])
        count_xmas += x_diag_1 in words_to_find
        count_xmas += x_diag_2 in words_to_find
print(count_xmas)
count_mas = 0
mas_to_find = ['MAS', 'SAM']
for row in range(len(data_l)-2):
    for col in range(len(data_l[0])-2):
        m_diag_1 = ''.join([data_l[row][col],data_l[row+1][col+1],data_l[row+2][col+2]])
        m_diag_2 = ''.join([data_l[row+2][col],data_l[row+1][col+1],data_l[row][col+2]])
        count_mas += m_diag_1 in mas_to_find and m_diag_2 in mas_to_find
print(count_mas)