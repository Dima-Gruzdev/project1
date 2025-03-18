
from unittest.mock import patch

from src.external_api import conver_to_rub


def test_conver_to_rub():
    trans = {"operationAmount": {"amount": "500.0", "currency": {"code": "RUB"}}}
    with patch("requests.get") as mock_get:
        result = conver_to_rub(trans)
        assert result == 500.0
        mock_get.assert_not_called()


# def test_conver_usd_to_rub():
#     trans = {"operationAmount":{"amount": "500.0", "currency": {"code": "USD"}}}
#     mock_response = Mock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = {"rates":{"RUB": 84}}
#     with patch("requests.get", return_value=mock_response):
#         result = conver_to_rub(trans)
#         assert result == 42000
