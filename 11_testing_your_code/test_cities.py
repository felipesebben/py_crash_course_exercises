import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does a city-country pair work?"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')


    def test_city_country_population(self):
        """Does a statement as 'Santiago, Chile -population 5000000 work?"""
        santiago_chile = city_country(
            'santiago', 'chile','50000000')
        self.assertEqual(santiago_chile, 'Santiago, Chile -population 50000000')


if __name__ == '__main__':
    unittest.main()