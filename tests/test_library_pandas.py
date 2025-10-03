from unittest.mock import patch
import unittest


from src.library_pandas import reading_transactions_csv


class TestJsonReader_csv_1(unittest.TestCase):
    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_open):
        result = reading_transactions_csv('path/to/nonexistent/file.csv')
        self.assertEqual(result, [])


class TestJsonReader_csv(unittest.TestCase):
    @patch('builtins.open')
    @patch('src.library_pandas.csv.DictReader')
    def test_read_csv(self, data_file, mock_open):
        data_file.return_value = [{"key": "value"}]
        result = reading_transactions_csv('path/to/file.csv')
        self.assertEqual(result, [{"key": "value"}])
