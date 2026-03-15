import pytest
from src import converter


# ---- Temperature Tests ----

def test_celsius_to_fahrenheit():
    assert converter.celsius_to_fahrenheit(0) == 32
    assert converter.celsius_to_fahrenheit(100) == 212
    assert converter.celsius_to_fahrenheit(-40) == -40
    assert converter.celsius_to_fahrenheit(37) == 98.6


def test_fahrenheit_to_celsius():
    assert converter.fahrenheit_to_celsius(32) == 0
    assert converter.fahrenheit_to_celsius(212) == 100
    assert converter.fahrenheit_to_celsius(-40) == -40
    assert converter.fahrenheit_to_celsius(98.6) == 37


def test_celsius_to_kelvin():
    assert converter.celsius_to_kelvin(0) == 273.15
    assert converter.celsius_to_kelvin(100) == 373.15
    assert converter.celsius_to_kelvin(-273.15) == 0


def test_celsius_to_kelvin_below_absolute_zero():
    with pytest.raises(ValueError):
        converter.celsius_to_kelvin(-300)


# ---- Distance Tests ----

def test_miles_to_kilometers():
    assert converter.miles_to_kilometers(1) == 1.61
    assert converter.miles_to_kilometers(0) == 0
    assert converter.miles_to_kilometers(5) == 8.05
    assert converter.miles_to_kilometers(100) == 160.93


def test_kilometers_to_miles():
    assert converter.kilometers_to_miles(1) == 0.62
    assert converter.kilometers_to_miles(0) == 0
    assert converter.kilometers_to_miles(10) == 6.21
    assert converter.kilometers_to_miles(160.93) == 100.0


def test_negative_distance():
    with pytest.raises(ValueError):
        converter.miles_to_kilometers(-5)
    with pytest.raises(ValueError):
        converter.kilometers_to_miles(-10)


# ---- Weight Tests ----

def test_pounds_to_kilograms():
    assert converter.pounds_to_kilograms(1) == 0.45
    assert converter.pounds_to_kilograms(0) == 0
    assert converter.pounds_to_kilograms(100) == 45.36
    assert converter.pounds_to_kilograms(220) == 99.79


def test_kilograms_to_pounds():
    assert converter.kilograms_to_pounds(1) == 2.2
    assert converter.kilograms_to_pounds(0) == 0
    assert converter.kilograms_to_pounds(50) == 110.23
    assert converter.kilograms_to_pounds(100) == 220.46


def test_negative_weight():
    with pytest.raises(ValueError):
        converter.pounds_to_kilograms(-5)
    with pytest.raises(ValueError):
        converter.kilograms_to_pounds(-10)


# ---- Invalid Input Tests ----

def test_invalid_input():
    with pytest.raises(ValueError):
        converter.celsius_to_fahrenheit("hot")
    with pytest.raises(ValueError):
        converter.miles_to_kilometers(None)
    with pytest.raises(ValueError):
        converter.pounds_to_kilograms([10])