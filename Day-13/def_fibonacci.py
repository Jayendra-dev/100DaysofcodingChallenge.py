# fibonacci series using def
n=int(input("enter n:"))
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(n)
