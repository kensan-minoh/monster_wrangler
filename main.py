import pygame
import random

# create a display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GAME_WINDOW_UP = 100
GAME_WINDOW_BOTTOM = WINDOW_HEIGHT - 100

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Monster Wrangler')


# set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# main game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # fill the background
    display_surface.fill((0, 0, 0))

    # draw the game window
    pygame.draw.rect(display_surface, 'orange', 
                     (0, GAME_WINDOW_UP, WINDOW_WIDTH, GAME_WINDOW_BOTTOM-GAME_WINDOW_UP), width=2)

    # update the display
    pygame.display.update()

    clock.tick(FPS)

# end the game
pygame.quit()
