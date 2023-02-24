# recursive approach
def lstSquare(n):
    if n == 1:
        return [1]
    else:
        return lstSquare(n-1) + [n**2]

# list comprehension approach
def lstSquare(n):
    return [i**2 for i in range(1,n+1)]

# high-order function approach
def lstSquare(n):
    return list(map(lambda x: x**2, range(1,n+1)))

print(lstSquare(3))