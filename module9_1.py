def square (x):
    return x ** 2

def is_odd(x):
    return x % 2

my_numbers = [1,2,5,7,12,11,35,4,89,10]
result = map(square, filter(is_odd, my_numbers))
print(list(result))