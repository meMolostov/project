from functools import wraps
from time import time


def log(filename=""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__

