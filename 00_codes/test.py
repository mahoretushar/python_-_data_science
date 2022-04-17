name = "Tushar Ravindra Mahore"


def count_upper_lower(name_one):
    upper = 0
    lower = 0
    for charcater in name_one:
        if charcater.islower():
            lower += 1
        elif charcater.isupper():
            upper += 1
    print(f"Lower: {lower}")
    print(f"Upper: {upper}")


count_upper_lower(name)
