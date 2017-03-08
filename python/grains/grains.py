def on_square(square):
    return 2 ** (square-1)

def total_after(square):
    result = 0
    for i in range(0, square):
        result = (result * 2) + 1
    return result
    
