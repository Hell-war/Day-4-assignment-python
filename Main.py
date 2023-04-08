'''Write a Python function that takes in a list of numbers and returns the sum of the squares of all the numbers in the list.'''


def sum_of_squares(numbers):
    return sum([num ** 2 for num in numbers])
numbers = [1, 2, 3, 4, 5]
result = sum_of_squares(numbers)
print(result)