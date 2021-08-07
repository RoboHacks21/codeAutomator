
# 1: Import the library pygame
import pygame
from pygame.locals import *

# 2: Initiate pygame
pygame.init()
pygame.font.init()

# 3: Determine the size of the playing field
width, height = 64*10, 64*8
screen=pygame.display.set_mode((width, height))

# 4: Create x and y position for the player
player_x = 200
player_y = 200

# 5: Import Images
player = pygame.image.load("../images/SlimeFighter.jpg")

# 6: Create while loop that don't end
while 1:
    # 7: Illustrate a white board
    screen.fill((255,255,255))

    # 8: Draw the image player on an x, y coordinate
    screen.blit(player, (player_x, player_y))

    # 9: Update the playing field
    pygame.display.flip()

    # 10: Process all new events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)