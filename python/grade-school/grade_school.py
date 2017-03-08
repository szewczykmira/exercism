class School:

    def __init__(self, name):
        self.name = name
        self.GRADES = {}

    def grade(self, grade):
        return sorted(self.GRADES.get(grade, []))

    def add(self, name, grade):
        if grade not in self.GRADES:
            self.GRADES[grade] = []
        self.GRADES[grade].append(name)

    def sort(self):
        sorted_keys = sorted(self.GRADES.keys())
        return [(key, tuple(self.grade(key))) for key in sorted_keys]

