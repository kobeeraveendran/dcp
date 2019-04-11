def well_formed(string):
    frequencies = {}

    for char in string:
        if char in frequencies:
            frequencies[char] += 1

        else:
            frequencies[char] = 1

    for key in frequencies.keys():
        if key == '[':
            if ']' not in frequencies or frequencies[']'] != frequencies[key]:
                return False

        if key == '{':
            if '}' not in frequencies or frequencies['}'] != frequencies[key]:
                return False
        
        if key == '(':
            if ')' not in frequencies or frequencies[')'] != frequencies[key]:
                return False

    return True

test1 = "([])[]({})"
test2 = "([)]"
test3 = "((()"

print(well_formed(test1))       # expected out: True
print(well_formed(test2))       # expected out: False
print(well_formed(test3))       # expected out: False