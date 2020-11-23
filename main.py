import pygame
import random
import math
from pygame import mixer

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

# background sound
mixer.music.load('Attack on Titan full theme song.wav')
mixer.music.play(-1)  # -1 means it plays for loop

# player 1 function
def player(x, y):
    # blit, means draw
    # basically you draw the playerimg to a certain position
    screen.blit(playerImg, (x, y))

# Enemy


# multiple enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_for_enemies = 6
for i in range(number_for_enemies):
    enemyImg.append(pygame.image.load('red-enemy.png'))  # enemy picture

    # Enemy spawn location
    # random.randint(randomises the enemy spawn location)
    enemyX.append(random.randint(1, 729))
    enemyY.append(random.randint(1, 100))

    # Enemy movement
    enemyX_change.append(0.2)
    enemyY_change.append(40)


# Enemy function
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

bulletImg = pygame.image.load('space-ship-bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
# Ready state - You can't see the bullet on the screen
# Fire state - The bullet is currently moving
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 11, y - 32))

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def show_score(x, y):
    score = font.render(f'Score: {score_value}', True, (255, 255, 255))
    screen.blit(score, (x, y))

# GAME OVER TEXT


over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render('Master you lost uwu :(', True, (255, 255, 255))
    screen.blit(over_text, (100, 250))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 30:
        return True
    else:
        return False

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
                if bullet_state == 'ready':
                    # shooting sound effect
                    bullet_sound = mixer.Sound('Desert Eagle Shoot Sound Effect CSGO.wav')
                    bullet_sound.play()
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

    # if enemy touches border, it goes the other way
    for i in range(number_for_enemies):

        # game over
        if enemyY[i] > 200:
            for j in range(number_for_enemies):
                enemyY[j] = 2000  # moves all of the enemies under the screen
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 730:
            enemyX_change[i] = -0.2
            enemyY[i] += enemyY_change[i]

        elif enemyX[i] <= 0:
            enemyX_change[i] = 0.2
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            # collision sound effect
            collision_sound = mixer.Sound('Bruh Sound Effect 2.wav')
            collision_sound.play()
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(1, 729)
            enemyY[i] = random.randint(1, 100)
        enemy(enemyX[i], enemyY[i], i)
    # bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY <= -40:
            bulletY = 480
            bullet_state = 'ready'

    player(playerX, playerY)
    show_score(textX, textY)

    # updates display, for new movements etc..
    pygame.display.update()
