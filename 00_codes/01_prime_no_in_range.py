# program to print prime number in range

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for n in range(start, end + 1):
    if n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                break
            else:
                print(n)
