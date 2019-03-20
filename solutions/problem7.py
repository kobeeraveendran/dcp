def num_ways_decoded(message):
    l = len(message)
    num_ways = l if l % 2 == 0 else l - 1
    
    # split into groups of 1 or 2 characters
    # ones is just the string as-is; every message is valid in this form as long as there are no zeros
    if '0' not in message:
        num_ways += 1

    # check two's list (sliding window)
    # for a string of length n, there will be n - 1 pairs to check
    for i in range(l - 1):
        sub_str = message[i : i + 2]
        if int(sub_str) > 26 or int(sub_str) < 1 or sub_str[0] == '0':
            num_ways -= 1

    return num_ways

test1 = '111'   # aaa, ak, ka  ==> 3
test2 = '1111'  # kk, aka, kaa, aak, aaaa ==> 5
test3 = '271'   # bga ==> 1

print(num_ways_decoded(test1))
print(num_ways_decoded(test2))
print(num_ways_decoded(test3))