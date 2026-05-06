import pygame
from random import choice, randint,uniform
from constants import screen_Width, screen_Height
from particlese import Particle
display_surface = pygame.display.set_mode(( screen_Width, screen_Height))
clock = pygame.time.Clock()

particle_group = pygame.sprite.Group()

def spawn_particles(n: int):
    for _ in range(n):
        pos = pygame.mouse.get_pos()
        color = choice(("blue","mediumblue","dodgerblue"))
        direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
        direction = direction.normalize()
        speed = randint(50,400)
        Particle(particle_group, pos, color, direction, speed)

def main ():
    while True:
        #pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                spawn_particles(100)
                
        #pygame clock
        dt = clock.tick()/1000

        #display setup
        display_surface.fill((0, 0, 0))    
        particle_group.draw(display_surface)

        #update code
        particle_group.update(dt)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()