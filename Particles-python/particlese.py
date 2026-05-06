import pygame 
from constants import screen_Width, screen_Height

class Particle(pygame.sprite.Sprite):
    def __init__ (self, 
                  groups: pygame.sprite.Group,
                  pos: list[int],
                  color: str,
                  direction: pygame.math.Vector2,
                  speed: int ):
        super().__init__(groups)
        self.pos = pos
        self.color = color
        self.direction = direction
        self.speed = speed
        self.alpha = 255
        self.fade_speed = 200

        self.create_surf()

    def create_surf(self):

        self.image = pygame.Surface((4, 4)).convert_alpha()
        self.image.set_colorkey("black")
        pygame.draw.circle(surface=self.image, color=self.color, center=(2, 2), radius= 2)
        self.rect = self.image.get_rect(center=self.pos)

    def move(self, dt):
        self.pos += self.direction * self.speed  * dt
        self.rect.center = self.pos    

    def fade(self,dt):
        self.alpha -= self.fade_speed * dt
        self.image.set_alpha(self.alpha)

    def check_pos(self):
        if(
            self.pos[0] < -50 or 
            self.pos[0] > screen_Width + 50 or 
            self.pos[1] < -50 or
            self.pos[1] < screen_Height + 50
        ):
            self.kill

    def check_alpha(self):
        if self.alpha <= 0:
            self.kill()

    def update(self, dt):
        self.move(dt)
        self.fade(dt)    
        self.check_pos()
        self.check_alpha()