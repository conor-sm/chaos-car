import pygame
import random
import sys

pygame.init()

running = True
game_active = False

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def menu():
    print(f"running: {running} /|\ game_active: {game_active}")

def game():
    print(f"running: {running} /|\ game_active: {game_active}")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game_active:
                game_active = True

    if not game_active:
        menu()

    if game_active:
        game()

    pygame.display.update()
    clock.tick()

pygame.quit()
