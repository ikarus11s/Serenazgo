import threading
import time
from simulation_automovil import simulate_automovil
from simulation_a_pie import simulate_a_pie
from simulation_motorizado import simulate_motorizado

class SimulationController:
    def __init__(self):
        self.automovil_thread = threading.Thread(target=simulate_automovil)
        self.a_pie_thread = threading.Thread(target=simulate_a_pie)
        self.motorizado_thread = threading.Thread(target=simulate_motorizado)
        self.running = False

    def start_simulations(self):
        self.running = True
        self.automovil_thread.start()
        self.a_pie_thread.start()
        self.motorizado_thread.start()

    def stop_simulations(self):
        self.running = False
        self.automovil_thread.join()
        self.a_pie_thread.join()
        self.motorizado_thread.join()

simulation_controller = SimulationController()