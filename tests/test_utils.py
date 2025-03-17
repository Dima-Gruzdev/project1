import unittest
from json import JSONDecodeError
from unittest.mock import patch

from src.utils import transactions_finance
import json
import pytest


class TestJsonReader(unittest.TestCase):
    @patch('builtins.open')
    @patch('json.load')
    def test_read_json(self, mock_json_load, mock_open):
        mock_json_load.return_value = [{"key": "value"}]
        result = transactions_finance('path/to/file.json')
        self.assertEqual(result, [{"key": "value"}])


class TestJsonReader_1(unittest.TestCase):
    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_open):
        result = transactions_finance('path/to/nonexistent/file.json')
        self.assertEqual(result, [])


@patch('../data/operations.json.load', side_effect=json.JSONDecodeError("Ожидаемое значение", "", 0))
def test_read_trans_finance(mock_json_load):
    with pytest.raises(json.JSONDecodeError):
        transactions_finance('path/to/file.json')

if __name__ == '__main__':
    unittest.main()

