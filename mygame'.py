import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 8
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Initialize the ball
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))

# Initialize the paddles
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 70, 10, 140)
opponent = pygame.Rect(10, HEIGHT // 2 - 70, 10, 140)

# Scores
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= PADDLE_SPEED

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x = -ball_speed_x

    if ball.left <= 0:
        player_score += 1
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_speed_x = BALL_SPEED
        ball_speed_y = BALL_SPEED

    if ball.right >= WIDTH:
        opponent_score += 1
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_speed_x = -BALL_SPEED
        ball_speed_y = BALL_SPEED

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Display scores
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH - 50, 50))
    screen.blit(opponent_text, (20, 50))

    pygame.display.flip()

pygame.quit()
