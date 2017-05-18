import math

check = [1,2,3,4,5,6,7,8,9]
block_coords = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]

game1 = [[1,2,3,4,5,6,7,8,9],
        [4,0,6,7,8,9,1,2,3],
        [7,8,9,1,2,3,4,5,6],
        [2,3,1,5,6,4,8,9,7],
        [5,6,4,8,9,7,2,3,1],
        [8,9,7,2,3,1,5,6,4],
        [3,1,2,6,4,5,9,7,8],
        [6,4,5,9,7,8,3,1,2],
        [9,7,8,3,1,2,6,4,5]]

game2 = [[0,2,0,4,5,6,7,8,9],
        [4,5,7,0,8,0,2,3,6],
        [6,8,9,2,3,7,0,4,0],
        [0,0,5,3,6,2,9,7,4],
        [2,7,4,0,9,0,6,5,3],
        [3,9,6,5,7,4,8,0,0],
        [0,4,0,6,1,8,3,9,7],
        [7,6,1,0,4,0,5,2,8],
        [9,3,8,7,2,5,0,6,0]]

game = [[6,0,0,0,2,0,0,0,9],
        [0,1,0,3,0,7,0,5,0],
        [0,0,3,0,0,0,1,0,0],
        [0,9,0,0,0,0,0,2,0],
        [2,0,0,8,7,5,0,0,3],
        [0,0,5,0,1,0,4,0,0],
        [0,7,0,0,8,0,0,9,0],
        [0,0,1,0,4,0,8,0,0],
        [0,0,0,2,5,9,0,0,0]]


def get_block(x_coord, y_coord):
    block = []
    for y in range(3):
        block.extend([game[y + (math.floor(x_coord / 3) * 3)][z + (math.floor(y_coord / 3) * 3)] for z in range(3)])
    return block


def get_column(y_coord):
    return [game[x][y_coord] for x in range(9)]


def check_solution():
    for x in range(9):
        if sorted(game[x]) != check:
            return False
        if sorted([game[y][x] for y in range(9)]) != check:
            return False
        block = get_block(math.floor(x / 3) * 3, math.floor(x % 3) * 3)
        if sorted(block) != check:
            return False
    return True


def get_options(x, y):
    row = game[x]
    column = get_column(y)
    block = get_block(x, y)
    nums = list(set(row).union(set(column), set(block)))
    options = list(set(check).difference(nums))
    return options


def check_uniques(options):
    uniques = []
    options_flat = [x for y in options for x in y]
    for i in options_flat:
        if options_flat.count(i) == 1:
            uniques.append(i)
    # print(options)
    # print(uniques)
    for x in range(len(uniques)):
        index = next(((i) for i, y in enumerate(options) if uniques[x] in y))
        game[x][index] = uniques[x]
        # print(index)


if __name__ == "__main__":
    game_flat = [x for row in game for x in row]
    while not check_solution():
        # for row in range(9):
        #     options = []
        #     for elem in range(9):
        #         if game[row][elem] == 0:
        #             options.append(get_options(row, elem))
        #         else:
        #             options.append([])
        #     #(*options, sep='\n')
        #     check_uniques(options)
        for column in range(9):
            options = []
            for elem in range(9):
                if game[elem][column] == 0:
                    options.append(get_options(column, elem))
                else:
                    options.append([])
            print(*options, sep='\n')
            check_uniques(options)
        #print(*game, sep="\n")
#block = get_block(block_coords[x][0], block_coords[x][1])
#pos = (math.floor(x/3)*26 + (x%3)*3)+(math.floor(y/3)*9)+(math.floor(x/3)+(y%3))

        # holes = [(i, j)for i, row in enumerate(game) for j, num in enumerate(row) if num == 0]