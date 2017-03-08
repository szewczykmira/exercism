def multipliers_lt(max_num, elem):
    try:
        times = int(max_num // elem)
    except ZeroDivisionError:
        times = 0
    return {elem * i for i in range(1, times+1)}

def sum_of_multiples(max_num, elements):
    sets = [multipliers_lt(max_num - 1, elem) for elem in elements]
    multi_union = sets[0].union(*sets[1:])
    return sum(multi_union)
