def filter_by_state(transactions: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """ Фильтрует список словарей, оставляя только те, у которых ключ 'state'
       равен заданному значению """
    result_transaction = []
    for transaction in transactions:
        if transaction.get('state') == state:
            result_transaction.append(transaction)
    return result_transaction


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """ Сортирует список словарей по дате (ключ 'date') в заданном порядке """
    return sorted(transactions, key=lambda transaction: transaction['date'], reverse=reverse)
