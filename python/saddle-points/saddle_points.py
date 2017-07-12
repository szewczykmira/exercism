from functools import reduce

class Matrix:
    def __init__(self, matrix):
        self.clean = matrix
        self.test_data()
        self.enum = self.enum_matrix()

    def test_data(self):
        lens = [len(x) for x in self.clean]
        if lens and not len(set(lens)) == 1:
            raise ValueError

    def enum_matrix(self):
        new_matrix = []
        for num, row in enumerate(self.clean):
            new_row = [MatrixPoint((num, num_el), elem)
                    for num_el, elem in enumerate(row)]
            new_matrix.append(new_row)
        return new_matrix

    def gte_from_list(self, data):
        result = reduce(lambda x, y: x if x >= y else y, data)
        if result:
            result = list(filter(lambda x: x.value == result.value, data))
        return result

    def lte_form_list(self, data):
        result = reduce(lambda x, y: x if x <= y else y, data)
        if result:
            result = list(filter(lambda x: x.value == result.value, data))
        return result

    @property
    def rows(self):
        return self.enum

    @property
    def columns(self):
        matrix_len = len(self.enum)
        result = []
        for i in range(0, matrix_len):
            curr_col = []
            for row in self.enum:
                curr_col.append(row[i])
            result.append(curr_col)
        return result

    def saddle_points(self):
        gte = []
        for row in self.rows:
            gte.extend(self.gte_from_list(row))
        lte = []
        for column in self.columns:
            lte.extend(self.lte_form_list(column))
        return {val.coord for val in gte if val in lte}

class MatrixPoint:
    def __init__(self, coord, value):
        self.coord = coord
        self.value = value

    def __str__(self):
        return ' '.join([str(self.coord), str(self.value)])

    def __repr__(self):
        return '<%s - %d>' % (str(self.coord), self.value)

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.coord == other.coord and self.value == other.value


def saddle_points(matrix):
    matrix = Matrix(matrix)
    return matrix.saddle_points()
