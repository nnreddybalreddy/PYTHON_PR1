
def flatten(lst):
    for item in lst:
        if hasattr(item,'__iter__'):
            # print(f'iterable {item}')
            yield from flatten(item)
        else:
            # print(f'{item} is not iterable')
            yield item
L=[1,2,[3,4,[5,6,7],8],9,[10,11]]


flat=flatten(L)

flat_list=list(flat)
print(flat_list)

#$ python flatten.py
# 1 is not iterable
# 2 is not iterable
# iterable [3, 4, [5, 6, 7], 8]
# 3 is not iterable
# 4 is not iterable
# iterable [5, 6, 7]
# 5 is not iterable
# 6 is not iterable
# 7 is not iterable
# 8 is not iterable
# 9 is not iterable
# iterable [10, 11]
# 10 is not iterable
# 11 is not iterable

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]