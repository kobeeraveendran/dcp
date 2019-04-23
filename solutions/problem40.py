# O(kN) -> O(N) time; O(k) space, where k is the number of distinct integers
def find_single(array):

    classes = list(set(array))

    for item in classes:
        if array.count(item) == 1:
            return item
        
test1 = [6, 1, 3, 3, 3, 6, 6]
test2 = [13, 19, 13, 13]

print(find_single(test1))   # expected out: 1
print(find_single(test2))   # expected out: 19