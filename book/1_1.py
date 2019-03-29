'''
1.1 Get product of all other elements

Given an array of integers, return a new array such that each element at index i of the new 
array is the product of all the numbers in the original array except the one at i.

ex.
input: [1, 2, 3, 4 5]           output: [120, 60, 40, 30, 24]
input: [3, 2, 1]                output: [2, 3, 6]

Follow-up: What if you can't use division?
'''

# with division
def get_products(array):

    total_product = 1

    for num in array:
        total_product *= num

    new_arr = []

    for num in array:
        new_arr.append(total_product / num)

    return new_arr

# without division
def get_products_bonus(array):
    