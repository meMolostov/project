import json


def load_transactions(file_path):
    """
        Принимает на вход путь до JSON-файла и возвращает список словарей
        с данными о финансовых транзакциях.
        Если файл пустой, содержит не список или не найден,
        функция возвращает пустой список
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            else:
                return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []
    except Exception:
        return []
