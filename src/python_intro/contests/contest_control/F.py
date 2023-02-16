l = list(map(int, input().split()))
size = l[0]
num = l[1]
mat = []
for i in range(0, size):
    row_spl = input().split()
    row = []
    for j in range(0, len(row_spl)):
        row += [[abs(int(row_spl[j]) - num), int(row_spl[j])]]

    mat += [row]

sorted_by_column = []
for i in range(0, size):
    column = []
    for j in range(0, size):
        column += [mat[j][i]]

    column.sort()
    sorted_by_column += [column]

another_mat = []
for i in range(0, size):
    row = []
    for j in range(0, size):
        row += [sorted_by_column[j][i]]

    another_mat += [row]

for row in another_mat:
    for i in range(0, len(row)):
        if i != size - 1:
            print(row[i][1], end=" ")
        else:
            print(row[i][1])