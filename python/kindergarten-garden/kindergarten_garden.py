CHILDREN = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
            'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

class Garden:
    PLANTS = {
            'G': 'Grass',
            'C': 'Clover',
            'R': 'Radishes',
            'V': 'Violets',
    }

    def __init__(self, plants, students=CHILDREN):
        self.rows = plants.split('\n') 
        self.STUDENTS = sorted(students)
    

    def plants(self, name):
        index = self.STUDENTS.index(name) * 2
        plants_signs = ''.join([r[index: index + 2] for r in self.rows])
        return list(map(lambda x: self.PLANTS[x], plants_signs))

