# services/multiplier_service.py
from common.events import CALCULATION_REQUESTED, OPERATION_PERFORMED


class MultiplierWorker:
    def __init__(self, broker):
        self.broker = broker
        self.broker.subscribe(CALCULATION_REQUESTED, self.handle_event)

    def handle_event(self, data):
        if data.get("op") == "*":
            result = data["a"] * data["b"]
            self.broker.publish(OPERATION_PERFORMED, {"result": result, "op": "*"})
