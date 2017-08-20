BORDERS = ['+', '-', '|']
MINE = '*'
ALLOWED = BORDERS + [MINE] + [' ']


def validate_board(data):
    if not len({len(row) for row in data}) == 1:
        raise ValueError


def validate_row(row):
    if row[0] not in BORDERS or row[-1] not in BORDERS:
        raise ValueError


def validate_cell(cell):
    if cell not in ALLOWED and not cell.isdigit():
        raise ValueError


def increase(elem):
    if elem in BORDERS or elem in MINE:
        return elem
    try:
        to_int = int(elem)
        return str(to_int+1)
    except ValueError:
        return '1'


def get_neighbours(i, j):
    return [(i, j-1), (i, j+1), 
            (i-1, j-1), (i-1, j), (i-1, j+1), 
            (i+1, j-1), (i+1, j), (i+1, j+1)]
    

def board(input_board):
    validate_board(input_board)

    input_board = [list(row) for row in input_board]
    
    for row_n, row in enumerate(input_board):
    
        validate_row(row)
        
        for cell_n, cell in enumerate(row):
            validate_cell(cell)
            if not cell == MINE:
                continue
            neighbours = get_neighbours(row_n, cell_n)
            for r, c in neighbours:
                input_board[r][c] = increase(input_board[r][c])
    return [''.join(row) for row in input_board]

