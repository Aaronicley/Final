# Limitless particles

## Youtube link: https://youtu.be/pX0EJ-n0DZg

## repository Link: https://github.com/Aaronicley/Final

## description 

In this program you can use your mouse to create particle effects. You can capture screenshots of the particles and they will save to the photos folder.

The program runs off of three files. constants.py , particles.py and main.py. The constants.py file  is used to define the the window size. The particlese.py file is where the particles class is created. Important code other than some of the definabled variables is are the alpha check and position check. They destroy the particle after it's alpha reaches zero or if it leaves the window. This prevents the program from slowing down and keeps it running smoothly. 

The main.py file handles the bulk of the code. The in imports from the other files. It uses the variables in the constants to setup a screen varibale and uses the particles class in speperate functions to create different particle effects. The ecplosions use for loops to define how many particles will spawn in each explosion while the trails are tied to an if statement and spawn as long as they are true. The booleans are toggled on and of with the use of pygames eventkeydown events. The effect is achevied by impoting choice, randint, and uniform from random.

Screen captures can be made by pressing the space bar by utilizing the pygame.image.save command. They will all be saved in s photos folder and be uniquely named. by importing os to create a file path into the photos folder and creates a custom filename based off of the name of the last photo. this is by updateding the path every time the pygame.image.save command is uesed The program can be fullscreened if the TAB key is pressed. 