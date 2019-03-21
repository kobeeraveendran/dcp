# only works for messages of length 4-5 or less
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
        if int(sub_str) > 26 or sub_str[0] == '0':
            num_ways -= 1

    return num_ways

def num_ways(message):
    if len(message) <= 1:
        return 1

    if len(message) >= 2:

        return num_ways(message[1:]) + num_ways(message[2:]) if int(message[0:2]) in range(1, 27) else num_ways(message[1:])

test1 = '111'       # aaa, ak, ka  --> 3
test2 = '1111'      # kk, aka, kaa, aak, aaaa --> 5
test3 = '271'       # bga --> 1
test4 = '101'       # ja --> 1
test5 = '10001'     # unsure; may be either 0 (in which case, not a valid input) or 1 at most (ja)
test6 = '121121'    # abaaba, laaba, lku, lkba, laau, abaau, abku, auau, lala, abkba, aula,  --> 

print(num_ways_decoded(test1))
print(num_ways_decoded(test2))
print(num_ways_decoded(test3))
print(num_ways_decoded(test4))
print(num_ways_decoded(test5))
print(num_ways_decoded(test6))

print('\n\n')

print(num_ways(test1))
print(num_ways(test2))
print(num_ways(test3))
print(num_ways(test4))
print(num_ways(test5))
print(num_ways(test6))