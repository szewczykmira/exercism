def flatten(array):
    result = []
    for item in array:
        if item or item == 0:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
    return result
