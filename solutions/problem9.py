import heapq
import copy

def largest_nonadjacent_sum(array):
    '''
    strat: save two sums, one from before the current index and one after adding it
    '''
    cached, maxi = 0, 0

    for num in array:
        if num + cached > maxi:
            tmp = maxi
            maxi = num + cached
            cached = tmp
        else:
            cached = maxi

    return maxi

test1 = [2, 4, 6, 2, 5]         # expected out: 13
test2 = [5, 1, 1, 5]            # epxected out: 10
test3 = [-92, -1, 8, 92]        # expected out: 92

print(largest_nonadjacent_sum(test1))
print(largest_nonadjacent_sum(test2))
print(largest_nonadjacent_sum(test3))