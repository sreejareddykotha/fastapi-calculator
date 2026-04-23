class CalculationFactory:
    @staticmethod
    def calculate(a: float, b: float, calculation_type: str) -> float:
        if calculation_type == "Add":
            return a + b
        elif calculation_type == "Sub":
            return a - b
        elif calculation_type == "Multiply":
            return a * b
        elif calculation_type == "Divide":
            if b == 0:
                raise ValueError("Division by zero is not allowed")
            return a / b
        else:
            raise ValueError("Invalid calculation type")