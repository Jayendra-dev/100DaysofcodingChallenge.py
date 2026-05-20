# print fibonacci series upto n using while loop.
n = int(input("enter your number here:"))

a, b = 0, 1
i = 1

while i <= n:
    print(a)
    a, b = b, a + b
    i += 1
