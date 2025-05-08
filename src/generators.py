def filter_by_currency(transactions:[], currency: str):
    """Функция фильтрует список транзакций, оставляя только те, где валюта операции соответствует заданной.
       Возвращает итератор, который поочередно выдает подходящие транзакции. """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        transaction_currency = operation_amount.get("currency", {}).get("code")
        if transaction_currency == currency:
            yield transaction
