# print greatest common divisor or Highest common Factor of two no.
a = int(input("enter first number :"))
b = int(input("enter second number:"))

while b != 0:
    a, b = b, a % b

print(a)
