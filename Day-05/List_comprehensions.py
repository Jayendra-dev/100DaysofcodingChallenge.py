#Topic 1:list comprehension
#problem:ek list hai nums=[1,2,3,4,5,6,7,8]
#Task :Isme sirf even numbers ka square wali new list banao.
nums = [1,2,3,4,5,6,7,8]
even_squares = [x*x for x in nums if x % 2 == 0]
print(even_squares)  # Output: [4, 16, 36, 64]
