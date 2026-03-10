# common/logger.py
from common.events import CALCULATION_FAILED, CALCULATION_REQUESTED, OPERATION_PERFORMED


class EventLogger:
    def __init__(self, broker):
        self.broker = broker
        self.broker.subscribe(CALCULATION_REQUESTED, self.log_request)
        self.broker.subscribe(OPERATION_PERFORMED, self.log_success)
        self.broker.subscribe(CALCULATION_FAILED, self.log_error)

    def log_request(self, data):
        print(f"[LOGGER] 📨 Evento detectado: Solicitud de cálculo -> {data}")

    def log_success(self, data):
        print(f"[LOGGER] 🟢 Evento detectado: Operación exitosa -> {data}")

    def log_error(self, data):
        print(f"[LOGGER] 🔴 Evento detectado: Fallo en cálculo -> {data}")
