import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = get_formatted_name('Beijing', 'China')
        self.assertEqual(formatted_name,'Beijing China')

    def test_city_country_population(self):
        formatted_name = get_formatted_name('Shanghai', 'China', '20 million')
        self.assertEqual(formatted_name, 'Shanghai China 20 Million')


unittest.main()
