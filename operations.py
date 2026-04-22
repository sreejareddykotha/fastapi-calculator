import logging

logger = logging.getLogger(__name__)


def add(a, b):
    result = a + b
    logger.info(f"add({a}, {b}) = {result}")
    return result


def subtract(a, b):
    result = a - b
    logger.info(f"subtract({a}, {b}) = {result}")
    return result


def multiply(a, b):
    result = a * b
    logger.info(f"multiply({a}, {b}) = {result}")
    return result


def divide(a, b):
    if b == 0:
        logger.error("divide() called with b = 0")
        raise ZeroDivisionError("Cannot divide by zero")
    result = a / b
    logger.info(f"divide({a}, {b}) = {result}")
    return result
