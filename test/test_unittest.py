import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import converter


class TestTemperature(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(converter.celsius_to_fahrenheit(0), 32)
        self.assertEqual(converter.celsius_to_fahrenheit(100), 212)
        self.assertEqual(converter.celsius_to_fahrenheit(-40), -40)
        self.assertEqual(converter.celsius_to_fahrenheit(37), 98.6)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(converter.fahrenheit_to_celsius(32), 0)
        self.assertEqual(converter.fahrenheit_to_celsius(212), 100)
        self.assertEqual(converter.fahrenheit_to_celsius(-40), -40)
        self.assertEqual(converter.fahrenheit_to_celsius(98.6), 37)

    def test_celsius_to_kelvin(self):
        self.assertEqual(converter.celsius_to_kelvin(0), 273.15)
        self.assertEqual(converter.celsius_to_kelvin(100), 373.15)
        self.assertEqual(converter.celsius_to_kelvin(-273.15), 0)
        self.assertEqual(converter.celsius_to_kelvin(25.5), 298.65)

    def test_celsius_to_kelvin_below_absolute_zero(self):
        with self.assertRaises(ValueError):
            converter.celsius_to_kelvin(-300)


class TestDistance(unittest.TestCase):

    def test_miles_to_kilometers(self):
        self.assertEqual(converter.miles_to_kilometers(1), 1.61)
        self.assertEqual(converter.miles_to_kilometers(0), 0)
        self.assertEqual(converter.miles_to_kilometers(5), 8.05)
        self.assertEqual(converter.miles_to_kilometers(100), 160.93)

    def test_kilometers_to_miles(self):
        self.assertEqual(converter.kilometers_to_miles(1), 0.62)
        self.assertEqual(converter.kilometers_to_miles(0), 0)
        self.assertEqual(converter.kilometers_to_miles(10), 6.21)

    def test_negative_distance(self):
        with self.assertRaises(ValueError):
            converter.miles_to_kilometers(-5)
        with self.assertRaises(ValueError):
            converter.kilometers_to_miles(-10)

    def test_decimal_distance_values(self):
        self.assertEqual(converter.miles_to_kilometers(2.5), 4.02)
        self.assertEqual(converter.kilometers_to_miles(2.5), 1.55)


class TestWeight(unittest.TestCase):

    def test_pounds_to_kilograms(self):
        self.assertEqual(converter.pounds_to_kilograms(1), 0.45)
        self.assertEqual(converter.pounds_to_kilograms(0), 0)
        self.assertEqual(converter.pounds_to_kilograms(100), 45.36)
        self.assertEqual(converter.pounds_to_kilograms(220), 99.79)

    def test_kilograms_to_pounds(self):
        self.assertEqual(converter.kilograms_to_pounds(1), 2.2)
        self.assertEqual(converter.kilograms_to_pounds(0), 0)
        self.assertEqual(converter.kilograms_to_pounds(50), 110.23)
        self.assertEqual(converter.kilograms_to_pounds(100), 220.46)

    def test_negative_weight(self):
        with self.assertRaises(ValueError):
            converter.pounds_to_kilograms(-5)
        with self.assertRaises(ValueError):
            converter.kilograms_to_pounds(-10)

    def test_decimal_weight_values(self):
        self.assertEqual(converter.pounds_to_kilograms(2.5), 1.13)
        self.assertEqual(converter.kilograms_to_pounds(2.5), 5.51)


class TestInvalidInput(unittest.TestCase):

    def test_invalid_input_types(self):
        with self.assertRaises(ValueError):
            converter.celsius_to_fahrenheit("hot")
        with self.assertRaises(ValueError):
            converter.miles_to_kilometers(None)
        with self.assertRaises(ValueError):
            converter.pounds_to_kilograms([10])


if __name__ == '__main__':
    unittest.main()
