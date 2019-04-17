def rgb_sort(text):

    num_r = text.count('R')

    r_init = text.index('R')

    r_count = 0
    mark = 0

    for i in range(len(text)):
        if text[i] == 'R':
            if r_count != num_r:
                text = swap(text, i, mark)
                mark += 1
                r_count += 1

                if r_count == num_r:
                    leftoff = i
                    break

    g_init = text.index('G')
    
    for i in range(g_init, len(text)):
        if text[i] == 'G':
            text = swap(text, i, mark)
            mark += 1

    return text

# very simple and lazy solution that happened to work in this case, but has 
# time complexity of O(nlogn)
def rgb_sort_lazy(text):

    text.sort(reverse=True)

    return text

def swap(array, index1, index2):

    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

    return array

test1 = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
test2 = ['G', 'B', 'R', 'R', 'G', 'R', 'B']
test3 = ['B', 'R', 'G', 'G', 'B', 'R', 'G']

print(rgb_sort(test1))
print(rgb_sort(test2))
print(rgb_sort(test3))