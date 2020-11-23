import pygame

# without this, the game wouldn't work
pygame.init()

# screen size ((x cords, y cords))
screen = pygame.display.set_mode((800, 600))

# game title
pygame.display.set_caption('Space Invaders')

# game icon
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-ship.png')
playerX = 370
playerY = 480

playerX_change = 0
playerY_change = 0
playerXY_up_change = 0
playerXY_down_change = 0

# player 1 function
def player(x, y):
    # blit, means draw
    # basically you draw the playerimg to a certain position

    screen.blit(playerImg, (x, y))


# game loop
running = True
while running:
    # color - (red, green, blue)
    screen.fill((0, 0, 0))

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
                playerX_change = -0.1

            if event.key == pygame.K_RIGHT:
                # makes the player go towards positive X
                playerX_change = 0.1

            # Y MOVEMENT

            if event.key == pygame.K_UP:
                playerY_change = -0.1

            if event.key == pygame.K_DOWN:
                playerY_change = 0.1


            if event.key == pygame.K_SPACE:
                print('piu')

        # if the pressed down key is relased
        if event.type == pygame.KEYUP:
            # if the relased key is K_LEFT or K_RIGHT
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # As soon as the moving arrow has been relased it changes the X speed to 0.
                playerX_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0


    # puts the player onto window
    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)

    # updates display, for new movements etc..
    pygame.display.update()
