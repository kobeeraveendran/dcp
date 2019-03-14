def sum_check(num_list, k):
    seen = set()

    for i in range(len(num_list)):
        if k - num_list[i] in seen:
            return True
        
        seen.add(num_list[i])

    return False

num_list = [10, 15, 3, 7]
k = 17

print(sum_check(num_list, k))