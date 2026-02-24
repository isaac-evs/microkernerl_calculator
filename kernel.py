import importlib
import pkgutil

import operations


class CalculatorKernel:
    def __init__(self):
        self.registry = {}

    def load_plugins(self):
        """Load operation plugins."""
        for _, name, _ in pkgutil.iter_modules(operations.__path__):
            module = importlib.import_module(f"operations.{name}")
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if (
                    isinstance(attribute, type)
                    and hasattr(attribute, "execute")
                    and attribute_name != "OperationPlugin"
                ):
                    plugin_instance = attribute()
                    self.registry[plugin_instance.name] = plugin_instance
        print(f"Kernel: Loaded {list(self.registry.keys())} operations.")

    def compute(self, op_symbol, a, b):
        if op_symbol not in self.registry:
            raise ValueError(f"Operation '{op_symbol}' not supported.")
        return self.registry[op_symbol].execute(a, b)
