# Recursion : It is a function that calls itself, very recursive function has two cases: the base case and the recursive case.
# Examples :
def factorial(num):
    if num <= 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))

# Fibonacci Sequence

num_list = []


def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


for i in range(10):
    num_list.append(fibonacci(i))
print(num_list)


# sum of the elements in a list using recursion
def sum_of_list(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_of_list(array[1:])
    

# Calculating the number of elements in a list using recursuion

def array_len(array):
    if not array:
        return 0
    else:
        return 1 + array_len[1:]
