from decimal import Decimal


def calculate(num1: float, num2: float, operation: str) -> float:
    output = None
    if operation == "ARITH_MULTI":
        output = num1 * num2
    elif operation == "ARITH_ADD":
        output = num1 + num2

    return float(output)
