import logging

logger = logging.getLogger("masks.py")
file_handler = logging.FileHandler('masks.log', 'w', encoding="utf8")
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция которая на вход принимает номер карты а возращает на половину зашифрованный"""
    if len(card_number) == 0:
        logger.error("Пустая строка")
        return "Пустая строка"
    elif len(card_number) > 16 or len(card_number) < 16:
        logger.error("Неверное количество цифр")
        return "Неверное количество цифр"
    logger.info(f"{card_number[-4:]} {card_number[4:6]}** **** {card_number[12:]}")
    return f"{card_number[-4:]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция которая принимает номер счета и возращает зашифрованный номер и 4 последние цифры"""
    if len(mask_account) == 0:
        logger.error("Пустая строка")
        return "Пустая строка"
    elif len(mask_account) < 20:
        logger.error("Неверная длина счета")
        return "Неверная длина счета"
    logger.info(f"**{mask_account[-4:]}")
    return f"**{mask_account[-4:]}"


print(get_mask_account("52522233584258622626"))
print(get_mask_card_number("0047857231871258"))
