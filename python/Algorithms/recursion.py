# Recursion : It is a function that calls itself, very recursive function has two cases: the base case and the recursive case. 
# Examples : 
def factorial(num):
    if (num <= 0):
        return 1
    else:
        return num * factorial(num-1)
print(factorial(5))

# Fibonacci Sequence 

num_list = []
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return (fibonacci(num-1) + fibonacci(num-2))

for i in range(10):
    num_list.append(fibonacci(i))
print(num_list)