# print prime numbers in range
start = int(input("enter starting number:"))
end = int(input("enter  ending no. here:"))

while start <= end:
    i = 2
    flag = 0

    while i < start:
        if start % i == 0:
            flag = 1
            break
        i += 1

    if start > 1 and flag == 0:
        print(start)

    start += 1
