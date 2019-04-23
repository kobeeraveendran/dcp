def compute_itinerary(flight_list, start):

    itinerary = [start]
    origins = {}

    # mapping of origins to destinations
    for flight in flight_list:
        if flight[0] in origins:
            origins[flight[0]].append(flight[1])

        else:
            origins[flight[0]] = [flight[1]]

    # lexicographically sort any keys with multiple values by value
    for key in origins.keys():
        if len(origins[key]) > 1:
            origins[key].sort()

    # DEBUG: printing origins dict
    '''
    for key in origins.keys():
        print(key + ': ', end = '')
        
        for i in range(len(origins[key])):
            print(origins[key][i], end = ' ')
        print('\n')
    '''

    # generate itinerary
    if start not in origins:
        return None
    else:
        itinerary.append(origins[start][0])
    origins[start].remove(origins[start][0])

    for _ in range(len(flight_list) - 1):
        try:
            itinerary.append(origins[itinerary[-1]][0])
            origins[itinerary[-2]].remove(origins[itinerary[-2]][0])
        except:
            # this should only happen if the destination of one 
            # origin isn't itself an origin
            return None
    
    return itinerary

test1 = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
test2 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
test3 = [('SFO', 'COM'), ('COM', 'YYZ')]

print(compute_itinerary(test1, 'YUL'))      # expected out: ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
print(compute_itinerary(test2, 'A'))        # expected out: ['A', 'B', 'C', 'A', 'C']
print(compute_itinerary(test3, 'COM'))      # expected out: None