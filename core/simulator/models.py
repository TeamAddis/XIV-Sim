from django.db import models

class Simulator:
    
    def __init__(self):
        self.action_loops = []

    def add_action_loop(self, action_loop):
        self.action_loops.append(action_loop)

    def calculate_total_potency(self):
        potency = 0
        for action_loop in self.action_loops:
            potency = potency + action_loop.calculate_loop_potency()

        return potency