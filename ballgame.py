#!/usr/local/bin/python3
import pygame
import random

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((600, 600))

# Define ball properties
ball_x = 300
ball_y = 300
ball_radius = 10
ball_speed_x = 5
ball_speed_y = 5
ball_color = (255, 255, 255)

# Define block properties
block_width = 50
block_height = 25
block_color = (255, 255, 0)
block_list = []
for i in range(5):
    block_x = random.randint(0, 550)
    block_y = random.randint(0, 550)
    block_list.append([block_x, block_y])

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # decreases speed by 1 in the x direction
                ball_speed_x -= 1
            elif event.key == pygame.K_RIGHT: #increases speed by 1 in the x direction
                ball_speed_x += 1
            elif event.key == pygame.K_UP:#decreases speed by 1 in the y direction
                ball_speed_y -= 1
            elif event.key == pygame.K_DOWN: #increases speed by 1 in the y direction
                ball_speed_y += 1
    
    # Clear screen
    screen.fill((0, 0, 0))
    
    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Check for ball hitting walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= 600:
        ball_speed_x *= -1
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= 600:
        ball_speed_y *= -1
    
    # Check for ball hitting blocks
    for block in block_list:
        if ball_x > block[0] and ball_x < block[0] + block_width and ball_y > block[1] and ball_y < block[1] + block_height:
            ball_speed_y *= -1
            block_list.remove(block)
            break
    
    # Draw ball
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)
    
    # Draw blocks
    for block in block_list:
        pygame.draw.rect(screen, block_color, pygame.Rect(block[0], block[1], block_width, block_height))
    
    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()
