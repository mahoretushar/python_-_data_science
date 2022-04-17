# program to display Fibonacci series up to n-th term
num = int(input("Enter how many numbers you want to display: "))
n1 = 0
n2 = 1
count = 0
print("Fibonacci series:")
print(n1)
print(n2)
while count < num:
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
    count += 1

