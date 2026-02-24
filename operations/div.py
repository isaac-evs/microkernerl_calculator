from operation_plugin import OperationPlugin


class DivOperator(OperationPlugin):
    @property
    def name(self):
        return "/"

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b