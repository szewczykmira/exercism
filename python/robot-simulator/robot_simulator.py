NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)

BEARINGS = [NORTH, EAST, SOUTH, WEST]

class Robot:
    STEPS = {
        'L': 'turn_left',
        'R': 'turn_right',
        'A': 'advance'}

    def __init__(self, face=NORTH, lat=0, lon=0):
        self.coordinates = (lat, lon)
        self.bearing = face

    def change_bearing(self, clock):
        one = 1 if clock else -1
        old_index = BEARINGS.index(self.bearing)
        self.bearing = BEARINGS[(old_index + one) % 4]

    def turn_right(self):
        self.change_bearing(True)

    def turn_left(self):
        self.change_bearing(False)

    def advance(self):
        zipped = zip(self.coordinates, self.bearing)
        self.coordinates = tuple(map(lambda x: sum(x), zipped))

    def simulate(self, steps):
        for step in steps:
            action = getattr(self, self.STEPS[step])
            action()

