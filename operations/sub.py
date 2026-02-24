import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interfaces import OperationPlugin

class Resta(OperationPlugin):
    @property
    def name(self): return "-"
    def execute(self, a, b): return a - b