# write a function to check armstrong
#logic:wo no. jiska total digits ki power krke jodo,to wahi no.wapas mil jaye.
# 153=1^3+5^3+3^3=1+125+27=153,
# 9474,
n=int(input("enetr n:"))
def is_armstrong(num):
    m= len(str(num))          # Step 1: Digit count nikaalo
    temp = num                 # Step 2: Copy bana lo
    total = 0                    # Step 3: Sum ke liye dabba
    
    while temp > 0:            # Step 4: Jab tak number bacha hai
        digit = temp % 10      # Step 5: Last digit nikaalo
        total+= digit ** m      # Step 6: Power karke sum me jodo
        temp //= 10            # Step 7: Last digit hata do
    
    return total == num          # Step 8: Check karo barabar hai ya nahi
    
print(is_armstrong(n))       # True/false aayega
