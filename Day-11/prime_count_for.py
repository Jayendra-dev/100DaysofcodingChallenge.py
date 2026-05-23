# Day-11: Count primes upto n using for loops.
n = int(input("enter n:"))  # yaha tak prime ginne hai
count = 0

# 2 se n tak har number check karo
for num in range(2, n + 1):
    is_prime = True
    
    # check karo num prime hai ya nahi
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break  # divide ho gaya to prime nahi hai
    
    if is_prime:
        count = count + 1

print("Prime numbers upto", n, ":", count)  # n=10 ke liye output: 4
