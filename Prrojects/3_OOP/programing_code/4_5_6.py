# recursive approach
# def dist(lst,n):
#     if len(lst) == 0: return []
#     elif len(lst) == 1:
#         return [(lst[0], n)]
#     else:
#         return [(lst[0], n)] + dist(lst[1:], n)

# def dist(lst,n):
#     return [(x, n) for x in lst]

# high-order function approach
def dist(lst, n):
    return list(map(lambda x: (x, n), lst))


print(dist([],4))
    