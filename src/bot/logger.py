import functools
import logging


def log_start_and_end(logger: logging.Logger):
    def inner_decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            logger.info(f"Функция {func.__name__} начала выполнение")
            result = await func(*args, **kwargs)
            logger.info(f"Функция {func.__name__} успешно завершила выполнение")
            return result

        return wrapper

    return inner_decorator
