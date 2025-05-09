def filter_by_currency(transactions, currency):
    """Функция фильтрует список транзакций, оставляя только те, где валюта операции соответствует заданной.
       Возвращает итератор, который поочередно выдает подходящие транзакции. """

    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        transaction_currency = operation_amount.get("currency", {}).get("code")
        if transaction_currency == currency:
            yield transaction

    #filtered_by_currency = list(filter(lambda x: x["currency"] == currency, transactions))
    #return filtered_by_currency


def transaction_descriptions(transactions:[]):
    """Генератор, который поочередно возвращает описания операций из списка транзакций."""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start:int, end:int):
    """ Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999. Принимает начальное и конечное значения
    для генерации диапазона номеров."""
    for number in range(start, end+1):
        card_str = f"{number:016d}"
        formatted_card = " ".join([card_str[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_card