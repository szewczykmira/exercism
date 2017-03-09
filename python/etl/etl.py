def transform(old_dict):
    new_dict = {}
    for key, values in old_dict.items():
        for value in values:
            new_dict.update({value.lower(): key})
    return new_dict

