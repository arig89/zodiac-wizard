"""Tests for my functions.
"""

from my_module.functions import zodiac_function, zodiac_horoscope, zodiac_compatibility


#Tests to make sure proper zodiac sign assigned.
def test_zodiac_function():
    test_month = 9
    test_day = 11
    assert zodiac_function(test_month, test_day) == "Virgo"

def test_zodiac_compatibility():
    test_user = "Virgo"
    test_friend = "Aries"
    assert zodiac_compatibility(test_user, test_friend) == "You get along quite well!"


def test_zodiac_horoscope():
    test_sign = "Gemini"
    assert zodiac_horoscope(test_sign) == "you will run into an old friend."

