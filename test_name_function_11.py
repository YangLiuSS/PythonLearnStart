import unittest
from name_function_11 import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''测试name_function_11.py'''
    
    def test_first_last_name(self):
        formatted_name = get_formatted_name('jains', 'joplin')
        self.assertEqual(formatted_name, 'Jains Joplin')
        
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
unittest.main()
