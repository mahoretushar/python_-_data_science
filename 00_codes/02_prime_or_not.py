# Check number is prime or not

n = int(input("Enter a Number: "))
for i in range(2, n + 1):
    if n % i == 0:
        break

if i == n:
    print(n, " is a prime number")
else:
    print(n, " is not a prime number")
