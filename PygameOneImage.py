# 1. Import Packages
import pygame
from pygame.locals import *
import sys


# 2. Define Constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND =30


# 3. Initialize the world
pygame.init()    # this will initialize the Pygame
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # to create a window for programme

clock = pygame.time.Clock()  # to create a clock object

# 4. Load assets: image(s), sound(s), etc.

ballImage = pygame.image.load('images/ball.png')

# 5. Initialize variables

# 6. Loop forever

while True:
    # 7. Check for and handle events
    for event in pygame.event.get():
        # clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8. - Do any "per frame" actions

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements

    # draw ball at position 100 across (x) and 200 down (y)
    window.blit(ballImage, (100, 200))

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)