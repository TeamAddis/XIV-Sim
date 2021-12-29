from django.db import models



class ActionLoop:
    
    def __init__(self, id):
        self.actions = []
        self.id = id


    def add_action(self, action):
        self.actions.append(action)

    def calculate_loop_potency(self):
        potency = 0
        for action in self.actions:
            if action.potency:
                potency = potency + action.potency
        return potency