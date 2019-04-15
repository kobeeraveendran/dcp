def running_median(sequence):

    temp_list = []
    l = 0

    for i in range(len(sequence)):
        temp_list.append(sequence[i])
        temp_list.sort()
        l += 1

        if l % 2 == 0:
            print((temp_list[l // 2] + temp_list[l // 2 - 1]) / 2)

        else:
            print(temp_list[l // 2])

test1 = [2, 1, 5, 7, 2, 0, 5]

running_median(test1) # expected out: 2, 1.5, 2, 3.5, 2, 2, 2