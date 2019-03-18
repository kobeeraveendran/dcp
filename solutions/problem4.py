# naive but close - O(n) time, O(n) additional space
def firstMissingPositive(array):

    seen = set()

    for num in array:
        if num > 0:
            seen.add(num)

    for i in range(1, len(array) + 1):
        if i not in seen:
            return i

# more efficient - O(n) time, O(1) additional space
# approach: use array indices as keys to a "dict", similar to above
# solution but without extra space
# i.e. in [3, 4, 1], to denote that we've seen 1, 3, and 4, we have:
# [x, o, x], subtracting 1 to adjust for indexing rules
# with this, we see that 1 (1 - 1 = 0, x), 3 (3 - 1 = 2, x) are seen, and 4 - 1
# is out of range, so its position is o
# thus, the missing integer is either an o index (+1 to account for indexing)
# or if no o's are found, the length of the array +1
def firstMissingPositive_improved(array):

    array = remove_negatives(array)

    # [3, 4, 1] -> [4, 3, 1]
    # [1, 2, 0] -> [2, 1]
    l = len(array) # 3, 2

    for i in range(l):
        if abs(array[i]) - 1 < l and array[abs(array[i]) - 1] > 0:
            array[abs(array[i]) - 1] *= -1

    # [-4, 3, -1]
    # [-2, -1]

    for i in range(l):
        if array[i] > 0:
            return i + 1

    return l + 1

def remove_negatives(array):

    index = 0

    for i in range(len(array)):
        if array[i] <= 0:
            tmp = array[index]
            array[index] = array[i]
            array[i] = tmp
            index += 1


    return array[index:]

# test cases
test1 = [3, 4, -1, 1]
test2 = [1, 2, 0]

print(firstMissingPositive(test1))      # expected output: 2
print(firstMissingPositive(test2))      # expected output: 3

# better soln
print(firstMissingPositive_improved(test1))
print(firstMissingPositive_improved(test2))