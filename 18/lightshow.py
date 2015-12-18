"""
--- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.
The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?
"""


def get_initial_grid():
    lights = []
    with open('./testinput.txt') as fi:
        for line in fi.readlines():
            light_row = []
            for light in list(line):
                if light == '.':
                    light_row.append(0)
                elif light == '#':
                    light_row.append(1)
            lights.append(light_row)

    return lights


def count_neighbors_that_are_on(grid, starting_row, starting_col):
    # check around it, and turn it off or leave it on according to our rules
    neighbors_on = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            try:
                if any([starting_row + k == 0 and starting_col + l == 0,
                        starting_row + k == 0 and starting_col + l == len(grid[starting_row]) - 1,
                        starting_row + k == len(grid) - 1 and starting_col + l == 0,
                        starting_row + k == len(grid) - 1 and starting_col + l == len(grid[starting_row]) - 1
                        ]):
                    neighbors_on += 1
                elif not any([starting_row + k < 0,
                              starting_col + l < 0,
                              starting_row + k > len(grid),
                              starting_col + l > len(grid[starting_row]),
                              k == 0 and l == 0
                              ]):
                    # print grid[starting_row + k][starting_col + l]
                    neighbors_on += grid[starting_row + k][starting_col + l]
            except IndexError:
                pass

    # print '[%s][%s]' % (starting_row, starting_col), 'has %s neighbors on' % neighbors_on
    return neighbors_on


def compute_step(grid):
    next_step = []
    for i in range(len(grid)):
        next_step.append([])
        for j in range(len(grid[i])):
            is_on = grid[i][j] == 1
            # print i, j, 'is on:', is_on
            neighbors_on = count_neighbors_that_are_on(grid, i, j)
            if any([i == 0 and j == 0,
                    i == 0 and j == len(grid) - 1,
                    i == len(grid) - 1 and j == 0,
                    i == len(grid) - 1 and j == len(grid[i]) - 1
                    ]):
                next_step[i].append(1)
            else:
                if is_on:
                    # print '  it should stay on:', any([neighbors_on == 2, neighbors_on == 3])
                    next_step[i].append(0 if not any([neighbors_on == 2, neighbors_on == 3]) else 1)
                else:
                    # print '  it should stay off:', neighbors_on != 3
                    next_step[i].append(1 if neighbors_on == 3 else 0)

    return next_step


def print_grid(grid):
    for line in grid:
        print line


def sum_grid(grid):
    return sum([sum(line) for line in grid])


def iterate_grid(the_grid, iterations):
    for i in range(iterations):
        the_grid = compute_step(the_grid)
    print sum_grid(the_grid)


the_grid = get_initial_grid()
iterate_grid(the_grid, 100)
