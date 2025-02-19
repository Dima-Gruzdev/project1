def get_mask_card_number(card_number: str) -> str:
    """Функция которая на вход принимает номер карты а возращает на половину зашифрованный"""
    return f"{card_number[-4:]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция которая принимает номер счета и возращает зашифрованный номер и 4 последние цифры"""
    if mask_account == "":
        return "Пустая строка"
    elif len(mask_account) > 20 or len(mask_account) < 20:
        return "Неверная длина счета"
    return f"**{mask_account[-4:]}"


print(get_mask_account("52523623584258622626"))
print(get_mask_card_number("7005007857712585"))
