from masks import get_mask_card_number
from masks import get_mask_account

def mask_account_card(type_number: str) -> str:
    """"Функция принимает строку, содержащую тип и номер карты
    или счета и возвращает строку с замаскированным номером"""
    masked_type_number = ''
    if 'счет' in type_number.lower():
        masked_type_number = 'Cчет ' + get_mask_account(type_number[5:])
    elif 'Visa Platinum' in type_number:
        masked_type_number = 'Visa Platinum ' + get_mask_card_number(type_number[-16:])
    elif 'Visa Classic' in type_number:
        masked_type_number = 'Visa Classic ' + get_mask_card_number(type_number[-16:])
    elif 'Visa Gold' in type_number:
        masked_type_number = 'Visa Gold ' + get_mask_card_number(type_number[-16:])
    elif 'MasterCard' in type_number:
        masked_type_number = 'MasterCard ' + get_mask_card_number(type_number[-16:])
    elif 'Maestro' in type_number:
        masked_type_number = 'Maestro ' + get_mask_card_number(type_number[-16:])

    return masked_type_number


def get_date(date: str) -> str:
    """ Функция принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ" ("11.03.2024")"""

    formated_date = f'{date[8:10]}.{date[5:7]}.{date[0:4]}'
    return formated_date
