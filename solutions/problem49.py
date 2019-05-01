def max_sum_subarray(array):

    best_sum = 0
    curr_sum = 0

    for num in array:

        curr_sum += num

        if curr_sum > best_sum:
            best_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0

        #print(curr_sum)

    return max(best_sum, 0)

test1 = [34, -50, 42, 14, -5, 86]
test2 = [-5, -1, -8, -9]

print('testcase 1: ', max_sum_subarray(test1))      # expected out: 137
print('testcase 2: ', max_sum_subarray(test2))      # expected out: 0 (include none of the elements)