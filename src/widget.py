from datetime import datetime


def mask_account_card(mask_number_card: str) -> str:
    """Фунцкция которая принимает счет и номер карты и возвращает зашифрованный"""
    mask_card_split = mask_number_card.split()
    mask_card_isalpha = []
    mask_card_isdigit = []
    if "Счет" in mask_card_split:
        return f"Счет **{mask_number_card[-4:]}"
    for i in mask_card_split:
        if i.isalpha():
            mask_card_isalpha.append(i)
        elif i.isdigit():
            mask_card_isdigit.append(i)
    card_isdigit_join: str = ''.join(mask_card_isdigit)
    return f"{' '.join(mask_card_isalpha)} {card_isdigit_join[:4]} {card_isdigit_join[4:6]}** **** {card_isdigit_join[-4:]}"


print(mask_account_card("Maestro 7000792289606361"))


def get_date(edited_date: str) -> str:
    """Функция которая принимает дату ввиде 2024-03-11T02:26:18.671407 и возращает в формате
    ДД.ММ.Г"""
    date_obj = datetime.strptime(edited_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
