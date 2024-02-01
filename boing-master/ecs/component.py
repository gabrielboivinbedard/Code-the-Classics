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

class PlayerComponent:
    def __init__(self, player):
        self.player = player

class SoundComponent:
    def __init__(self, sounds):
        pass

class ScoreComponent:
    def __init__(self, score):
        self.score = score

class TimerComponent:
    def __init__(self, counter):
        self.counter = counter

class EffectComponent:
    def __init__(self, effect):
        self.effect = effect