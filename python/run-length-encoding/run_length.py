from itertools import groupby


def encode(element):
    str_result = ''
    for key, value in groupby(element):
        times = sum(1 for _ in value)
        str_times = str(times) if times > 1 else ''
        str_result += str_times + key
    return str_result


def decode(element):
    result = ''
    times = ''
    for c in element:
        if c.isdigit():
            times += c
        else:
            if not times:
                result += c
            else:
                result += (int(times) * c)
                times = ''
    return result
