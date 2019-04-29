def count_inversions(array):

    count = 0

    for i in range(len(array) - 1):
        sub_array = array[i + 1:]

        for j in range(len(sub_array)):
            if sub_array[j] < array[i]:
                count += 1

    return count

test1 = [2, 4, 1, 3, 5]
test2 = [5, 4, 3, 2, 1]
test3 = [1, 2, 3, 4, 5]

print(count_inversions(test1))      # expected out: 3
print(count_inversions(test2))      # expected out: 10
print(count_inversions(test3))      # expected out: 0