import pygame
import sys
# from ecs.entity import

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('ECS Pattern Example')






# Create Entities
player = Entity(1)
player.add_component(PositionComponent(100, 100))
player.add_component(GraphicsComponent((255, 0, 0), 50, 50))

# List of all entities
entities = [player]

# Initialize Systems
render_system = RenderSystem(screen)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update Systems
    screen.fill((0, 0, 0))  # Clear screen
    render_system.update(entities)

    # Update the display
    pygame.display.flip()

    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

