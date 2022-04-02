# 1
# 2 3
# 4 5 6
# 7 8 9 1
# 2 3 4 5 6

count = 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(count, end=' ')
        count += 1
        if count > 9:
            count = 1
    print()
