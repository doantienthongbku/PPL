# Write a function that takes a list of numbers and returns 
# the product of all the numbers using reduce high-order function.

from functools import reduce

def product(numbers):
    return reduce(lambda x, y: x * y, numbers)


# Write a function that takes a list of strings and
# returns a new list with only the palindromes using reduce high-order function.

def palindromes(strings):
    def is_palidromes(s):
        return (s == s[::-1])

    return reduce(lambda x, y: x + [y] if is_palidromes(y) else x, strings, [])


# Write a function that takes a list of tuples with two numbers each and 
# returns a new list with the sum of each pair using reduce high-order function.
def sum_pairs(pairs):
    return reduce(lambda lst, p: lst + [p[0] + p[1]], pairs, [])

if __name__ == "__main__":
    print(sum_pairs([(1, 2), (3, 4), (5, 6), (7, 8)]))