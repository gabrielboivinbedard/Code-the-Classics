from .entity import *
from .component import *
from constants import *
from util import *
import pgzero, pgzrun, pygame

# System Classes
class RenderSystem:
    def __init__(self, screen):
        self.screen = screen

    def update(self, entities):
        self.screen.blit("table", (0,0))

        for entity in entities:
            position = entity.get_component(PositionComponent)
            graphics = entity.get_component(GraphicsComponent)
            timer = entity.get_component(TimerComponent)
            player = entity.get_component(PlayerComponent)

            if timer and player: #mettre les effets si un but a ete marque
                if timer > 0: #TODO Check if ball is out
                    self.screen.blit("effect"+str(player-1), (0,0))
            
            if position and graphics:

                if timer and player:
                    pass
                
            
class SoundSystem:
    def __init__(self, screen):
        pass

    def update(self, entities):
        pass        

class DynamicSystem:
    def __init__(self):
        pass

    def update(self, entities):
        for entity in entities:
            position = entity.get_component(PositionComponent)
            velocity = entity.get_component(VelocityComponent)
            player = entity.get_component(PlayerComponent)
            timer = entity.get_component(TimerComponent)

            if velocity and position: #Ball Logic
                original_x = entity.x

                entity.x += entity.dx
                entity.y += entity.dy

                ballsign = sign( entity.x - HALF_WIDTH)

                for ent2 in entities:
                        
                        if ent2.type == EntityType.BAT:
                            batsign = sign(ent2.get_component(PositionComponent).x - HALF_WIDTH) #trouve l'entite de la bat du cote ou la balle se trouve
                            if batsign == ballsign:
                                activebat = ent2
                            if batsign != ballsign:
                                opposingbat = ent2

                        if ent2.type == EntityType.GAME:
                            game = ent2
                    
                if abs(entity.x - HALF_WIDTH) >= 344 and abs(original_x - HALF_WIDTH) < 344: 
                    
                    if entity.x < HALF_WIDTH:
                        new_dir_x = 1
                        
                    else:
                        new_dir_x = -1

                    difference_y = entity.y - activebat.y

                    if difference_y > -64 and difference_y < 64: #Check si la balle frappe une bat
                        entity.dx = -entity.dx
                        entity.dy += difference_y / 128
                        entity.dy = min(max(self.dy, -1), 1)
                        self.dx, self.dy = normalised(self.dx, self.dy)

                        # TODO Create an impact effect
                        # game.impacts.append(Impact((self.x - new_dir_x * 10, self.y)))

                        entity.speed += 1

                        # TODO Add an offset to the AI player's target Y position, so it won't aim to hit the ball exactly
                        # in the centre of the bat
                        # game.ai_offset = random.randint(-10, 10)

                        # Bat glows for 10 frames
                        activebat.timer = 10

                        # TODO Play hit sounds, with more intense sound effects as the ball gets faster
                        # game.play_sound("hit", 5)  # play every time in addition to:
                        # if self.speed <= 10:
                        #     game.play_sound("hit_slow", 1)
                        # elif self.speed <= 12:
                        #     game.play_sound("hit_medium", 1)
                        # elif self.speed <= 16:
                        #     game.play_sound("hit_fast", 1)
                        # else:
                        #     game.play_sound("hit_veryfast", 1)
                if abs(entity.y - HALF_HEIGHT) > 220:
                    entity.dy = -entity.dy
                    entity.y += entity.dy

                    # TODO Create impact effect
                    # game.impacts.append(Impact(self.pos))

                    # TODO Sound effect
                    # game.play_sound("bounce", 5)
                    # game.play_sound("bounce_synth", 1)
                if entity.x <0 or entity.x > WIDTH: #TODO logique de scorer un but
                    if activebat.timer < 0:
                        opposingbat.score += 1
                        # TODO play sound
                        # game.play_sound("score_goal", 1)
                        activebat.timer = 20
                    elif activebat.timer == 0: #Reset Ball
                        entity.speed = 5
                        entity.x = HALF_WIDTH
                        entity.y = HALF_HEIGHT
                        # TODO Set la direction de la balle vers la active bat
                        
                        if sign(activebat.get_component(PositionComponent).x - HALF_WIDTH) < 0:
                            entity.dx = -1
                        else:
                            entity.dx = 1

            if player and timer: #Paddle Logic
                for ent3 in entities:
                    if ent3.type == EntityType.BALL:
                        ball = ent3
                entity.timer -= 1
                frame = 0
                if timer > 0:
                    if ball.x <0 or ball.x > WIDTH:
                        frame = 2
                    else:
                        frame = 1
                
                entity.path = "bat" + str(entity.player-1) + str(frame)

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