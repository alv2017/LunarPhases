import datetime
from django.test import TestCase
from .moon_phase_calculator import get_julian_days, get_lunar_phase


class MoonPhaseCaclulatorTests(TestCase):

    def test_get_julian_days(self):
        # known test date case
        test_date = datetime.date(year=2018, month=1, day=1)
        expected_julian_days = 2458119.5
        calculated_julian_days = get_julian_days(test_date)
        self.assertAlmostEqual(expected_julian_days, calculated_julian_days)
        self.assertEqual(int(expected_julian_days), int(calculated_julian_days))

        # known test date case
        test_date = datetime.date(year=2018, month=2, day=1)
        expected_julian_days = 2458150.5
        calculated_julian_days = get_julian_days(test_date)
        self.assertAlmostEqual(expected_julian_days, calculated_julian_days)
        self.assertEqual(int(expected_julian_days), int(calculated_julian_days))

        # known test date case
        test_date = datetime.date(year=2021, month=3, day=25)
        expected_julian_days = 2459298.5
        calculated_julian_days = get_julian_days(test_date)
        self.assertAlmostEqual(expected_julian_days, calculated_julian_days)
        self.assertEqual(int(expected_julian_days), int(calculated_julian_days))

        # known test date case
        test_date = datetime.date(year=2021, month=10, day=15)
        expected_julian_days = 2459502.5
        calculated_julian_days = get_julian_days(test_date)
        self.assertAlmostEqual(expected_julian_days, calculated_julian_days)
        self.assertEqual(int(expected_julian_days), int(calculated_julian_days))


    def test_get_lunar_phase(self):
        # known test date case
        test_date = datetime.date(year=2021, month=1, day=6)
        expected_phase = 'Last Quarter'
        expected_age = 22
        calculated_phase, calculated_age = get_lunar_phase(test_date)
        self.assertEqual(expected_phase, calculated_phase)
        self.assertEqual(expected_age, calculated_age)

        # known test date case
        test_date = datetime.date(year=2021, month=1, day=13)
        expected_phase = 'New Moon'
        expected_age = 0
        calculated_phase, calculated_age = get_lunar_phase(test_date)
        self.assertEqual(expected_phase, calculated_phase)
        self.assertEqual(expected_age, calculated_age)

        # known test date case
        test_date = datetime.date(year=2021, month=1, day=21)
        expected_phase = 'First Quarter'
        expected_age = 8
        calculated_phase, calculated_age = get_lunar_phase(test_date)
        self.assertEqual(expected_phase, calculated_phase)
        self.assertEqual(expected_age, calculated_age)

        # known test date case
        test_date = datetime.date(year=2021, month=1, day=28)
        expected_phase = 'Full Moon'
        expected_age = 15
        calculated_phase, calculated_age = get_lunar_phase(test_date)
        self.assertEqual(expected_phase, calculated_phase)
        self.assertEqual(expected_age, calculated_age)




