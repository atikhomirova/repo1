import unittest
from cleansing import *


class TestTrimWhitespaces(unittest.TestCase):
    def setUp(self):
        self.dct = {'IsEmptyStr': '', 'OnlyWhitespaces': '   ',
                    'NoWhitespaces': 'foo123', 'NormalCase': '  Username  '}

    def test_name_not_in_dct(self):
        self.assertEqual(trim_whitespaces(self.dct, 'FaultyName'), self.dct, 
            "If name not in dict, returns original dict")

    def test_name_is_empty_str(self):
        self.assertEqual(trim_whitespaces(self.dct, ''), self.dct, 
            "If name is empty, returns original dict")

    def test_value_is_empty_str(self):
        result = trim_whitespaces(self.dct, 'IsEmptyStr')
        self.assertEqual(result['IsEmptyStr'], '')

    def test_value_contains_only_whitespaces(self):
        result = trim_whitespaces(self.dct, 'OnlyWhitespaces')
        self.assertEqual(result['OnlyWhitespaces'], '')

    def test_value_contains_no_whitespaces(self):
        result = trim_whitespaces(self.dct, 'NoWhitespaces')
        self.assertEqual(result['NoWhitespaces'], 'foo123')

    def test_normal_case(self):
        result = trim_whitespaces(self.dct, 'NormalCase')
        self.assertEqual(result['NormalCase'], 'Username')


class TestRemoveExtraWhitespaces(unittest.TestCase):
    def setUp(self):
        self.dct = {'IsEmptyStr': '', 'OnlyWhitespaces': '   ',
                    'NoWhitespaces': 'foo123', 'NormalCase': '  User    Name  '}

    def test_name_not_in_dct(self):
        self.assertEqual(remove_extra_whitespaces(self.dct, 'FaultyName'), self.dct, 
            "If name not in dict, returns original dict")

    def test_name_is_empty_str(self):
        self.assertEqual(remove_extra_whitespaces(self.dct, ''), self.dct, 
            "If name is empty, returns original dict")

    def test_value_is_empty_str(self):
        result = remove_extra_whitespaces(self.dct, 'IsEmptyStr')
        self.assertEqual(result['IsEmptyStr'], '')

    def test_value_contains_only_whitespaces(self):
        result = remove_extra_whitespaces(self.dct, 'OnlyWhitespaces')
        self.assertEqual(result['OnlyWhitespaces'], '')

    def test_value_contains_no_whitespaces(self):
        result = remove_extra_whitespaces(self.dct, 'NoWhitespaces')
        self.assertEqual(result['NoWhitespaces'], 'foo123')

    def test_normal_case(self):
        result = remove_extra_whitespaces(self.dct, 'NormalCase')
        self.assertEqual(result['NormalCase'], 'User Name')


class TestSkipRowWithValue(unittest.TestCase):
    def setUp(self):
        self.dct = {'IsEmptyStr': '', 'OnlyWhitespaces': '   ',
                    'NoWhitespaces': 'foo123', 'NormalCase': '  User    Name  '}
        # self.args_to_skip ='''
                   # noreply@frucon.net,
                   # christof.colle@frucon.net,gabriele.perego@me.com,
                   # alessia.wewerweri@gmail.com,test@mavenasgency.co.za'''

    def test_name_not_in_dct(self):
        self.assertEqual(skip_row_with_value(self.dct, 'FaultyName'), self.dct, 
            "If name not in dict, returns original dict")

    def test_name_is_empty_str(self):
        self.assertEqual(skip_row_with_value(self.dct, ''), self.dct, 
            "If name is empty, returns original dict")

    def test_with_default_argument(self):
        self.assertEqual(skip_row_with_value(self.dct, 'IsEmptyStr'), 'FILTERED')

    def test_with_custom_argument(self):
        self.assertEqual(skip_row_with_value(self.dct, 'OnlyWhitespaces', '42'), 
            self.dct)

    def test_normal_situation(self):
        #print(self.dct)
        self.assertEqual(skip_row_with_value(self.dct, 'NormalCase', 'User'),
            'FILTERED')



if __name__ == '__main__':
    unittest.main()
