import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def conver_to_rub(transactions_finance: dict) -> float:
    """"Принимает на вход транзакцию и возвращает сумму транзакции в рублях если валюта в USD или EUR
    то идет обращение к внешему  Exchange Rates Data API."""
    value = str(transactions_finance["operationAmount"]["amount"])
    from_currency = str(transactions_finance["operationAmount"]["currency"]["code"])
    to = "RUB"
    try:
        if from_currency == to:
            return float(transactions_finance["operationAmount"]["amount"])
        else:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_currency}&amount={value}"
            headers = {"apikey": API_KEY}
            response = requests.get(url, headers=headers)
            status_code = response.status_code
            if status_code == 200:
                return response.json()["result"]
            else:
                print(f"Запрос не был успешным. Возможная причина: {response.reason}")
    except requests.exceptions.RequestException:
        print("Произошла ошибка, Видимо в коде некорректные данные")


if __name__ == "__main__":
    transactions_finance = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "1.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
    print(conver_to_rub(transactions_finance))
