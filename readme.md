# Limitless particles

## Youtube link: https://youtu.be/pX0EJ-n0DZg

## repository Link: https://github.com/Aaronicley/Final

## description 

In this program you can use your mouse to create particle effects. You can capture screenshots of the particles, and they will be saved in the photos folder.

The program runs off three files. constants.py, particles.py, and main.py. The constants.py file is used to define the window size. The particlese.py file is where the particles class is created. Important code other than some of the definable variables are the alpha check and position check. They destroy the particle after its alpha reaches zero or if it leaves the window. This prevents the program from slowing down and keeps it running smoothly. 

The main.py file handles the bulk of the code. The in imports from the other files. It uses the variables in the constants to set up a screen variable and uses the particles class in separate functions to create different particle effects. The explosions use for loops to define how many particles will spawn in each explosion while the trails are tied to an if statement and spawn as long as they are true. The Booleans are toggled on and off with the use of pygames eventkeydown events. The effect is achieved by importing choice, randint, and uniform from random.

Screen captures can be made by pressing the space bar by utilizing the pygame.image.save command. They will all be saved in s photos folder and be uniquely named. by importing os to create a file path into the photos folder and creates a custom filename based off of the name of the last photo. This is by updating the path every time the pygame.image.save command is used The program can be full screened if the TAB key is pressed. 