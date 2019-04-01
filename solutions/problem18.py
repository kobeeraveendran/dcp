# straight-forward way: O(k * n)
def max_subarray(array, k):

    for i in range(len(array) - k + 1):
        subarray = array[i:i + k]
        print(max(subarray))



test1 = [10, 5, 2, 7, 8, 7]

max_subarray(test1, k = 3)