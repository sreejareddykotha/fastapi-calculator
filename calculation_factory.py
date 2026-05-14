from operations import (
    add,
    subtract,
    multiply,
    divide,
    power,
    modulus
)


class CalculationFactory:

    @staticmethod
    def calculate(a, b, calculation_type):

        operations = {
            "Add": add,
            "Subtract": subtract,
            "Multiply": multiply,
            "Divide": divide,
            "Power": power,
            "Modulus": modulus
        }

        if calculation_type not in operations:

            raise ValueError(
                f"Invalid calculation type: {calculation_type}"
            )

        return operations[calculation_type](a, b)
    