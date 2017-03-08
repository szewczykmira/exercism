from datetime import datetime, timedelta
from math import pow

GIGASECONDS = pow(10, 9)

def add_gigasecond(date):
    return date + timedelta(seconds=GIGASECONDS)

