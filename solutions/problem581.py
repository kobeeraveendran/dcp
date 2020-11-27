def rectangle_intersection(r1, r2):

    r1_topleft, r1_dims = r1
    r2_topleft, r2_dims = r2

    r1_botright = (r1_topleft[0] + r1_dims[0], r1_topleft[1] - r1_dims[1])
    r2_botright = (r2_topleft[0] + r2_dims[0], r2_topleft[1] - r2_dims[1])

    min_x = max(r1_topleft[0], r2_topleft[0])
    max_x = min(r1_botright[0], r2_botright[0])
    min_y = max(r1_botright[1], r2_botright[1])
    max_y = min(r1_topleft[1], r2_topleft[1])

    if max_x > min_x and max_y > min_y:
        overlap = (max_x - min_x) * (max_y - min_y)

    else:
        overlap = -1

    return overlap

if __name__ == "__main__":
    test1 = [
        ((1, 4), (3, 3)), 
        ((0, 5), (4, 3))
    ]

    tests = [test1]
    outputs = [rectangle_intersection(*test) for test in tests]

    for i, o in enumerate(outputs):
        print("Test {}: {}".format(i + 1, o))