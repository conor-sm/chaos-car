import pygame
import random
import sys

pygame.init()

running = True
game_active = False

class GameClass:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 500, 700
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

    def menu(self):
        print(f"running: {running} /|\ game_active: {game_active}")

    def game(self):
        print(f"running: {running} /|\ game_active: {game_active}")

game_class = GameClass()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game_active:
                game_active = True

    if not game_active:
        game_class.menu()

    if game_active:
        game_class.game()

    pygame.display.update()
    game_class.clock.tick()

pygame.quit()
