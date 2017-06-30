from itertools import chain

def fence_walk(length, rails):
    up = False
    fence = [list() for _ in range(0, rails)]
    rails -= 1
    layer = 0
    for num in range(0, length):
        fence[layer].append(num)
        if layer == rails:
            up = True
        if layer == 0:
            up = False
        layer = layer - 1 if up else layer + 1
    return chain.from_iterable(fence)

def encode(text, rails):
    text = text.replace(" ", "")
    fence = fence_walk(len(text), rails)
    text_dict = dict(enumerate(text))
    return ''.join([text_dict[num] for num in fence])
    

def decode(text, rails):
    fence = fence_walk(len(text), rails)
    text_zip = sorted(zip(fence, text), key=lambda x: x[0])
    return ''.join([x[1] for x in text_zip])

