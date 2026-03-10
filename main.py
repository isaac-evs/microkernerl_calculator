# main.py
from broker.event_broker import EventBroker
from common.logger import EventLogger
from services.addition_service import AdditionWorker
from services.division_service import DivisionWorker
from services.multiplier_service import MultiplierWorker
from ui.cli_handler import CalculatorCLI


def main():
    print("--- Iniciando Sistema Calculadora EDA ---\n")

    # 1. Levantar Infraestructura
    broker = EventBroker()
    logger = EventLogger(broker)  # Monitoreo global

    # 2. Levantar Microservicios (Workers)
    AdditionWorker(broker)
    DivisionWorker(broker)
    MultiplierWorker(broker)

    # 3. Levantar la Interfaz de Usuario
    cli = CalculatorCLI(broker)

    # 4. Simular la interacción del usuario
    cli.request_calculation(10, "+", 5)
    cli.request_calculation(12, "*", 3)
    cli.request_calculation(20, "/", 4)
    cli.request_calculation(5, "/", 0)  # Prueba de error gestionado

    # Prueba de evento ignorado (no hay servicio para la resta)
    # Notarás que el logger registra la petición, pero no hay respuesta.
    cli.request_calculation(10, "-", 5)


if __name__ == "__main__":
    main()
