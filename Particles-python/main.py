import pygame

from constants import screen_Width, screen_Height

display_surface = pygame.display.set_mode(( screen_Width, screen_Height))
clock = pygame.time.Clock()

def main ():
    while True:
        #pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        #pygame clock
        clock.tick()

        #display setup and update
        display_surface.fill((0, 0, 0))    
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()