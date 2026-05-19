# Check Armstrong or not using while loop
n = int(input("enter number Here:"))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum += digit ** 3
    n //= 10

if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")
