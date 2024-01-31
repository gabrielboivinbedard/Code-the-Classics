import pygame
import sys
from constants import *
from util import *



# Component Classes
class PositionComponent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class GraphicsComponent:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

