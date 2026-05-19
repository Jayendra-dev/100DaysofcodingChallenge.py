# Do product of digits using while loop.
n = int(input( "enter number Here:"))
product = 1

while n > 0:
    product *= n % 10
    n //= 10

print(product)
