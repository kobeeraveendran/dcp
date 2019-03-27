import random

def estimate_pi():
    in_circle = []
    out_circle = []

    for i in range(10000000):
        x = random.random()
        y = random.random()

        if pow(x, 2) + pow(y, 2) <= 1:
            in_circle.append(1)

        else:
            out_circle.append(1)

    num_in = len(in_circle)
    num_out = len(out_circle)

    pi = num_in / (num_in + num_out) * 4

    return pi


print("pi approximation: ", estimate_pi())