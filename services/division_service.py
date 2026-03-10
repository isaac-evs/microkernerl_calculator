# services/division_service.py
from common.events import CALCULATION_FAILED, CALCULATION_REQUESTED, OPERATION_PERFORMED


class DivisionWorker:
    def __init__(self, broker):
        self.broker = broker
        self.broker.subscribe(CALCULATION_REQUESTED, self.handle_event)

    def handle_event(self, data):
        if data.get("op") == "/":
            try:
                if data["b"] == 0:
                    raise ValueError("División por cero no permitida.")
                result = data["a"] / data["b"]
                self.broker.publish(OPERATION_PERFORMED, {"result": result, "op": "/"})
            except Exception as e:
                self.broker.publish(CALCULATION_FAILED, {"error": str(e), "op": "/"})
