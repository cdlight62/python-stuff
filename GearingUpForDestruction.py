def answer(pegs):
    def place_gears():
        gears = [(pegs[1] - pegs[0]) / 2.0, (pegs[1] - pegs[0]) / 2.0]
        for i in range(2, len(pegs)):
            gears.append(pegs[i] - pegs[i - 1] - gears[i - 1])
        return gears

    def check_gears(gear):
        gear_list = [gear]
        for i in range(1, len(pegs)):
            gear_list.append(pegs[i] - pegs[i - 1] - gear_list[i - 1])
        for g in gear_list:
            if g < 1:
                return False
        return True

    gears = place_gears()
    if len(pegs) == 2:
        sum = gears[0] + gears[-1]
        if sum % 3 == 0:
            last_gear = [sum / 3.0, 1]
            first_gear = [last_gear[0] * 2, 1]
        else:
            last_gear = [sum, 3]
            first_gear = [sum * 2, 3]
        return first_gear
    elif gears.count(0) > 0:
        return [-1, -1]
    elif len(pegs) % 2 != 0:
        if gears[-1] >= gears[0]:
            return [-1, -1]
        diff = gears[0] - gears[-1]
        first_gear = diff * 2
        if gears[0] - first_gear == gears[-1] - diff:
            return list(float(first_gear).as_integer_ratio())
        else:
            return [-1, -1]
    else:
        sum = gears[0] + gears[-1]
        if sum < 3:
            return [-1, -1]
        if sum % 3 == 0:
            last_gear = [sum / 3.0, 1]
            first_gear = [last_gear[0] * 2, 1]
        else:
            last_gear = [sum, 3]
            first_gear = [sum * 2, 3]
        if check_gears(first_gear[0]/first_gear[1]):
            if (first_gear[0]) - (gears[0] * first_gear[1]) == (gears[-1] * first_gear[1]) - (last_gear[0]):
                return first_gear
        else:
            return [-1, -1]


print(answer([4, 30, 31, 58]))
