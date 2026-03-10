# ui/cli_handler.py
from common.events import CALCULATION_FAILED, CALCULATION_REQUESTED, OPERATION_PERFORMED


class CalculatorCLI:
    def __init__(self, broker):
        self.broker = broker
        # Escucha los resultados
        self.broker.subscribe(OPERATION_PERFORMED, self.display_result)
        self.broker.subscribe(CALCULATION_FAILED, self.display_error)

    def request_calculation(self, a, op, b):
        print(f"\n[CLI] 👤 El usuario ingresó: {a} {op} {b}")
        self.broker.publish(CALCULATION_REQUESTED, {"a": a, "op": op, "b": b})

    def display_result(self, data):
        print(f"[CLI] ✅ Mostrar al usuario: El resultado es {data['result']}")

    def display_error(self, data):
        print(f"[CLI] ❌ Mostrar al usuario: Ocurrió un error -> {data['error']}")
