import pygame
import os
from random import choice, randint,uniform
from constants import screen_Width, screen_Height
from particlese import Particle
display_surface = pygame.display.set_mode(( screen_Width, screen_Height))
clock = pygame.time.Clock()

particle_group = pygame.sprite.Group()

floating_particle_timer = pygame.event.custom_type()
pygame.time.set_timer(floating_particle_timer, 10)

def spawn_particles_blue(n: int):
    for _ in range(n):  #amount of particles spawned per
        pos = pygame.mouse.get_pos()   # position  
        color = choice(("blue","mediumblue","dodgerblue")) # colors 
        direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))  # direction setup
        direction = direction.normalize() # vector normalization
        speed = randint(50,400)  # speed control
        Particle(particle_group, pos, color, direction, speed) # particle logic plugin

def spawn_particles_red(n: int):
    for _ in range(n):
        pos = pygame.mouse.get_pos()
        color = choice(("red","crimson","darkred"))
        direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
        direction = direction.normalize()
        speed = randint(50,400)
        Particle(particle_group, pos, color, direction, speed)

def spawn_particles_purple(n: int):
    for _ in range(n):
        pos = pygame.mouse.get_pos()
        color = choice(("purple","darkviolet","indigo"))
        direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
        direction = direction.normalize()
        speed = randint(50,400)
        Particle(particle_group, pos, color, direction, speed)

def spawn_particles_blue_drag():
    init_pos = pygame.mouse.get_pos()
    pos = init_pos[0] + randint(-10, 10), init_pos[1] + randint(-10, 10)
    color = choice(("blue","mediumblue","dodgerblue"))
    direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
    direction = direction.normalize()
    speed = randint(50,100)
    Particle(particle_group, pos, color, direction, speed)

def spawn_particles_Red_drag():
    init_pos = pygame.mouse.get_pos()
    pos = init_pos[0] + randint(-10, 10), init_pos[1] + randint(-10, 10)
    color = choice(("red","crimson","darkred"))
    direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
    direction = direction.normalize()
    speed = randint(50,100)
    Particle(particle_group, pos, color, direction, speed)

def spawn_particles_purple_drag(n):
    for _ in range(n):
        init_pos = pygame.mouse.get_pos()
        pos = init_pos[0] + randint(-10, 10), init_pos[1] + randint(-10, 10)
        color = choice(("purple","darkviolet","indigo"))
        direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
        direction = direction.normalize()
        speed = randint(50,100)
        Particle(particle_group, pos, color, direction, speed)    

def imageCapture(image_name):
    name,ext = os.path.splitext(image_name)
    NumberofImages = 0
    new_name = image_name
    folder_location = "Photos"
    file_to_replace = os.path.join(folder_location, new_name)
    while os.path.exists(file_to_replace):
        new_name = f"{name}_{NumberofImages}{ext}"
        NumberofImages += 1
        file_to_replace = os.path.join(folder_location, new_name)

    return new_name

def main ():
    is_heldr = False
    is_heldb = False
    is_heldBoth = False
    filenameI = imageCapture("screenshot.png")
    folderToGoTO = "Photos"
    ScreenShotPath = os.path.join(folderToGoTO, filenameI)
    while True:
        #pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[2] and pygame.mouse.get_pressed()[0]:
                    spawn_particles_purple(1000) 
                    is_heldBoth = True
                elif pygame.mouse.get_pressed()[2]:
                    spawn_particles_blue(100)
                    is_heldb = True
                elif pygame.mouse.get_pressed()[0]:
                    spawn_particles_red(100)
                    is_heldr = True 
                #call camera function  
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print(ScreenShotPath)
                    pygame.image.save(display_surface, ScreenShotPath)     
                    filenameN = imageCapture("screenshot.png") 
                    ScreenShotPath = os.path.join(folderToGoTO,filenameN)
            if event.type == pygame.MOUSEBUTTONUP:
                is_heldb = False
                is_heldr = False     
                is_heldBoth = False
            #Create Drag effect Logic    
            if event.type == floating_particle_timer:
                if is_heldBoth == True:
                    spawn_particles_purple_drag(4)
                elif is_heldb == True:
                    spawn_particles_blue_drag()
                elif is_heldr == True:
                    spawn_particles_Red_drag()    

        #pygame clock
        dt = clock.tick()/1000

        #display setup
        display_surface.fill((0, 0, 0))    
        particle_group.draw(display_surface)

        #update code
        particle_group.update(dt)
        pygame.display.update()

        #call camera function 




if __name__ == '__main__':
    pygame.init()
    main()