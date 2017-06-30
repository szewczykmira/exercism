
def encode(text, rails):
    up = False
    text = text.replace(" ", "")
    fence = [list() for _ in range(0, rails)]
    rails -= 1
    layer = 0
    for character in text:
        fence[layer] += character
        if layer == rails:
            up = True
        if layer == 0:
            up = False
        layer = layer - 1 if up else layer + 1
    return ''.join([''.join(rail) for rail in fence])
    



def decode(text, rails):
    raise Exception
