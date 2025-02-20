from datetime import datetime
from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(mask_number_card: str) -> str:
    """Фунцкция которая принимает счет и номер карты и возвращает зашифрованный"""
    mask_card_split = mask_number_card.split()
    card_isalpha = []
    card_isdigit = []
    if "Счет" in mask_card_split:
        return f"Счет {get_mask_account(mask_number_card)}"
    for item in mask_number_card:
        if item == "!" or item == "," or item == ".":
            return "Недопустимые символы"
    for i in mask_card_split:
        if i.isalpha():
            card_isalpha.append(i)
        elif i.isdigit():
            card_isdigit.append(i)
    card_join: str = "".join(card_isdigit)
    return f"{' '.join(card_isalpha)} {get_mask_card_number(card_join)}"


print(mask_account_card("Maestro 7000792289606362"))
print(mask_account_card("Счет 7000792229651826361"))


def get_date(edited_date: str) -> str:
    """Функция которая принимает дату ввиде 2024-03-11T02:26:18.671407 и возращает в формате
    ДД.ММ.Г"""
    date_obj = datetime.strptime(edited_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
