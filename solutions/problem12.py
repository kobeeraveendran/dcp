def climb(n):

    if n == 0:
        return 1

    if n < 2:
        return climb(n - 1)

    else:
        return climb(n - 1) + climb(n - 2)

# i.e. X = {1, 3, 5}
def climb_generalized(n, x):

    # assuming you can't "over-step" the staircase; in other words, the number of remaining steps must be 0 or greater
    if n <= 1:
        return 1 if n >= 0 else 0

    n_ways = 0
    
    for step_size in x:
        
        n_ways += climb_generalized(n - step_size, x)
        
    return n_ways

print(climb(4))                         # expected out: 5
print(climb(5))                         # expected out: 8
print(climb(3))                         # expected out: 3

print(climb_generalized(4, [1, 2]))     # expected out: 5 (this is essentially the same as the first base test)
print(climb_generalized(4, [1, 3]))     # expected out: 3 (assuming no over-stepping)
print(climb_generalized(4, [1, 3, 5]))  # expected out: 3 (assuming no over-stepping)