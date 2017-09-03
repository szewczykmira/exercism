def diagonal_to(elem):
    elem_row, elem_col = elem
    result = []
    for i in range(8):
        diff = i - elem_row
        col_1 = elem_col + diff
        col_2 = elem_col - diff
        if col_1 in range(0, 8):
            result.append((i, col_1))
        if col_2 in range(0, 8):
            result.append((i, col_2))
    return result


def check_board(white, black):
    if white == black or 8 in white or 8 in black:
        raise ValueError


def board(white, black):
    check_board(white, black)
   
    result = []
    for row in range(8):
        row_el = ''
        for column in range(8):
            if (row, column) == white:
                row_el += 'W'
            elif (row, column) == black:
                row_el += 'B'
            else:
                row_el += '_'
        result.append(row_el)
    return result


def can_attack(white, black):
    check_board(white, black)
    row = white[0] == black[0]
    column = white[1] == black[1]
    diagonal = black in diagonal_to(white)
    return row or column or diagonal
