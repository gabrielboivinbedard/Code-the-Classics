import pygame
import sys

# System Classes
class RenderSystem:
    def __init__(self, screen):
        self.screen = screen

    def update(self, entities):
        for entity in entities:
            position = entity.get_component(PositionComponent)
            graphics = entity.get_component(GraphicsComponent)
            if position and graphics:
                pygame.draw.rect(self.screen, graphics.color, 
                                 (position.x, position.y, graphics.width, graphics.height))