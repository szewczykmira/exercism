from decimal import Decimal

class SpaceAge:
    EARTH_YEAR = 31557600
    MERCURY_YEAR = 0.2408467
    VENUS_YEAR = 0.61519726
    MARS_YEAR = 1.8808158
    JUPITER_YEAR = 11.862615
    SATURN_YEAR = 29.447498
    URANUS_YEAR = 84.016846
    NEPTUN_YEAR = 164.79132

    def __init__(self, age):
        self.seconds = age

    def on_earth(self):
        return self.age_with_multiplier(1)

    def on_mercury(self):
        return self.age_with_multiplier(self.MERCURY_YEAR)

    def on_venus(self):
        return self.age_with_multiplier(self.VENUS_YEAR)

    def on_mars(self):
        return self.age_with_multiplier(self.MARS_YEAR)

    def on_jupiter(self):
        return self.age_with_multiplier(self.JUPITER_YEAR)

    def on_saturn(self):
        return self.age_with_multiplier(self.SATURN_YEAR)

    def on_uranus(self):
        return self.age_with_multiplier(self.URANUS_YEAR)

    def on_neptune(self):
        return self.age_with_multiplier(self.NEPTUN_YEAR)

    def age_with_multiplier(self, mul):
        return round(self.seconds / (self.EARTH_YEAR * mul), 2)

