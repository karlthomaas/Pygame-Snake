import pygame
import random

# without this, the game wouldn't work
pygame.init()

# screen size ((x cords, y cords))
screen = pygame.display.set_mode((800, 600))

# game title
pygame.display.set_caption('Space Invaders')

# game icon
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)

# game background
background = pygame.image.load('space-ship-bg.png')

# Player
playerImg = pygame.image.load('space-ship2.png')
# Player spawn location
playerX = 370
playerY = 480

playerX_change = 0
playerY_change = 0

# player speed
player_speed = 0.3

# player 1 function
def player(x, y):
    # blit, means draw
    # basically you draw the playerimg to a certain position
    screen.blit(playerImg, (x, y))


# Enemy
enemyImg = pygame.image.load('red-enemy.png')  # enemy picture

# Enemy spawn location
# random.randint(randomises the enemy spawn location)
enemyX = random.randint(1, 800)
enemyY = random.randint(1, 100)

# Enemy movement
enemyX_Change = 0.2
enemyY_Change = 40


# Enemy function
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

bulletImg = pygame.image.load('space-ship-bullet.png')
bulletX = 0
bulletY = 480
bulletX_Change = 0
bulletY_Change = 1
# Ready state - You can't see the bullet on the screen
# Fire state - The bullet is currently moving
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 11, y - 32))

# game loop
running = True
while running:
    # bg color - (red, green, blue)
    screen.fill((0, 0, 0))
    # bg image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        # if the X is pressed on window
        if event.type == pygame.QUIT:
            running = False

        # checks if key is pressed and whether it's right or left
        if event.type == pygame.KEYDOWN:
            # if the pressed key is left arrow

            # X MOVEMENT

            # if the pressed key is left arrow
            if event.key == pygame.K_LEFT:
                # makes the player go towards negative X
                playerX_change = -player_speed

            if event.key == pygame.K_RIGHT:
                # makes the player go towards positive X
                playerX_change = player_speed

            # Y MOVEMENT

            if event.key == pygame.K_UP:
                playerY_change = -player_speed

            if event.key == pygame.K_DOWN:
                playerY_change = player_speed

            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)


        # if the pressed down key is relased
        if event.type == pygame.KEYUP:
            # if the relased key is K_LEFT or K_RIGHT
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # As soon as the moving arrow has been relased it changes the X speed to 0.
                playerX_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0


    playerX += playerX_change
    playerY += playerY_change

    # if player cords is less than zero (borderline), it changes the location to the other side
    if playerX <= 0:
        playerX = 0
    # if player cords is more than borderline, it changes the player location to the other side
    elif playerX >= 730:
        playerX = 730

    # firstly moves to the right
    enemyX += enemyX_Change

    # if enemy touches border, it goes the other way
    if enemyX >= 730:
        enemyX_Change = -0.2
        enemyY += enemyY_Change

    elif enemyX <= 0:
        enemyX_Change = 0.2
        enemyY += enemyY_Change

    # bullet movement
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_Change
        if bulletY <= -40:
            bulletY = 480
            bullet_state = 'ready'

    player(playerX, playerY)
    enemy(enemyX, enemyY)


    # updates display, for new movements etc..
    pygame.display.update()
