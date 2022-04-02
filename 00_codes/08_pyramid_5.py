#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

for row in range(1, 6):
    for sp in range(1, 6 - row):
        print(' ', end=' ')
    for col in range(1, row + 1):
        print(col, end=' ')
    for erow in range(col - 1, 0, -1):
        print(erow, end=' ')
    print()
