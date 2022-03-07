# In Python we have 3 Logical Operators to model more complex conditions
# and
# or
# not

passing_year_2021 = True
has_high_score = False
arts_student = True

# In below line of code we did not compare passing_year == True because, passing_year is a boolean and it's either
# true or false
if passing_year_2021 and has_high_score:
    print("Eligible for Interview")
else:
    print("Not Eligible for Interview")

# Let's take a look at not operator
if not arts_student:
    print("Eligible")
else:
    print("Not Eligible")

# Complex conditions
if (passing_year_2021 or has_high_score) and not arts_student:
    print("Eligible")
else:
    print("Not Eligible")
