def longest_substring(string, k):

    seen = set()

    window_start = 0

    max_len = 0

    for i in range(len(string)):
        seen.add(string[i])

        if len(seen) > k:
            if string[window_start] in seen:
                seen.remove(string[window_start])
                max_len = max(i - window_start, max_len)
            window_start += 1

    return max(max_len, 1)

test1 = 'abcba'
test2 = 'abbbbbcddda'
test3 = 'abbbbbdddca'
test4 = 'abbbbbccddda'

print(longest_substring(test1, 2))  # expected out: 3
print(longest_substring(test2, 2))  # expected out: 6
print(longest_substring(test3, 2))  # expected out: 7
