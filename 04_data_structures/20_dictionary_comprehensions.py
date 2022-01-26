# values = []
# for x in range(5):
#     values.append(x * 2)

values_1 = [x * 2 for x in range(5)]
print(values_1)

values_2 = {x * 2 for x in range(5)}
print(values_2)

values_3 = {x: x * 2 for x in range(5)}
print(values_3)

values_4 = (x*2 for x in range(5))
print(values_4)
