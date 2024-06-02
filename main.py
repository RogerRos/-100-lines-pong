import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong")

ball_radius = 15
ball_speed_x = 5
ball_speed_y = 5
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

paddle_width = 10
paddle_height = 100
paddle_speed = 10

player1_pos = [10, (SCREEN_HEIGHT - paddle_height) // 2]
player2_pos = [SCREEN_WIDTH - 20, (SCREEN_HEIGHT - paddle_height) // 2]

player1_score = 0
player2_score = 0

font = pygame.font.Font(None, 74)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_pos[1] > 0:
        player1_pos[1] -= paddle_speed
    if keys[pygame.K_s] and player1_pos[1] < SCREEN_HEIGHT - paddle_height:
        player1_pos[1] += paddle_speed
    if keys[pygame.K_UP] and player2_pos[1] > 0:
        player2_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN] and player2_pos[1] < SCREEN_HEIGHT - paddle_height:
        player2_pos[1] += paddle_speed

    ball_pos[0] += ball_speed_x
    ball_pos[1] += ball_speed_y

    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y

    if ball_pos[0] - ball_radius <= player1_pos[0] + paddle_width and player1_pos[1] <= ball_pos[1] <= player1_pos[1] + paddle_height:
        ball_speed_x = -ball_speed_x
    if ball_pos[0] + ball_radius >= player2_pos[0] and player2_pos[1] <= ball_pos[1] <= player2_pos[1] + paddle_height:
        ball_speed_x = -ball_speed_x

    if ball_pos[0] - ball_radius <= 0:
        player2_score += 1
        ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        ball_speed_x = -ball_speed_x
    if ball_pos[0] + ball_radius >= SCREEN_WIDTH:
        player1_score += 1
        ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        ball_speed_x = -ball_speed_x

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player1_pos[0], player1_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (player2_pos[0], player2_pos[1], paddle_width, paddle_height))
    pygame.draw.circle(screen, WHITE, ball_pos, ball_radius)

    score_text = font.render(str(player1_score), True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 4, 10))
    score_text = font.render(str(player2_score), True, WHITE)
    screen.blit(score_text, (3 * SCREEN_WIDTH // 4, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
