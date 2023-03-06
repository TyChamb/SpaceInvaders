import pygame
pygame.init()
from tkinter import *
import random
projectileColor = (255, 0, 0)
playerSpeed = 5
projectileSpeed = 10
game_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 20)

surface = pygame.display.set_mode((1500,800))
color = (150, 150, 150)
color2 = (30, 30, 30)
color3 = (0, 0, 0)

X = 1500
Y = 800
 
# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))


# set the pygame window name
pygame.display.set_caption('image')

class Background(pygame.sprite.Sprite):
    
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (760,500))

backBase = pygame.image.load('Background.png').convert_alpha()
backScaled = pygame.transform.scale(backBase, (1800, 1000))
background = Background(scrn.get_rect().center, backScaled)
spritesBack = pygame.sprite.Group([background])

# create a surface object, image is drawn on it.
back = pygame.image.load("Background.png").convert_alpha()
michel = pygame.image.load("Michael.png").convert_alpha()

#scrn.blit(pygame.transform.scale(back, (1500, 1000)), (0, 0))
#scrn.blit(pygame.transform.scale(back, (1700, 1000)), (-60, -20))

class Barrier1(pygame.sprite.Sprite):
    
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (500,500))

class Barrier2(pygame.sprite.Sprite):
    
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (1000,500))


# sprite base image
carBase1 = pygame.image.load('Car1.png').convert_alpha()
carScaled1 = pygame.transform.scale(carBase1, (250, 125))
barrier1 = Barrier1(scrn.get_rect().center, carScaled1)
spritesB1 = pygame.sprite.Group([barrier1])

carBase2 = pygame.image.load('Car2.png').convert_alpha()
carScaled2 = pygame.transform.scale(carBase2, (250, 125))
barrier2 = Barrier2(scrn.get_rect().center, carScaled2)
spritesB2 = pygame.sprite.Group([barrier2])


spritesB1.draw(scrn)
spritesB2.draw(scrn)
pygame.display.flip()

pygame.draw.rect(surface, color3,(0, 0, 150, 900))
pygame.draw.rect(surface, color3,(1350, 0, 150, 900))
pygame.draw.rect(surface, color3,(0, 0, 1500, 50))
pygame.draw.rect(surface, color3,(0, 750, 1500, 50))

pygame.draw.rect(surface, color2,(150, 100, 1205, 1))
pygame.draw.rect(surface, color2,(150, 675, 1205, 1))

pygame.draw.rect(surface, color,(150, 50, 5, 700))
pygame.draw.rect(surface, color,(1350, 50, 5, 700))
pygame.draw.rect(surface, color,(150, 50, 1205, 5))
pygame.draw.rect(surface, color,(150, 750, 1205, 5))



scrn.blit(pygame.transform.scale(michel, (60, 60)), (175, 680))
scrn.blit(pygame.transform.scale(michel, (60, 60)), (237.5, 680))

class Projectile(pygame.sprite.Sprite):
# add specific spawn location for bullet based on player position
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 10))
        self.image.fill(projectileColor)
        self.rect = self.image.get_rect()
 
        # weapon fired from top of player
        self.rect.bottom = y
        self.rect.centerx = x

        # projectile speed
        self.speed_y = -(projectileSpeed)

    def update(self):
        self.rect.y += self.speed_y
        
        # remove from game if it goes past end of screen
        if self.rect.bottom < 0:
            self.kill()

# player classification
class Player(pygame.sprite.Sprite):
    
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (750,600))

    # player movement
    def update(self, surf):
        keys = pygame.key.get_pressed()
        self.rect.x += (keys[pygame.K_d]-keys[pygame.K_a]) * 5 
        
        self.rect.clamp_ip(surf.get_rect())

  # fire projectile
    def fire(self):
        # set position of projectile relative to player's object rect for centerx and top
        projectile = Projectile(self.rect.centerx, self.rect.top)
        
        game_sprites.add(projectile)

        # add each projectile to sprite group for all projectiles
        projectiles.add(projectile)

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('Zombie2.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

def enemy(x, y, i):
    scrn.blit(enemyImg[i], (x, y))


# sprite base image
michelBase = pygame.image.load('Michael.png').convert_alpha()
michelScaled = pygame.transform.scale(michelBase, (55, 80))
player = Player(scrn.get_rect().center, michelScaled)
controlledPlayer = pygame.sprite.Group([player])

all_sprites = pygame.sprite.Group([background, player, barrier1, barrier2])


#background = 
# loop that stops the program when the player quits

pygame.display.flip()
status = True
while (status):
    scrn.fill(0)
    clock.tick(30)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            status = False
           
           # if space is pressed, fire a projectile
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()

    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        enemy(enemyX[i], enemyY[i], i)

    controlledPlayer.update(scrn)
    projectiles.update()

    all_sprites.update(scrn)
    all_sprites.draw(scrn)

    projectiles.draw(scrn)
    controlledPlayer.draw(scrn)

    pygame.display.flip()

# deactivates the pygame library
pygame.quit()

