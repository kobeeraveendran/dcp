def calculate_water_trapped(array):

    limit = min(array[0], array[-1])
    water = 0

    for wall in array:
        if wall < limit:
            print('water gains: ', limit - wall)
            water += limit - wall

    return water

test1 = [2, 1, 2]
test2 = [3, 0, 1, 3, 0, 5]
test3 = [3, 0, 0, 2, 0, 4]
test4 = [1, 2, 3, 2, 1]

print(calculate_water_trapped(test1))       # expected out: 1
print(calculate_water_trapped(test2))       # expected out: 8
print(calculate_water_trapped(test3))       # expected out: 10
print(calculate_water_trapped(test4))       # expected out: 0