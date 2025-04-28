def get_mask_card_number(card_number: str) -> str:
    """ Функция принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    cleaned_number = card_number.replace(" ", "")
    first_part = cleaned_number[:6]
    last_part = cleaned_number[-4:]
    hidden_part = "** ****"
    masked_number = f"{first_part[:4]} {first_part[4:6]}{hidden_part} {last_part}"
    if card_number == '' or len(cleaned_number) != 16:
        return 'Введите корректные данные'
    else:
        return masked_number


def get_mask_account(account: str) -> str:
    """" Функция принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX
    """
    cleaned_account = account.replace(" ", "")
    last_part_account = cleaned_account[-4:]
    hidden_part_account = "**"
    masked_account = f"{hidden_part_account}{last_part_account}"
    if account == '' or len(cleaned_account) != 20:
        return 'Введите корректные данные'
    else:
        return masked_account
