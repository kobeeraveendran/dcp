# naive but close - O(n) time, O(n) additional space
def firstMissingPositive(array):

    seen = set()

    for num in array:
        if num > 0:
            seen.add(num)

    for i in range(1, len(array) + 1):
        if i not in seen:
            return i

test1 = [3, 4, -1, 1]
test2 = [1, 2, 0]
test3 = [3, 3, 4, -1, 1]

print(firstMissingPositive(test1))      # expected output: 2
print(firstMissingPositive(test2))      # expected output: 3
print(firstMissingPositive(test3))      # expected output: 2