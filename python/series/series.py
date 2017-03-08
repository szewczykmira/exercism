def slices(digit_string, num):
    len_digit = len(digit_string)
    result = []
    if len_digit < num or num == 0:
        raise ValueError
    for i in range(0, len_digit):
        partial = [int(dig) for dig in digit_string[i:(i+num)]]
        if len(partial) < num:
            return result
        result.append(partial)
    return result
