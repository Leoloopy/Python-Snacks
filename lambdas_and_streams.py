# Regular functions
# def add(a: int, b: int) -> int:
#     """Adds a number"""
#     return a + b


# print(add.__name__)
# print(add.__doc__)
# print(add.__annotations__)

# Higher order functions -- taking a function as a parameter
def operates(x, y, func):
    return func(x, y)


#
# print(operates(2, 3, add))

# currying
# def multiply(a):
#     def by(b):
#         return a * b
#
#     return by
#
#
# multiply_by_five = multiply(5)
#
# print(multiply_by_five(6))

# lambdas

# adder = lambda a, b: a + b
#
# print(adder(10, 9))
# print(operates(2, 3, adder))
# print(operates(2, 3, lambda a, b: a + b))
# print(operates(2, 3, lambda a, b: a - b))
# print(operates(2, 3, lambda a, b: a * b))

import builtins

sum = 67

print(builtins.sum([1, 2, 3]))
