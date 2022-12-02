# Snake game

import pygame
import random


pygame.init()
pygame.display.set_caption("Snake Game and AI")

WIDTH = 24
HEIGHT = 24
SCREEN = pygame.display.set_mode((500, 500))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
SPEED = 25
x_head = 251
y_head = 251
direction = None
apple_x = random.randrange(26, 476, 25)
apple_y = random.randrange(26, 476, 25)
length = 0
x_pos = [x_head]
y_pos = [y_head]


def grid():
    for x in range(25, 500, 25):
        pygame.draw.rect(SCREEN, WHITE, (x, 25, 1, 450))

    for y in range(25, 500, 25):
        pygame.draw.rect(SCREEN, WHITE, (25, y, 450, 1))


def press_key():
    global direction
    global keys
    if keys[pygame.K_RIGHT] and direction != 'left':
        direction = 'right'
    if keys[pygame.K_LEFT] and direction != 'right':
        direction = 'left'
    if keys[pygame.K_UP] and direction != 'down':
        direction = 'up'
    if keys[pygame.K_DOWN] and direction != 'up':
        direction = 'down'


def move_snake():
    global x_head
    global y_head
    global SCREEN
    global WIDTH
    global HEIGHT
    if direction == 'right':
        x_head += SPEED
    if direction == 'left':
        x_head -= SPEED
    if direction == 'up':
        y_head -= SPEED
    if direction == 'down':
        y_head += SPEED


def eat_apple():
    global apple_x
    global apple_y
    global length
    if x_head == apple_x and y_head == apple_y:
        apple_x = random.randrange(26, 476, 25)
        apple_y = random.randrange(26, 476, 25)
        if direction == 'right':
            pass
        if direction == 'left':
            pass
        if direction == 'up':
            pass
        if direction == 'down':
            pass
        length += 1
    pygame.draw.rect(SCREEN, RED, (apple_x, apple_y, WIDTH, HEIGHT))


def grow_snake():
    move_snake()
    global x_pos
    global y_pos
    for i in range(length):
        pygame.draw.rect(SCREEN, GREEN, (x_pos[i], y_pos[i], WIDTH, HEIGHT))


def game_over():
    global is_running
    if x_head < 26 or x_head > 456 or y_head < 26 or y_head > 456:
        is_running = False


is_running = True
while is_running:
    pygame.time.delay(150)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys = pygame.key.get_pressed()
    press_key()
    move_snake()
    SCREEN.fill(BLACK)
    grid()
    grow_snake()
    eat_apple()
    game_over()
    pygame.display.update()


pygame.quit()