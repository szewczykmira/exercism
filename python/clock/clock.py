from dataclasses import dataclass

@dataclass
class Clock:
    hours: int
    minutes: int

    def __post_init__(self):
        adds, self.minutes = divmod(self.minutes, 60)
        self.hours = (self.hours + adds) % 24


    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __add__(self, other) -> "Clock":
        if isinstance(other, int):
            return Clock(self.hours, self.minutes + other)

    def __sub__(self, other) -> "Clock":
        if isinstance(other, int):
            return Clock(self.hours, self.minutes - other)