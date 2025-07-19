import pygame
import random

# classed
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('blue_monster64.png')
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self):
        pass

class Knight(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

    def update(self):
        pass

class Game():
    def __init__(self):
        pass
    
    def update(self):
        pass

    def new_game_start(self):
        title_text = my_font.render("MONSTER WRANGLER",True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))

        # start messege
        start_text = my_font.render("Press 'Enter' To Begin", True, 'white')
        start_rect = start_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 40))

        display_surface.blit(title_text, title_rect)
        display_surface.blit(start_text, start_rect)
        pygame.display.update()

        is_waiting = True
        while is_waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_waiting = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    is_waiting = False

    def making_monster(self, round):
        for i in range(4*round):
            x = random.randint(0, WINDOW_WIDTH-64)
            y = random.randint(GAME_WINDOW_UP, GAME_WINDOW_BOTTOM-64)
            Monster(x, y, monster_group)

    def main_game_loop(self):
        # main game loop
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            



            # fill the background
            display_surface.fill((0, 0, 0))

            # draw the game window
            pygame.draw.rect(display_surface, PURPLE, 
                            (0, GAME_WINDOW_UP, WINDOW_WIDTH, GAME_WINDOW_BOTTOM-GAME_WINDOW_UP), width=2)

            # draw assets
            monster_group.draw(display_surface)

            # update the display
            pygame.display.update()

            clock.tick(FPS)








# initialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GAME_WINDOW_UP = 100
GAME_WINDOW_BOTTOM = WINDOW_HEIGHT - 100

# colors
BLUE = (70, 189, 240)
PURPLE = (234, 46, 255)
ORANGE = (245, 157, 24)
GREEN = (83, 207, 56)

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Monster Wrangler')

my_font = pygame.font.Font("game_font.ttf", 24)

# game variables
round = 2


# set FPS and clock
FPS = 60
clock = pygame.time.Clock()

my_game = Game()
my_game.new_game_start()

monster_group = pygame.sprite.Group()


# for i in range(4):
#     x = random.randint(0, WINDOW_WIDTH-64)
#     y = random.randint(GAME_WINDOW_UP, GAME_WINDOW_BOTTOM-64)
#     Monster(x, y, monster_group)

my_game.making_monster(round)
my_game.main_game_loop()



# end the game
pygame.quit()
