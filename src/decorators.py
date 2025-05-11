from functools import wraps


def log(filename=""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__

            try:
                result = func(*args, **kwargs)
                log_message = f"{func_name} ok."

                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message, end='')

                return result

            except Exception as e:
                error_message = f"{func_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

                if filename:
                    with open(filename, 'a') as f:
                        f.write(error_message)
                else:
                    print(error_message, end='')

                raise  # Повторно поднимаем исключение

        return wrapper

    return decorator
