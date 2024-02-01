from enum import Enum

class EntityType(Enum):
    BAT = 1
    BALL = 2
    GAME = 3


# Entity Class
class Entity:
    def __init__(self, id, type):
        self.id = id
        self.components = {}
        self.type = type

    def add_component(self, component):
        self.components[component.__class__] = component

    def get_component(self, component_type):
        return self.components.get(component_type)
    

