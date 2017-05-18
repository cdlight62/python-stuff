
count = 0
bricks = 200

stairs = {1:1, 2:1, 3:1, 4:1}

def get_stairs(n, max = bricks-1):
    global count
    j = n-1 if n <= max else max
    i = n - j
    stair_count = 0
    if n == 16:
        b = True
    while j >= round(math.sqrt(n*2)):
        if i < j and j <= max:
            count += 1
            stair_count += 1
        if i > 2:
            if i in stairs:
                if i <= j:
                    count += stairs[i]
                    stair_count += stairs[i]
                # elif i == j+1:
                #     min = int(round(math.sqrt(n*2)))+1
                #     diff = j - min
                #     for k in xrange(0, diff+1):
                #         count += stairs[i-1] - k
                #         stair_count += stairs[i - 1] - k
                # elif i == j + 2:
                #     # count += stairs[i - 1]
                #     # stair_count += stairs[i - 1]
                #     min = int(round(math.sqrt(n*2)))+1
                #     diff = j - min
                #     for k in xrange(1, diff+1):
                #         count += stairs[i - 1] - k
                #         stair_count += stairs[i - 1] - k
                elif j == round(math.sqrt(n * 2)):
                    stair_count += get_stairs(i, j-1)
                else:
                    tempj = j-1
                    tempi = i - tempj
                    if tempj > tempi:
                        tempcount = stairs[tempi] + stairs[tempj]
                    else:
                        tempcount = stairs[tempi] + stairs[tempj] - 1
                    count += tempcount
                    stair_count += tempcount
            else:
                stair_count += get_stairs(i, j-1)
        i += 1
        j -= 1
    if not n in stairs:
        stairs[n] = stair_count
    print(stairs)
    return stair_count

import math
get_stairs(bricks)

print(count)