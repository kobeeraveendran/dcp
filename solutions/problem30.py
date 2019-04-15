def calculate_water_trapped(array):

    limit = min(array[0], array[-1])
    water = 0

    for wall in array:
        if wall < limit:
            water += limit - wall

    return water

# O(n) time, O(1) space
def calculate_water_trapped_complete(array):

    cap = min(array[0], array[-1])

    water = 0

    for i in range(1, len(array) - 1):
        
        if array[i - 1] > cap and array[i + 1] > cap:
            limit = min(array[i - 1], array[i + 1])
            water += limit - array[i] if array[i] < limit else 0
        else:
            water += cap - array[i] if array[i] < cap else 0

    return water

test1 = [2, 1, 2]
test2 = [3, 0, 1, 3, 0, 5]
test3 = [3, 0, 0, 2, 0, 4]
test4 = [1, 2, 3, 2, 1]
test5 = [2, 0, 5, 0, 4, 1, 3]
test6 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(calculate_water_trapped(test1))       # expected out: 1
print(calculate_water_trapped(test2))       # expected out: 8
print(calculate_water_trapped(test3))       # expected out: 10
print(calculate_water_trapped(test4))       # expected out: 0
print(calculate_water_trapped(test5))       # expected out: 8
print(calculate_water_trapped(test6))       # expected out: 6

print('--------------')

print(calculate_water_trapped_complete(test1))      # expected out: 1
print(calculate_water_trapped_complete(test2))      # expected out: 8
print(calculate_water_trapped_complete(test3))      # expected out: 10
print(calculate_water_trapped_complete(test4))      # expected out: 0
print(calculate_water_trapped_complete(test5))      # expected out: 8
print(calculate_water_trapped_complete(test6))      # expected out: 6