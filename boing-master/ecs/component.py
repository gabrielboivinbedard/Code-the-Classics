import pgzero, pgzrun, pygame
import math, sys, random


# Component Classes
class PositionComponent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class GraphicsComponent:
    def __init__(self, path):
        self.path = path

class VelocityComponent:
    def __init__(self, dx=0, dy=0, speed=5):
        self.dx = dx
        self.dy = dy
        self.speed = speed

class ControlComponent:
    def __init__(self, control):
        self.control = control

class SoundComponent:
    def __init__(self, sounds):
        pass

class BallComponent:
    def __init__(self):
        pass

class BatComponent:
    def __init__(self):
        pass