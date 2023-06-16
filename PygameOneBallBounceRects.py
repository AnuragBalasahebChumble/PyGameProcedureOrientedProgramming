# 1. Import Packages
import pygame
from pygame.locals import *
import sys
import random

# 2. Define Constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 10
# BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3

# 3. Initialize the world
pygame.init()    # this will initialize the Pygame
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # to create a window for programme
clock = pygame.time.Clock()  # to create a clock object

# 4. Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load('images/ball.png')

# 5. Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)   # X - coordinate
ballRect.top = random.randrange(MAX_HEIGHT)   # Y - coordinate
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# 6. Loop forever

while True:
    # 7. Check for and handle events
    for event in pygame.event.get():
        # clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8. - Do any "per frame" actions
    if (ballRect.left < 0) or (ballRect.left >= MAX_WIDTH):
        xSpeed = -xSpeed  # Reverse the x direction
    if (ballRect.top < 0) or (ballRect.top >= MAX_HEIGHT):
        ySpeed = -ySpeed  # Reverse the Y direction

    # update the ball's location, using the speed in two directions.
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    window.blit(ballImage, ballRect)

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)