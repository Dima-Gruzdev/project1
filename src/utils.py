import json
import logging


logger = logging.getLogger("utils.py")
file_handler = logging.FileHandler('utils.log', 'w', encoding="utf8")
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def transactions_finance(path: str) -> any:
    """Функция которая с json файла возращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            transactions_dict = json.load(f)
            logger.info(transactions_dict)
            return transactions_dict
    except (json.JSONDecodeError, FileNotFoundError):
        logger.error("Файл не найден")
        return []


if __name__ == '__main__':
    print(transactions_finance('../data/operations.json'))
