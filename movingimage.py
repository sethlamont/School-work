'''
The purpose of this program is to "animate" an image on a PyGame screen.

The animation is done by initially displaying the image at position (10,10)
with the initial direction set to RIGHT.

With each iteration of the game loop, the x or y coordinates of the image are changed by 5 pixels,
and the direction of the image is changed when the image gets too close to the corners of the screen. 
'''
print('it works')

import pygame, sys
from pygame.locals import *

pygame.init()

# frames per second setting
FPS = 60 
fpsClock = pygame.time.Clock()

# set up the Game Screen
width = 800
height = 600
Game_Screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Catch the Tech Savages!')

# initialize colors and the Image 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
Image = pygame.image.load('logo_1.png')
picture = pygame.transform.scale(Image, (75, 75))
size_x = 35
size_y = 35
picture_zoom = pygame.transform.scale(Image, (size_x, size_y))




# display the image with its original position and direction
img_x = 15
img_y = 15
direction = 'right'
Game_Screen.fill(BLACK)
Game_Screen.blit(picture, (img_x, img_y))


#-----------------------
# BEGIN main game loop
#-----------------------
while True: 

    Game_Screen.fill(BLACK)

    #-------------------------------------
    # Update the (x,y) position of image
    # and direction of image if necessary.
    #--------------------------------------
    if direction == 'right':
        img_x += 5
        img_y +=5
        if img_x % 25 == 10 :
            direction = 'down'
    elif direction == 'down':
        img_y +=5
        img_x += 5
        if img_y  == 550:
            direction = 'left'
    elif direction == 'left':
        img_x -= 5
        img_y -= 5
        if img_x == 5:
            direction = 'up'
    elif direction == 'up':
        img_y -= 5
        img_x -= 5
        if img_y % 25 == 10:
            direction = 'right'
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == MOUSEBUTTONDOWN:
            
            mse_x = mouse_pos[0]
            mse_y = mouse_pos[1]
            
            cen_x = img_x + 50
            cen_y = img_y + 45
            
            print(' image  x = ', img_x,  ' image  y = ', img_y)
            print(' center x = ', cen_x,  ' center y = ', cen_y)
            print(' mouse  x = ', mse_x,  ' mouse  y = ', mse_y)
            print()

            #
            # Hit Detection:
            #     If the x,y coordinates of mouse are within 
            #     40 pixels of center of image, then BINGO!
 
            if (abs(mse_x - cen_x) < 40 ) and (abs(mse_y - cen_y) < 40):
                size_x += 25
                size_y += 25
                picture_zoom = pygame.transform.scale(Image, (size_x, size_y))
                Game_Screen.blit(picture_zoom, (img_x, img_y))
                
                print('\n ZOOMED \n')
            
    # display the image at the new (x,y) position
    
    Game_Screen.blit(picture_zoom, (img_x, img_y))
    
    # get current position of the computer mouse
    mouse_pos = pygame.mouse.get_pos()
    
    #
    # Await the next event:
    #   If user clicks the X on the game screen --> Quit Game
    #   If user clicks the mouse button on the Game Screen,
    #      --> print the (x,y) positions of
    #          the Image, center of Image, and the mouse 
    #
 


    # update game display and time       
    pygame.display.update()
    fpsClock.tick(FPS)

#--------------------
# END main game loop
#--------------------
