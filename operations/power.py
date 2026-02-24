from operation_plugin import OperationPlugin

class PowerOperator(OperationPlugin):
    @property
    def name(self):
        return "**"

    def execute(self, a: float, b: float) -> float:
        return a ** b