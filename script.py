import pygame
import random
import sys

pygame.init()

running = True
game_active = False

eventA_bool = False
eventB_bool = False

picked_bool = False

cooldown_start_time = 0
cooldown_duration = 5000

PLAYER_IMAGE = pygame.transform.scale(pygame.image.load("data/car.png"), (128, 192))
EVENT_A_IMAGE = pygame.transform.scale(pygame.image.load("data/red.png"), (480, 640))
EVENT_B_IMAGE = pygame.transform.scale(pygame.image.load("data/blue.png"), (480, 640))
GREEN_DEBUG_IMAGE = pygame.transform.scale(pygame.image.load("data/green.png"), (64, 64))
LOGO = pygame.transform.scale(pygame.image.load("data/logo.png"), (256, 256))
BACKGROUND = pygame.transform.scale(pygame.image.load("data/background.png"), (480, 640))

def pick_random_event():
    global eventA_bool, eventB_bool, picked_bool
    events = [0, 1]
    choice = random.choice(events)
    picked_bool = True
    if choice == 0:
        eventA_bool = True
        event_A.time_set()
    elif choice == 1:
        eventB_bool = True
        event_B.time_set()

class GameClass:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 480, 640
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.background = BACKGROUND
        self.background_x = 0
        self.background_y = 0

    def menu(self):
        print(f"running: {running} /|\ game_active: {game_active}")
        self.image = LOGO
        self.screen.blit(self.image, ((self.WIDTH - self.image.get_width()) // 2, (self.HEIGHT - self.image.get_height()) // 2 - 200))
    
    def update(self):
        self.background_y += 5
        if self.background_y > self.HEIGHT:
            self.background_y = 0

    def draw(self):
        self.screen.blit(self.background, (0, self.background_y))
        self.screen.blit(self.background, (0, self.background_y - self.HEIGHT))

    def game(self):
        global picked_bool, eventA_bool, eventB_bool
        print(f"running: {running} /|\ game_active: {game_active}")

        self.screen.fill((0, 0, 0))

        current_time = pygame.time.get_ticks()

        player_class.update()
        self.update()

        if not picked_bool and current_time - cooldown_start_time > 5000:
            pick_random_event()
        if eventA_bool:
            event_A.draw()
        if eventB_bool:
            event_B.draw()

        self.draw()
        player_class.draw()

class PlayerClass():
    def __init__(self):
        self.image = PLAYER_IMAGE
        self.image_rect = self.image.get_rect()
        self.player_x = (game_class.WIDTH - self.image.get_width()) // 2
        self.player_y = (game_class.HEIGHT - self.image.get_height()) // 2
        self.player_key_triggered = False
        self.pressed_duration = 0
        self.pressed_required_duration = 2000
    
    def update(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        if eventA_bool or eventB_bool:
            if keys[pygame.K_e]:
                if not self.player_key_triggered:
                    self.player_key_triggered = True
                    self.pressed_duration = current_time
                elif current_time - self.pressed_duration >= self.pressed_required_duration:
                    self.image = GREEN_DEBUG_IMAGE
                    return
            else:
                self.player_key_triggered = False
                self.pressed_duration = 0

        self.image = PLAYER_IMAGE
        
    def draw(self):
        game_class.screen.blit(self.image, (self.player_x, self.player_y))

class EventA:
    def __init__(self):
        self.image = EVENT_A_IMAGE
        self.image_x = 0
        self.image_y = 0
        self.eventA_event = pygame.USEREVENT +1

    def time_set(self):
        self.event_length = 5000
        pygame.time.set_timer(self.eventA_event, self.event_length)

    def draw(self):
        game_class.screen.blit(self.image, (self.image_x, self.image_y))

class EventB:
    def __init__(self):
        self.image = EVENT_B_IMAGE
        self.image_x = 0
        self.image_y = 0
        self.eventB_event = pygame.USEREVENT +2

    def time_set(self):
        self.event_length = 5000
        pygame.time.set_timer(self.eventB_event, self.event_length)

    def draw(self):
        game_class.screen.blit(self.image, (self.image_x, self.image_y))

game_class = GameClass()
player_class = PlayerClass()
event_A = EventA()
event_B = EventB()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game_active:
                game_active = True
                cooldown_start_time = pygame.time.get_ticks()

        if event.type == event_A.eventA_event:
            pygame.time.set_timer(event_A.eventA_event, 0)
            picked_bool = False
            eventA_bool = False
            cooldown_start_time = pygame.time.get_ticks()

        if event.type == event_B.eventB_event:
            pygame.time.set_timer(event_B.eventB_event, 0)
            picked_bool = False
            eventB_bool = False
            cooldown_start_time = pygame.time.get_ticks()

    if not game_active:
        game_class.menu()

    if game_active:
        game_class.game()

    pygame.display.update()
    game_class.clock.tick(60)

pygame.quit()