import pygame
import random

# classed
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, color, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(color + '_monster64.png')
        self.rect = self.image.get_rect(topleft=(x,y))
        self.velocity_x = random.randint(1, 5) * random.choice([1,-1])
        self.velocity_y = abs(self.velocity_x) * random.choice([1,-1])
        self.color = color

    def update(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.velocity_x *=-1
        if self.rect.top < GAME_WINDOW_UP or self.rect.bottom > GAME_WINDOW_BOTTOM:
            self.velocity_y *=-1

class Knight(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('knight64.png')
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT-50))
        self.velocity = 5

    def update(self):
        self.move()
        self.check_collisions()
        

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > GAME_WINDOW_UP:
            self.rect.y += -self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < GAME_WINDOW_BOTTOM:
            self.rect.y += self.velocity
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x += -self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity 

    def check_collisions(self):
        collided_sprites = pygame.sprite.spritecollide(self, monster_group, False)
        if collided_sprites:
            
            for sprite in collided_sprites:
                if sprite.color == target_monster_group.sprite.color:
                    my_game.hit_sound.play()

                    monster_group.remove(sprite)
                    if len(monster_group) == 0:
                        my_game.play_again_message()
                    else:   
                        my_game.making_target_monster()

            
    

class Game():
    def __init__(self):
        self.hit_sound = pygame.mixer.Sound('hit_sound.wav')
        self.score = 0
    def update(self):
        self.make_hud()

    def start_messege(self):
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
                    pygame.quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    is_waiting = False

    def play_again_message(self):
        final_score_text = my_font.render(f'FINAL SCORE: {score}', True, 'red')
        # final_score_text = pygame.transform.scale(final_score_text, (128, 128))
        final_score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        display_surface.blit(final_score_text, final_score_rect)
        start_text = my_font.render("Press 'Enter' To Play Again", True, 'white')
        start_rect = start_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 40))
        display_surface.blit(start_text, start_rect)
        pygame.display.update()

        is_waiting = True
        while is_waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    is_waiting = False

    def new_round(self):
        self.score = 0
        self.lives = STARTING_LIVES
        

    def making_monster(self, round):
        for j in range(round):
            colors = ["blue", "green", "orange", "purple"]
            for i in range(4):
                color = random.choice(colors)
                colors.remove(color)
                x = random.randint(0, WINDOW_WIDTH-64)
                y = random.randint(GAME_WINDOW_UP, GAME_WINDOW_BOTTOM-64)
                Monster(x, y, color, monster_group)

    def making_target_monster(self):
        sprite = random.choice(monster_group.sprites())
        color = sprite.color
        x = WINDOW_WIDTH // 2 -32
        y = 30
        target_monster = Monster(x, y, color, target_monster_group)
        print(target_monster)
    def making_knight(self):
        Knight(knight_group)

    def make_hud(self):
        score_text = my_font.render(f'SCORE: {score}',True, 'white')
        score_rect = score_text.get_rect(topleft =(5, 5))
        display_surface.blit(score_text, score_rect)
        lives_text = my_font.render(f'LIVES: {lives}',True, 'white')
        lives_rect = lives_text.get_rect(topleft =(5, 35))
        display_surface.blit(lives_text, lives_rect)
        current_round_text = my_font.render(f'CURRENT ROUND: {round}', True, 'white')
        current_round_rect = current_round_text.get_rect(topleft = (5, 65))
        display_surface.blit(current_round_text, current_round_rect)
        current_catch_text = my_font.render('CURRENT CATCH', True, 'white')
        current_catch_rect = current_catch_text.get_rect(midtop=(WINDOW_WIDTH//2, 5))
        display_surface.blit(current_catch_text, current_catch_rect)
        round_time_text = my_font.render(f'ROUND TIME: {round_time}', True, 'white')
        round_time_rect = round_time_text.get_rect(topright=(WINDOW_WIDTH-5, 5))
        display_surface.blit(round_time_text, round_time_rect)
        warps_text = my_font.render(f'WARPS: {warps}', True, 'white')
        warps_rect = warps_text.get_rect(topright=(WINDOW_WIDTH-5, 35))
        display_surface.blit(warps_text, warps_rect)



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
STARTING_SCORE = 0
score = STARTING_SCORE
STARTING_LIVES = 5
lives = STARTING_LIVES
STARTING_ROUND = 1
round = STARTING_ROUND
STARTING_ROUND_TIME = 0
round_time = STARTING_ROUND_TIME
STARTING_WARPS = 3
warps = STARTING_WARPS

# 

# set FPS and clock
FPS = 60
clock = pygame.time.Clock()

my_game = Game()
my_game.start_messege()

monster_group = pygame.sprite.Group()
target_monster_group =pygame.sprite.GroupSingle()
knight_group = pygame.sprite.Group()
my_game.making_monster(round)
my_game.making_target_monster()
my_game.making_knight()


# main game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the background
    display_surface.fill((0, 0, 0))

    # draw the game window
    pygame.draw.rect(display_surface, target_monster_group.sprite.color, 
                     (0, GAME_WINDOW_UP, WINDOW_WIDTH, GAME_WINDOW_BOTTOM-GAME_WINDOW_UP), width=2)

    # draw assets
    my_game.update()
    monster_group.update()
    monster_group.draw(display_surface)

    target_monster_group.draw(display_surface)
    pygame.draw.rect(display_surface, target_monster_group.sprite.color, target_monster_group.sprite.rect, width=1)
    knight_group.update()
    knight_group.draw(display_surface)

    # update the display
    pygame.display.update()

    clock.tick(FPS)

# end the game
pygame.quit()
