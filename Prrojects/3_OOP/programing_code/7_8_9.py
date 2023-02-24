# recursive approach
# def lessThan(lst,n):
#     if len(lst) == 0: return []
#     else:
#         return lessThan(lst[1:], n) if lst[0] >= n else [lst[0]] + lessThan(lst[1:], n)
    
# list comprehension approach
# def lessThan(lst, n):
#     return [x for x in lst if x < n]

# high-order function approach
def lessThan(lst, n):
    return list(filter(lambda x: x < n, lst))

    
print(lessThan([1,2,3,4,5],4))  # [1,2,3])