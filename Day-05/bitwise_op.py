# Bitwise and (&) operator
1.# AND &-Dono 1 Hoge Tabhi 1
# RULE:  1 & 1 =1,baaki sab 0
 # Use:kisi bit ko check karna ,mask lagana
a = 5  # 101
b = 3  # 011
print(a & b)  # 001 = 1

# Real Use:   Number Even hai ya Odd?
num = int(input("enter no. here:")) # 0111
if num & 1:  # 0111 & 0001 = 0001 = 1 = True
    print("Odd hai")  # Ye chalega
else:
    print("Even hai")
    # Odd no. ka last bit hamesha 1 hota h .& 1 se turant pata chal jata h.


# 2.OR (|):   KOI  1 BHI BAAT 1 HO TO 1.
# use:kisi bit ko set karna =1 banana.
a = 5  # 101
b = 3  # 011
print(a | b)  # 111 = 7

# Real Use: Permission dena
READ = 4   # 100
WRITE = 2  # 010
EXECUTE = 1 # 001

user_permission = READ | WRITE  # 100 | 010 = 110 = 6
print(user_permission)  # 6 = Read + Write permission mil gaya.


# XOR (^):   alag h to 1 ,Same h to 0.
# use : number swape karna ,toggle karna ,duplicate dhundhna.
a = 5  # 101
b = 3  # 011
print(a ^ b)  # 110 = 6

# Real Use: Bina 3rd variable ke swap
x = 10  # 1010
y = 7   # 0111
x = x ^ y  # x = 1101 = 13
y = x ^ y  # y = 1010 = 10 
x = x ^ y  # x = 0111 = 7
print(x, y)  # 7 10  Swap ho gaya bina temp ke


#  4.NOT(~):   ulta kar de .0 ko 1,1 ko zero.
# Rule:~0=1,~1=0 lekin python me thoda twist h.
# Python formula :~n=-(n+1)
a = 5  # 00000101
print(~a)  # -(5+1) = -6

# Kyu -6? Kyunki computer negative number 2's complement mein store karta
# 5 = 00000101 → NOT → 11111010 → Ye -6 hota hai


# 5.Left SHIFT(<<):  BIT ko laft khiska ,2 se multiply
#Rule:a << n=a*2^n
# USE :Fast Multiplication
a = 5  # 101
print(a << 1)  # 1010 = 10  = 5 * 2
print(a << 2)  # 10100 = 20 = 5 * 4
print(a << 3)  # 101000 = 40 = 5 * 8

# Real Use: 2 se multiply karna ho to ye sabse fast hai
salary = 50000
double_salary = salary << 1  # 100000  ek second mein


# 6.RIGHT SHIFT(>>):  BIT ko right khiska ,2 se divide 
#  Rule: a >> n=a//2^n
#USE:FAST DIVISION
a = 20  # 10100
print(a >> 1)  # 1010 = 10  = 20 // 2
print(a >> 2)  # 0101 = 5   = 20 // 4

# Real Use: Binary search mein mid nikalna
start = 0
end = 100
mid = (start + end) >> 1  # (100) >> 1 = 50  Fast division


print("CONSISTENCY>INTENSITY")



# QUESTION:check karo number 2 ki power h ya nhi ?
#TRICK: 2 ki power kA binary  hamesha 1000...... type hota h.
def is_power_of_two(n):
    # 8 = 1000,  8-1=7=0111,  1000 & 0111 = 0000
    return n > 0 and (n & (n-1)) == 0

print(is_power_of_two(8))   # True
print(is_power_of_two(10))  # False