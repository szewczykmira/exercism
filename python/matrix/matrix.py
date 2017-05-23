class Matrix(object):
    def __init__(self, matrix):
        self.data = matrix
        self.rows = self.generate_rows()
        self.columns = self.generate_columns()

    def generate_rows(self):
        rows = self.data.split('\n')
        return [self.handle_row(row) for row in rows]

    def handle_row(self, row):
        row = row.split(' ')
        return [int(r) for r in row]

    def generate_columns(self):
        columns = []
        for i in range(0, len(self.rows)-1):
            column = [row[i] for row in self.rows]
            columns.append(column)
        return columns

