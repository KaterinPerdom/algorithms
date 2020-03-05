"""
Given a list, returns an item from the list 
each skip, until empty.

Example
a=[1,2,3,4]

circ_counter(a, 2)
2
4
3
1

"""
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def circ_counter(int_list, skip):
    skip = skip - 1  # list starts with 0 index
    idx = 0
    while len(int_list) > 0:
        # hashing to keep changing the index to every 3rd
        idx = (skip + idx) % len(int_list)
        print(int_list.pop(idx))


circ_counter(a, 3)
