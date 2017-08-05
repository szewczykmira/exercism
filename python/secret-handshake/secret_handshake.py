SECRET = ['wink', 'double blink', 'close your eyes', 'jump']

def check_data(n):
    if isinstance(n, int):
        binary = bin(n)[2:]
    else:
        binary = n
        n = int(n, 2)

    if n < 0:
        raise ValueError
    return binary


def handshake(n):
    result = []
    try:
        binary = check_data(n)
    except ValueError:
        return result

    for enum, data in enumerate(binary[::-1]):
        if int(data):
            if enum == 4:
                result = result[::-1]
            else:
                result.append(SECRET[enum])
    return result


def code(codes):
    result = ['0'] * 4
    to_secret = []
    for text in codes:
        if text not in SECRET:
            return '0'
        index = SECRET.index(text)
        to_secret.append(index)
        result[index] = '1'

    if not to_secret == sorted(to_secret):
        result.append('1')

    return ''.join(result[::-1]).lstrip('0')


