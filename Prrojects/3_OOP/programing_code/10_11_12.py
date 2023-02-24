from functools import reduce

# recursive approach
# def flatten(lst):
#     if len(lst) == 0: return []
#     else:
#         return lst[0] + flatten(lst[1:])


# list comprehension approach
# def flatten(lst):
#     return [item for sublst in lst for item in sublst]

# high-order function approach
def flatten(lst):
    return reduce(lambda item, sublst: item + sublst, lst)


print(flatten([[1,2,3],[4,5],[6,7]]))      # [1,2,3,4,5,6,7]