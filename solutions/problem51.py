import random

NUM_CARDS = 52

def rng(k):
    return random.randint(0, k)

def shuffle_deck():
    cards = [x for x in range(NUM_CARDS)]

    for i in range(NUM_CARDS):
        rand_num = rng(i)

        tmp = cards[i]
        cards[i] = cards[rand_num]
        cards[rand_num] = tmp

    return cards

print(shuffle_deck())