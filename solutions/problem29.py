def run_length_encoding(text):

    count = 0
    encoded_string = ''
    curr = ''
    l = len(text)

    for i in range(l):
        if text[i] != curr:
            encoded_string += str(count) + curr if count != 0 else ''
            count = 1
            curr =  text[i]

        else:
            count += 1

    encoded_string += str(count) + curr

    return encoded_string

def run_length_decoding(text):

    decoded_string = ''

    for i in range(len(text) // 2):
        decoded_string += text[i * 2 + 1] * int(text[i * 2])

    return decoded_string


test1_encode = 'AAAABBBCCDAA'
test1_decode = '4A3B2C1D2A'

print(run_length_encoding(test1_encode))
print(run_length_decoding(test1_decode))