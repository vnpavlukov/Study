import unittest
from Test_17_get_formatted_name import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'jolpin')
        self.assertEqual(formatted_name, 'Janis Jolpin')


unittest.main()
