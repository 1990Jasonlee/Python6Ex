import unittest
import temperature_utils_v2


class TemperatureUtilsTest(unittest.TestCase):

    def test_convert_to_celsius(self):
        test_cases = [
            (0, 273.15),
            (100, 373.15),
            (-100, 173.15),
            (-273.15, 0)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_to_kelvin(temp_in))

    def test3_temperature_tuple(self):
        temps_input = (-100, 0, 100)
        expected = ((-100, 173.15), (0, 273.15), (100, 373.15))
        actual = temperature_utils_v2.temperature_tuple(temps_input, 'k')
        self.assertEqual(expected, actual)
