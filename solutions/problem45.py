import random

def rand5():
    return random.randint(1, 5)

def rand7():
    choice = random.random()

    print(choice)

    if choice < 5/7:
        return rand5()

    else:
        return random.randint(6, 7)

print(rand7())
print(rand7())