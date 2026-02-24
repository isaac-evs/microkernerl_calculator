import math
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from interfaces import OperationPlugin


class Multiplicacion(OperationPlugin):
    @property
    def name(self):
        return "!"

    def execute(self, a, b):
        return math.factorial(a + b)
