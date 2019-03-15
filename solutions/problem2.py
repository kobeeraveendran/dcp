# initial soln - O(n)
def evolved_arr(array):

    cumulative_product = 1

    if array.count(0) >= 2:
        return [0] * len(array)

    for num in array:
        cumulative_product *= num

    if array.count(0) == 1:
        evo_array = [0] * len(array)
        special_product = 1

        for i in range(len(array)):
            if array[i] == 0:
                continue
            special_product *= array[i]

        evo_array[evo_array.index(0)] = special_product
        
        return evo_array

    evo_array = []

    for num in array:
        evo_array.append(cumulative_product // num)

    return evo_array

# without division (naive approach) - O(n^2)
def evolved_arr_naive(array):

    evo_array = []

    for i in range(len(array)):
        temp_product = 1

        for j in range(len(array)):
            if i == j:
                continue

            temp_product *= array[j]

        evo_array.append(temp_product)

    return evo_array


# test case(s)
test1 = [1, 2, 3, 4, 5]
test2 = [3, 2, 1]
test3 = [0, 0, 1, 2] # edge case 1 - zeros
test4 = [0, 1, 2, 3] # edge case 2 - zeros

print(evolved_arr(test1))   # expected output: [120, 60, 40, 30, 24]
print(evolved_arr(test2))   # expected output: [2, 3, 6]
print(evolved_arr(test3))   # expected output: [0, 0, 0, 0]
print(evolved_arr(test4))   # expected output: [6, 0, 0, 0]

# naive tests
print(evolved_arr_naive(test1))
print(evolved_arr_naive(test2))
print(evolved_arr_naive(test3))
print(evolved_arr_naive(test4))