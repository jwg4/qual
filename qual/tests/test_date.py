import unittest

from datetime import date

from qual.calendars import DateWithCalendar

class TestDateWtihCalendar(unittest.TestCase):
    def setUp(self):
        date_dt = date(2010, 8, 1)
        self.date_wc = DateWithCalendar(None, date_dt)

    def test_comparisons(self): 
        self.assertTrue(self.date_wc < date(2010, 8, 2))
        self.assertFalse(self.date_wc < date(2010, 7, 31))
        self.assertTrue(self.date_wc > date(2010, 7, 2))
        self.assertFalse(self.date_wc > date(2010, 8, 31))
        
