import numpy as np

def game_of_life(start, num_runs):

    live_cells = start

    grid = [['.' for i in range(10)] for i in range(10)]
    grid = np.asarray(grid)

    for coord in live_cells:
        #print('({}, {})'.format(coord[0], coord[1]))
        grid[coord[0]][coord[1]] = '*'

    min_x, min_y, max_x, max_y = find_cutoffs(live_cells)

    print_board(grid[min_x - 1:max_x - 1, min_y - 1:max_y - 1])

def print_board(grid):

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[j][i], end = ' ')
        
        print()

def find_cutoffs(coords):
    min_x = min([x[0] for x in coords])
    min_y = min([y[1] for y in coords])
    max_x = max([x[0] for x in coords])
    max_y = max([y[1] for y in coords])

    return min_x, min_y, max_x, max_y

init = [(3, 5), (4, 2), (1, 6), (5, 9)]
game_of_life(init, 2)
