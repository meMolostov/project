def filter_by_state(operations:list[dict], state: str = 'EXECUTED') -> list[dict]:
    """ Фильтрует список словарей, оставляя только те, у которых ключ 'state'
       равен заданному значению """
    result_operation = []
    for operation in operations:
        if operation.get('state') == state:
            result_operation.append(operation)
    return result_operation


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """ Сортирует список словарей по дате (ключ 'date') в заданном порядке """
    return sorted(operations, key=lambda operation: operation.get('date'), reverse= reverse)
