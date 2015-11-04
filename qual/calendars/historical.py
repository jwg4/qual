from datetime import date

from base import Calendar
from date import InvalidDate, DateWithCalendar
from main import JulianCalendar, ProlepticGregorianCalendar

class SwitchDateWithCalendar(DateWithCalendar):
    def __str__(self):
        return "%s (%s - %s)" % (
            self.calendar.date_display_string(self._date),
            self.calendar.display_name,
            self.calendar.period_string(self._date)
        )

class JulianToGregorianCalendar(Calendar):
    def date(self, year, month, day):
        gregorian_date = date(year, month, day)
        if gregorian_date < self.first_gregorian_day:
            julian_date = JulianCalendar().date(year, month, day)
            if not julian_date < self.first_gregorian_day:
                raise InvalidDate("This is a 'missing day' when the calendars changed.")
            return self.from_date(julian_date._date)
        return self.from_date(gregorian_date)

    @classmethod
    def date_display_string(cls, d):
        if d >= cls.first_gregorian_day:
            return ProlepticGregorianCalendar.date_display_string(d)
        return JulianCalendar.date_display_string(d)

    @classmethod
    def period_string(cls, d):
        if d >= cls.first_gregorian_day:
            return 'Gregorian'
        else:
            return 'Julian'

    def bless(self, d):
        d.calendar = self.__class__

    def from_date(self, d):
        return SwitchDateWithCalendar(self.__class__, d)

class EnglishHistoricalCalendar(JulianToGregorianCalendar):
    display_name = "English Historical Calendar"
    first_gregorian_day = date(1752, 9, 14)

class SpanishHistoricalCalendar(JulianToGregorianCalendar):
    display_name = "Spanish Historical Calendar"
    first_gregorian_day = date(1582, 10, 15)

class FrenchHistoricalCalendar(JulianToGregorianCalendar):
    display_name = "French Historical Calendar"
    first_gregorian_day = date(1582, 12, 20)

