def splice_text(s: str, k: int):
    split = s.split()
    retval = []
    tmp_string = ''
    remaining = k

    for i in range(len(split)):
        if len(split[i]) <= remaining:
            tmp_string += split[i]
            remaining -= len(split[i])
            
        if i == 0:
            tmp_string += split[i]