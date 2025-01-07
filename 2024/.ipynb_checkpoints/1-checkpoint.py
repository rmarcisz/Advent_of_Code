#part 1
data = open('inputs/1.txt')
left = []
right = []
total_1 = 0
for row in data:
    row_split = row.split()
    left.append(int(row_split[0]))
    right.append(int(row_split[1]))
data.close()
for pair in range(len(right)):
    diff = abs(min(right) - min(left))
    total_1 += diff
    left.remove(min(left))
    right.remove(min(right))
print(f'The final value is equal to {total_1}')
#part 2
data = open('inputs/1.txt')
left = []
right = []
total_1 = 0
for row in data:
    row_split = row.split()
    left.append(int(row_split[0]))
    right.append(int(row_split[1]))
data.close()
total_2 = 0
for number in left:
    multiplier = right.count(number)
    total_2 += (number * multiplier)
print(f'Turns out final value is actually equal to {total_2}')

