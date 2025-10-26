import pygame
import random
import sys

pygame.init()

running = True
game_active = False

PLAYER_IMAGE = pygame.transform.scale(pygame.image.load("data/yellow.png"), (64, 64))
EVENT_A_IMAGE = pygame.transform.scale(pygame.image.load("data/red.png"), (480, 640))
EVENT_B_IMAGE = pygame.transform.scale(pygame.image.load("data/blue.png"), (480, 640))
EVENT_C_IMAGE = pygame.transform.scale(pygame.image.load("data/green.png"), (480, 640))

class GameClass:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 480, 640
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

    def menu(self):
        print(f"running: {running} /|\ game_active: {game_active}")

    def game(self):
        print(f"running: {running} /|\ game_active: {game_active}")
        self.screen.fill((0, 0, 0))
        event_A.update()
        event_A.draw() 
        player_class.draw()

class PlayerClass():
    def __init__(self):
        self.image = PLAYER_IMAGE
        self.image_rect = self.image.get_rect()
        self.player_x = (game_class.WIDTH - self.image.get_width()) // 2
        self.player_y = (game_class.HEIGHT - self.image.get_height()) // 2

    def draw(self):
        game_class.screen.blit(self.image, (self.player_x, self.player_y))

class EventA:
    def __init__(self):
        self.image = EVENT_A_IMAGE
        self.event_length = 10000
        self.eventA_event = pygame.USEREVENT +1
        pygame.time.set_timer(self.eventA_event, self.event_length)
        self.image_x = 0
        self.image_y = 0

    def update(self):
        self.image_y += 5

    def draw(self):
        game_class.screen.blit(self.image, (self.image_x, self.image_y))

class EventB:
    def __init__(self):
        self.image == EVENT_B_IMAGE
        self.event_length = 3000
        self.eventB_event = pygame.USER_EVENT +1
        pygame.time.set_timer(self.eventA_event, self.event_length)
        self.image_x = 0
        self.image_y = 0

    def update(self):
        self.image_y += 5

    def draw(self):
        game_class.screen.blit(self.image, (self.image_x, self.image_y))

class EventC:
    def __init__(self):
        self.image == EVENT_C_IMAGE
        self.event_length = 3000
        self.eventC_event = pygame.USER_EVENT +1
        pygame.time.set_timer(self.eventC_event, self.event_length)
        self.image_x = 0
        self.image_y = 0

    def update(self):
        self.image_y += 5

    def draw(self):
        game_class.screen.blit(self.image, (self.image_x, self.image_y))

game_class = GameClass()
player_class = PlayerClass()
event_A = EventA()
event_B = EventB()
event_C = EventC()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game_active:
                game_active = True

        #if event.type == event_A.event_A_event():
            
    if not game_active:
        game_class.menu()

    if game_active:
        game_class.game()

    pygame.display.update()
    game_class.clock.tick()

pygame.quit()
