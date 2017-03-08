from calendar import Calendar, day_name
from datetime import date, timedelta

MeetupException = Exception


class Meetup:
    def __init__(self, year, month, week_day):
        self.calendar = Calendar()
        self.week_day = week_day
        self.month_to_list = self.calendar.monthdayscalendar(year, month)

    @property
    def get_all_week_days(self):
        index = list(day_name).index(self.week_day)
        
        all_week = [l[index] for l in self.month_to_list]
        return list(filter(lambda x: x > 0, all_week))

    def get_nth(self, counter):
        week_days = self.get_all_week_days
        try:
            return week_days[counter-1]
        except IndexError:
            raise MeetupException

    def get_teenth(self):
        return next(filter(lambda x: x >= 10, self.get_all_week_days))


def handle_meetup(year, month, week_day, counter):
    meetup = Meetup(year, month, week_day)

    if counter == 'last':
        return meetup.get_nth(0)

    if counter == 'teenth':
        return meetup.get_teenth()

    return meetup.get_nth(int(counter[0]))

def meetup_day(year, month, week_day, counter):
    day = handle_meetup(year, month, week_day, counter)
    return date(year, month, day)


