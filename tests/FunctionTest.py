# from datetime import datetime
# from src.masks import get_mask_card_number
#
#
# def mask_account_card(mask_number_card: str) -> str:
#     """Фунцкция которая принимает счет и номер карты и возвращает зашифрованный"""
#     s = get_mask_card_number('card_number')
#     mask_card_split = mask_number_card.split()
#     card_isalpha = []
#     card_isdigit = []
#     if "Счет" in mask_card_split:
#         return f"Счет **{mask_number_card[-4:]}"
#     for i in mask_card_split:
#         if i.isalpha():
#             card_isalpha.append(i)
#         elif i.isdigit():
#             card_isdigit.append(i)
#     card_join: str = "".join(card_isdigit)
#     return f"{' '.join(card_isalpha)} {s}"
#
#
# print(mask_account_card("Maestro 7000792289606361"))



# def get_mask_card_number(card_number: str) -> str:
#     """Функция которая на вход принимает номер карты а возращает на половину зашифрованный"""
#     return f"{card_number[-4:]} {card_number[4:6]}** **** {card_number[12:]}"
#
#
# def get_mask_account(mask_account: str) -> str:
#     """Функция которая принимает номер счета и возращает зашифрованный номер и 4 последние цифры"""
#     return f"**{mask_account[-4:]}"
#
#
# print(get_mask_card_number("7005007857712585"))
# print(get_mask_account("51298752159625475835"))


# def get_mask_card_number(card_number: str) -> str:
#     """Функция которая на вход принимает номер карты а возращает на половину зашифрованный"""
#     if len(card_number) != 16:
#         return "Неверное количество цифр карты "
#     else:
#         return f"{card_number[-4:]} {card_number[4:6]}** **** {card_number[12:]}"
#
#
# def get_mask_account(mask_account: str) -> str:
#     """Функция которая принимает номер счета и возращает зашифрованный номер и 4 последние цифры"""
#     if len(mask_account) != 20:
#         return "Неверное количетсво цифр счета"
#     else:
#         return f"**{mask_account[-4:]}"
#
#
# print(get_mask_card_number("7005007857712585"))
# print(get_mask_account("51298752159625475835"))