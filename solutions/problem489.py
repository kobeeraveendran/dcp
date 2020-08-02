def longest_subarray_len(array):

    seen = set()
    count = 0

    for num in array:
        if num in seen:
            seen.clear()
            seen.add(num)
            count = 1

        else:
            seen.add(num)
            count += 1

    return count

test = [5, 1, 3, 5, 2, 3, 4, 1]

print("Input: ", test)
print("Output: ", longest_subarray_len(test))