import pygame
import random
import math

# intialise the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('5512626.jpg')

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('001-space-ship.png')
playerX = 380
playerY = 480
playerX_change = 0

# enemy
enemyImg = pygame.image.load('001-outer-space.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 20

# bullet
bulletImg = pygame.image.load('001-bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 1, y + 10))


def isCollision(enemyX, enemyY, bulletX, BulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:

    screen.fill((30, 0, 74))
    # background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check weather it is right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_LALT:
                playerX_change = -0.7
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_RALT:
                playerX_change = 0.7
            if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 760:
        playerX = 760

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += bulletY_change
    elif enemyX >= 760:
        enemyX_change = -0.3
        enemyY += bulletY_change

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #collision
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print (score)
        enemyX = random.randint(0, 800)
        enemyY = random.randint(50, 150)




    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
