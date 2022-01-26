from sys import getsizeof

values_1 = [x * 2 for x in range(100000)]

# for x in values_1:
#     print(x)

values_2 = (x * 2 for x in range(5))
print(values_2)

# for x in values_2:
#     print(x)

print("List: ", getsizeof(values_1))
print("Gen: ", getsizeof(values_2))
# print(len(values_2))
