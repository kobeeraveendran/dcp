def autocomplete(query, all_strings):

    retval = []
    prefix_len = len(query)

    for string in all_strings:
        if len(string) < prefix_len:
            continue

        if string[0:prefix_len] == query:
            retval.append(string)

    return retval

test1 = ('de', ['dog', 'deer', 'deal'])
test2 = ('def', ['defeat', 'define', 'def', 'dep', 'de', 'd'])

print(autocomplete(test1[0], test1[1]))
print(autocomplete(test2[0], test2[1]))