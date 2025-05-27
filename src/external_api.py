import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL = 'https://api.apilayer.com/exchangerates_data/latest'


def get_exchange_rate(base_currency: str) -> float:
    """Получает текущий курс валюты к RUB через API"""
    if not API_KEY:
        raise ValueError("API key is not configured")

    params = {'base': base_currency, 'symbols': 'RUB'}
    headers = {'apikey': API_KEY}

    response = requests.get(BASE_URL, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()
    return data['rates']['RUB']


def convert_transaction_amount(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    """
    amount = float(transaction['amount'])
    currency = transaction['currency'].upper()

    if currency == 'RUB':
        return amount

    if currency not in ('USD', 'EUR'):
        raise ValueError(f"Unsupported currency: {currency}")

    rate = get_exchange_rate(currency)
    return amount * rate