def room_scheduler(time_intervals):

    all_times = set()
    num_rooms = 0

    for lecture in time_intervals:
        if lecture[0] in all_times or lecture[1] in all_times:
            num_rooms += 1

        all_times.update(range(lecture[0], lecture[1] + 1))            

    return num_rooms

test1 = [(30, 75), (0, 50), (60, 150)]
test2 = [(0, 10), (5, 10), (3, 4)]
test3 = [(0, 10), (5, 10), (3, 4), (3, 10)]
test4 = [(0, 10), (5, 10), (3, 4), (3, 10), (11, 12)]
test5 = [(0, 10), (5, 10), (3, 4), (3, 10), (3, 4)]


print(room_scheduler(test1))            # expected output: 2
print(room_scheduler(test2))            # expected output: 2
print(room_scheduler(test3))            # expected output: 3
print(room_scheduler(test4))            # expected output: 3
print(room_scheduler(test5))            # expected output: 4