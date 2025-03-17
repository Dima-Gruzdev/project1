# import unittest
# from unittest.mock import patch
#
# import requests
#
# from src import conver_to_rub
#
#
# @patch("requests.get")
# def test_conver_to_rub(mock_get):
#     expected = [
#         {"RUB": 500,
#          "RUB": 2000}]
#     mock_get.return_value.return_value = expected
#     assert conver_to_rub() == expected
#     mock_get.assert_called_once()
