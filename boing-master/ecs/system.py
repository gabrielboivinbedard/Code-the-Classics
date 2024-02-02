from entity import *
from component import *
from constants import *
from util import *
from pygame import mixer
import os
import sys
import logging

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Boing!!')

IMG_PATH = os.path.join(os.getcwd(), "boing-master", "images")

# System Classes
class RenderSystem:
    def __init__(self, screen):
        self.screen = screen
        

    def update(self, entities):
        image_path = os.path.join(IMG_PATH, "table.png")
        image_surface = pygame.image.load(image_path)
        self.screen.blit(image_surface, (0,0))

        for entity in entities:
            logging.info(entity.type)
            position = entity.get_component(PositionComponent)
            graphics = entity.get_component(GraphicsComponent)
            timer = entity.get_component(TimerComponent)
            player = entity.get_component(PlayerComponent)

            if timer and player: 
                if timer.counter > 0: 
                    self.screen.blit("effect"+str(player-1), (0,0))
            
            if position and graphics:
                image_path = os.path.join(IMG_PATH, graphics.path+".png")
                image_surface = pygame.image.load(image_path)
                self.screen.blit(image_surface, (0,0))
              
class SoundSystem:
    def __init__(self, screen):
        mixer.init()

    def update(self, entities):
        for entity in entities:
            sounds = entity.get_component(SoundComponent)

            if sounds:
                for sound in sounds.sounds:
                    try:
                        mixer.Sound.play(sound)
                    except Exception as e:
                        pass

                sounds.sounds.clear()

class DynamicSystem:
    def __init__(self):
        pass

    def update(self, entities):
        for entity in entities:
            position = entity.get_component(PositionComponent)
            velocity = entity.get_component(VelocityComponent)
            player = entity.get_component(PlayerComponent)
            timer = entity.get_component(TimerComponent)
            soundsC = entity.get_component(SoundComponent)
            graphics = entity.get_component(GraphicsComponent)

            if velocity and position: #Ball Logic
                original_x = position.x

                position.x += velocity.dx
                position.y += velocity.dy

                ballsign = sign( position.x - HALF_WIDTH)

                for ent2 in entities:
                        
                        if ent2.type == EntityType.BAT:
                            batsign = sign(ent2.get_component(PositionComponent).x - HALF_WIDTH) #trouve l'entite de la bat du cote ou la balle se trouve
                            if batsign == ballsign:
                                activebat = ent2
                            if batsign != ballsign:
                                opposingbat = ent2

                        if ent2.type == EntityType.GAME:
                            game = ent2
                    
                if abs(position.x - HALF_WIDTH) >= 344 and abs(original_x - HALF_WIDTH) < 344: 
                    
                    if position.x < HALF_WIDTH:
                        new_dir_x = 1
                        
                    else:
                        new_dir_x = -1

                    difference_y = position.y - activebat.get_component(PositionComponent).y

                    if difference_y > -64 and difference_y < 64: #Check si la balle frappe une bat
                        velocity.dx = -velocity.dx
                        velocity.dy += difference_y / 128
                        velocity.dy = min(max(velocity.dy, -1), 1)
                        velocity.dx, velocity.dy = normalised(velocity.dx, velocity.dy)

                        # TODO Create an impact effect
                        # game.impacts.append(Impact((self.x - new_dir_x * 10, self.y)))

                        velocity.speed += 1

                        # TODO Add an offset to the AI player's target Y position, so it won't aim to hit the ball exactly
                        # in the centre of the bat
                        # game.ai_offset = random.randint(-10, 10)

                        # Bat glows for 10 frames
                        activebat.get_component(TimerComponent).counter = 10

                        if soundsC:
                            sound1 = "hit" + str(random.randint(0, 4))

                            soundsC.sounds.append(sound1)
                            if entity.speed <= 10:
                                sound2 = "hit_slow0"
                                soundsC.sounds.append(sound2)
                            elif entity.speed <= 12:
                                sound2 = "hit_medium0"
                                soundsC.sounds.append(sound2)
                            elif entity.speed <= 16:
                                sound2 = "hit_fast0"
                                soundsC.sounds.append(sound2)
                            else:
                                sound2 = "hit_veryfast0"
                                soundsC.sounds.append(sound2)

                if abs(position.y - HALF_HEIGHT) > 220:
                    velocity.dy = -velocity.dy
                    position.y += velocity.dy

                    # TODO Create impact effect
                    # game.impacts.append(Impact(self.pos))
                    
                    if soundsC:
                        sound1 = "bounce" + str(random.randint(0, 4))
                        ball.sounds.append(sound1)
                        ball.sounds.append("bounce_synth0")

                if position.x <0 or position.x > WIDTH: #TODO logique de scorer un but
                    if activebat.get_component(TimerComponent).counter < 0:
                        opposingbat.get_component(ScoreComponent).score += 1

                        soundsC.sounds.append("score_goal0")

                        activebat.get_component(TimerComponent).counter = 20
                    elif activebat.get_component(TimerComponent).counter == 0: #Reset Ball
                        velocity.speed = 5
                        position.x = HALF_WIDTH
                        position.y = HALF_HEIGHT
                        velocity.dy = 0

                        if sign(activebat.get_component(PositionComponent).x - HALF_WIDTH) < 0:
                            velocity.dx = -1
                        else:
                            velocity.dx = 1

            if player and timer and graphics: #Paddle Logic
                for ent3 in entities:
                    if ent3.type == EntityType.BALL:
                        ball = ent3
                timer.counter -= 1
                frame = 0
                if timer.counter > 0:
                    if ball.get_component(PositionComponent).x <0 or ball.get_component(PositionComponent).x > WIDTH:
                        frame = 2
                    else:
                        frame = 1
                
                graphics.path = "bat" + str(player.player-1) + str(frame)

class EffectsSystem:
    def __init__(self, screen):
        pass

    def update(self, entities):
        pass   

class ControlSystem:
    def __init__(self, screen):
        pass

    def update(self, entities):

        pass  


# Initialize Pygame
    
entities = []

bat1 = Entity(1, EntityType.BAT)
bat1.add_component(PositionComponent(40, HALF_HEIGHT))
bat1.add_component(GraphicsComponent("bat00"))
bat1.add_component(ControlComponent(Control.PLAYER1))
bat1.add_component(ScoreComponent(0))
bat1.add_component(PlayerComponent(1))

bat2 = Entity(2, EntityType.BAT)
bat2.add_component(PositionComponent(760, HALF_HEIGHT))
bat2.add_component(GraphicsComponent("bat10"))
bat2.add_component(ControlComponent(Control.AI))
bat2.add_component(ScoreComponent(0))
bat2.add_component(PlayerComponent(2))

ball = Entity(3, EntityType.BALL)
ball.add_component(PositionComponent(HALF_WIDTH,HALF_HEIGHT))
ball.add_component(VelocityComponent(-1))
ball.add_component(GraphicsComponent("ball"))


entities.append(bat1)
entities.append(bat2)
entities.append(ball)

render_system = RenderSystem(screen)
dynamic_system = DynamicSystem()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update Systems
    render_system.update(entities)
    dynamic_system.update(entities)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    pygame.display.update()


# Quit Pygame
pygame.quit()
sys.exit()

