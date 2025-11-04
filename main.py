import pygame
import random
import os
import asyncio

pygame.init()

running = True
game_active = False
game_over = False
game_won = False

eventA_bool = False
eventB_bool = False

picked_bool = False

cooldown_start_time = 0
cooldown_duration = 5000

pick_insult_complete = False

player_key_complete = False

event_start_time = 0

event_successful = False
just_reset = False

PLAYER_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("data", "car.png")), (128, 192))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("data", "background.png")), (480, 640))
QUESTION_BOX = pygame.transform.scale(pygame.image.load(os.path.join("data", "question_box.png")), (220, 145))
ENEMY_A_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("data","enemyA.png")), (80, 120))
ENEMY_B_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("data","enemyB.png")), (80, 120))

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

def pick_insult():
    global insult_choice, pick_insult_complete
    insults = ["Did you get that on camera?", "Nearly...", "Dissapointing", "You can do better!", "Next time..."]
    insult_choice = random.choice(insults)
    pick_insult_complete = True

class GameClass:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 480, 640
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Chaos Car")
        self.clock = pygame.time.Clock()
        self.background = BACKGROUND
        self.background_x = 0
        self.background_y = 0
        self.font = pygame.font.Font(os.path.join("data", "font.ttf"), 32)
        self.small_font = pygame.font.Font(os.path.join("data", "font.ttf"), 20)
        self.smaller_font = pygame.font.Font(os.path.join("data", "font.ttf"), 15)
        self.points = 0

    def menu(self):
        self.screen.fill((0, 0, 0))
        print(f"running: {running} /|\ game_active: {game_active} /|\ game_over: {game_over}")
        self.line_1 = self.small_font.render("Chaos Car", True, (255, 255, 255))
        self.line_2 = self.small_font.render("ENTER to begin", True, (255, 255, 255))
        self.screen.blit(self.line_1, ((self.WIDTH - self.line_1.get_width()) // 2, (self.HEIGHT - self.line_1.get_height()) // 2 - 65))
        self.screen.blit(self.line_2, ((self.WIDTH - self.line_2.get_width()) // 2, (self.HEIGHT - self.line_2.get_height()) // 2 - 30))
    
    def game_over_function(self):
        global insult_choice, pick_insult_complete
        self.screen.fill((0, 0, 0))
        player_class.points = 0
        if not pick_insult_complete:
            pick_insult()
        self.line_1 = self.smaller_font.render(f"{insult_choice}", True, (200, 200, 200))
        self.line_2 = self.small_font.render("ENTER to try again", True, (200, 200, 200))
        self.screen.blit(self.line_1, ((self.WIDTH - self.line_1.get_width()) // 2, (self.HEIGHT - self.line_1.get_height()) // 2 - 65))
        self.screen.blit(self.line_2, ((self.WIDTH - self.line_2.get_width()) // 2, (self.HEIGHT - self.line_2.get_height()) // 2 - 30))
    
    def game_won_function(self):
        self.screen.fill((0, 0, 0))
        self.line_1 = self.smaller_font.render("How?", True, (200, 200, 200))
        self.line_2 = self.small_font.render("Congratulations!", True, (200, 200, 200))
        self.screen.blit(self.line_1, ((self.WIDTH - self.line_1.get_width()) // 2, (self.HEIGHT - self.line_1.get_height()) // 2 - 65))
        self.screen.blit(self.line_2, ((self.WIDTH - self.line_2.get_width()) // 2, (self.HEIGHT - self.line_2.get_height()) // 2 - 30))
    
    def clear_event(self):
        global eventA_bool, eventB_bool, picked_bool, event_successful, cooldown_start_time
        eventA_bool = False
        eventB_bool = False
        picked_bool = False
        event_successful = False
        cooldown_start_time = pygame.time.get_ticks()
        pygame.time.set_timer(event_A.eventA_event, 0)
        pygame.time.set_timer(event_B.eventB_event, 0)

    def update(self):
        self.background_y += 5
        if self.background_y > self.HEIGHT:
            self.background_y = 0

    def draw(self):
        self.screen.blit(self.background, (0, self.background_y))
        self.screen.blit(self.background, (0, self.background_y - self.HEIGHT))

    def reset(self):
        global game_active, game_over, cooldown_start_time, pick_insult_complete, just_reset
        global eventA_bool, eventB_bool, picked_bool, event_successful
        global player_class, event_A, event_B
        game_active = True
        game_over = False
        cooldown_start_time = pygame.time.get_ticks()
        pick_insult_complete = False
        just_reset = True
        eventA_bool = False
        eventB_bool = False
        picked_bool = False
        event_successful = False
        player_class.player_key_triggered = False
        player_class.pressed_duration = 0
        player_class.points = 0
        pygame.time.set_timer(event_A.eventA_event, 0)
        pygame.time.set_timer(event_B.eventB_event, 0)

    def game(self):
        global picked_bool, eventA_bool, eventB_bool, game_won
        print(f"running: {running} /|\ game_active: {game_active} /|\ game_over: {game_over}")
        self.screen.fill((0, 0, 0))
        current_time = pygame.time.get_ticks()
        player_class.update()
        self.update()
        self.draw()
        if self.points > 999:
            game_won = True
        self.points_text = self.font.render(f"{player_class.points}", True, (0, 0, 0))
        self.screen.blit(self.points_text, (20, 20))
        player_class.draw()
        if not picked_bool and current_time - cooldown_start_time > 5000:
            pick_random_event()
        if eventA_bool:
            event_A.draw()
        if eventB_bool:
            event_B.draw()

class PlayerClass():
    def __init__(self):
        self.image = PLAYER_IMAGE
        self.image_rect = self.image.get_rect()
        self.player_x = (game_class.WIDTH - self.image.get_width()) // 2
        self.player_y = 100
        self.player_key_triggered = False
        self.pressed_duration = 0
        self.pressed_required_duration = 1000
        self.points = 0
    
    def update(self):
        global game_over, game_active, player_key_complete, event_successful
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        if eventA_bool or eventB_bool:
            if not event_successful:
                if not self.player_key_triggered and current_time - event_start_time > 2000:
                    game_over = True
                    game_active = False
                    return

            if keys[pygame.K_e]:
                if not self.player_key_triggered:
                    self.player_key_triggered = True
                    self.pressed_duration = current_time
                
                elif current_time - self.pressed_duration >= self.pressed_required_duration:
                    event_successful = True
                    self.points +=1
                    game_class.clear_event()
                    pygame.time.set_timer(pygame.USEREVENT + 99, 500)
                    return
            else:   
                if self.player_key_triggered:
                    held_time = current_time - self.pressed_duration
                    if held_time < self.pressed_duration and not event_successful:
                        game_over = True
                        game_active = False
                    self.player_key_triggered = False
                    self.pressed_duration = 0
        else:
            self.player_key_triggered = False
            self.pressed_duration = 0
            event_successful = False
        
    def draw(self):
        game_class.screen.blit(self.image, (self.player_x, self.player_y))

class EventA:
    def __init__(self):
        self.image = ENEMY_A_IMAGE
        self.image_x = (game_class.WIDTH - 80) // 2
        self.image_y = 330
        self.eventA_event = pygame.USEREVENT +1
        self.x = 0
        self.y = 0
        self.text_background = QUESTION_BOX

    def time_set(self):
        global event_start_time
        self.event_length = 3800
        pygame.time.set_timer(self.eventA_event, self.event_length)
        event_start_time = pygame.time.get_ticks()

    def draw(self):
        self.line_1 = game_class.smaller_font.render("Watch Out!", True, (200, 200, 200))
        self.line_2 = game_class.smaller_font.render("Hold [E]", True, (200, 200, 200))
        game_class.screen.blit(self.text_background, (125, 460))
        game_class.screen.blit(self.line_1, ((game_class.WIDTH - self.line_1.get_width()) // 2, 510))
        game_class.screen.blit(self.line_2, ((game_class.WIDTH - self.line_2.get_width()) // 2, 540))
        game_class.screen.blit(self.image, (self.image_x, self.image_y))

class EventB:
    def __init__(self):
        self.image = ENEMY_A_IMAGE
        self.image_x = (game_class.WIDTH - 80) // 2
        self.image_y = 330
        self.eventB_event = pygame.USEREVENT +2
        self.text_background = QUESTION_BOX

    def time_set(self):
        global event_start_time
        self.event_length = 3800
        pygame.time.set_timer(self.eventB_event, self.event_length)
        event_start_time = pygame.time.get_ticks()

    def draw(self):
        game_class.screen.blit(self.text_background, (125, 460))
        self.line_1 = game_class.smaller_font.render("Look Out!", True, (200, 200, 200))
        self.line_2 = game_class.smaller_font.render("Hold [E]", True, (200, 200, 200))
        game_class.screen.blit(self.line_1, ((game_class.WIDTH - self.line_1.get_width()) // 2, 510))
        game_class.screen.blit(self.line_2, ((game_class.WIDTH - self.line_2.get_width()) // 2, 540))
        game_class.screen.blit(self.image, (self.image_x, self.image_y))

game_class = GameClass()
player_class = PlayerClass()
event_A = EventA()
event_B = EventB()

async def main():
    global running, game_active, game_over, game_won
    global picked_bool, eventA_bool, eventB_bool
    global cooldown_start_time, event_successful, just_reset
    global pick_insult_complete

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not game_active:
                    game_active = True
                    cooldown_start_time = pygame.time.get_ticks()

                if event.key == pygame.K_RETURN and game_over:
                    game_class.reset()

            if event.type == event_A.eventA_event:
                pygame.time.set_timer(event_A.eventA_event, 0)
                picked_bool = False
                eventA_bool = False
                cooldown_start_time = pygame.time.get_ticks()
                event_successful = False

            if event.type == event_B.eventB_event:
                pygame.time.set_timer(event_B.eventB_event, 0)
                picked_bool = False
                eventB_bool = False
                cooldown_start_time = pygame.time.get_ticks()
                event_successful = False

            if event.type == pygame.USEREVENT + 99:
                pygame.time.set_timer(pygame.USEREVENT + 99, 0)
                game_class.clear_event()

        if just_reset:
            pick_insult_complete = True
            just_reset = False

        if game_over and not game_active:
            game_class.game_over_function()

        elif game_won:
            game_class.game_won_function()

        elif not game_active:
            game_class.menu()

        elif game_active:
            game_class.game()

        pygame.display.update()
        game_class.clock.tick(60)

        await asyncio.sleep(0)
    pygame.quit()

asyncio.run(main())