def get_mask_card_number(card_number: str) -> str:
    """Функция которая на вход принимает номер карты а возращает на половину зашифрованный"""
    return f"{card_number[-4:]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция которая принимает номер счета и возращает зашифрованный номер и 4 последние цифры"""
    return f"**{mask_account[-4:]}"


print(get_mask_card_number("7005007857712585"))
print(get_mask_account("51298752159625475835"))
