def justify(text, k):

    justified = []
    temp = ''
    remaining = k

    for word in text:
        if len(word) < remaining:
            temp.join(word + ' ')
            remaining -= len(word) + 1

        elif len(word) == remaining:
            temp.join(word)
            remaining = k
            justified.append(temp)
            temp = ''

def pad_line(line):
    l = len(line)

