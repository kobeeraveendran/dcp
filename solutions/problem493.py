import random

def generate_prob_nums(nums, probs):

    for i in range(1, len(probs)):
        probs[i] = probs[i] + probs[i - 1]

    rand = random.random()

    print(rand)

    for i in range(1, len(nums)):
        if rand >= probs[i-1] and rand < probs[i]:
            return nums[i]

    return nums[0]

test = (
    [1, 2, 3, 4], 
    [0.1, 0.5, 0.2, 0.2]
)

print(generate_prob_nums(*test))