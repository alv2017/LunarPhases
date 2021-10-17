import datetime

KNOWN_NEW_MOON = datetime.date(year=2000, month=1, day=6)
LUNAR_PHASE_PERIOD = 29.53

LUNAR_PHASES = ('New Moon',
                'Waxing Crescent',
                'First Quarter',
                'Waxing Gibbous',
                'Full Moon',
                'Waning Gibbous',
                'Last Quarter',
                'Waxing Crescent'
                )


def get_julian_days(dt: datetime.date) -> float:
    """
    Caclulates Julian day.
    Julian day is the continuous count of days since the beginning of the Julian period
    :param dt: date
    :return: float: Julian day
    """
    year = dt.year
    month = dt.month
    day = dt.day

    if month < 3:
        year = year - 1
        month = month + 12

    a = int(year/100)
    b = int(a/4)
    c = 2 - a + b
    e = int(365.25 * (year + 4716))
    f = int(30.6001 * (month + 1))

    return c + day + e + f - 1524.5


def get_lunar_phase(dt: datetime.date) -> (str, int):
    """
    The function takes date as an input and returns a tuple containing a moon phase and an age of Moon in days.
    :param dt: date
    :return: (str, int): tuple containing moon phase and moon age in days
    """
    if dt < KNOWN_NEW_MOON:
        raise ValueError(f"The lunar phase date must be greater than {KNOWN_NEW_MOON}")

    # convert KNOWN_NEW_MOON to Julian Days
    knm_jd = get_julian_days(KNOWN_NEW_MOON)

    # convert dt to Julian Days
    dt_jd = get_julian_days(dt)

    # days since new moon
    days_since_new = dt_jd - knm_jd

    # new moons
    new_moons = days_since_new / LUNAR_PHASE_PERIOD

    # lunar phase
    passed_cycles = int(new_moons)
    phase_index = int((new_moons - passed_cycles) * 8)
    moon_age = int((new_moons - passed_cycles) * LUNAR_PHASE_PERIOD)
    moon_phase = LUNAR_PHASES[phase_index]

    return moon_phase, moon_age
