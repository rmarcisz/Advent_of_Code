#part 1
import re
result = 0
data_string = ''
data = open('inputs/3.txt')
for row in data:
    data_string += row
data.close()
def get_values(string):
    result = 0
    txt = re.findall('mul[(][0-9]{0,3}[,][0-9]{0,3}[)]', string)
    for i in txt:
        i = i.replace('mul(', '')
        i = i.replace(')', '')
        i = i.split(',')
        multiplied = int(i[0]) * int(i[1])
        result += multiplied
    return result
print(get_values(data_string))
#part 2
data_2_split = []
workables = []
data_string_workables = ''
data_2 = 'YYY' + data_string 
data_2 = data_2.replace('do()', 'do()YYY')
data_2 = data_2.replace('''don't()''', '''don't()NNN''')
data_2 = data_2.split('do()')
for elem in data_2:
    app = elem.split('''don't()''')
    data_2_split.append(app)
for elem in data_2_split:
    for subelem in elem:
        if subelem[:3] == 'YYY':
            workables.append(subelem)
for elem in workables:
    data_string_workables += elem
print(get_values(data_string_workables))