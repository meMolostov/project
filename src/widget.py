def mask_account_card(type_number: str) -> str:
    """"Функция принимает строку, содержащую тип и номер карты
    или счета и возвращает строку с замаскированным номером"""
    parts = type_number.split(' ', 1)
    if len(parts) != 2:
        return type_number  # если не удалось разделить, возвращаем как есть

    name, number = parts

    if type_number.lower() == 'счет':
        masked_type_number = '**' + number[-4:]
    else:
        # Маскировка для карты: первые 4, затем 2**, потом 4 последние
        if len(number) < 16:
            return type_number  # если номер слишком короткий для карты

        masked_type_number = (
            f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
        )
    return f"{name} {masked_type_number}"


def get_date(date: str) -> str:
    """ Функция принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ" ("11.03.2024")"""

    formated_date = f'"ДД.ММ.ГГГГ" ("{date[9:11]}.{date[6:8]}.{date[1:5]}")'
    return formated_date
