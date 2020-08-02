def int_palindrome(integer):

    digits = []

    while integer // 10:
        digits.append(integer % 10)
        integer = integer // 10

    digits.append(integer)
    
    return digits == digits[::-1]

tests = [121, 888, 678, 77]

for i, test in enumerate(tests):
    print("Test {}:".format(i+1), end = '')
    print(int_palindrome(test))