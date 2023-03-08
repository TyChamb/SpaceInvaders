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

class Enemy1(pygame.sprite.Sprite):
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (750,200))
enemyBase1 = pygame.image.load('Zombie1.png').convert_alpha()
enemyScaled1 = pygame.transform.scale(enemyBase1, (100, 100))
E1 = Enemy1(scrn.get_rect().center, enemyScaled1)
enemy1 = pygame.sprite.Group([E1])
enemy1.draw(scrn)
class Enemy2(pygame.sprite.Sprite):
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (650,200))
enemyBase2 = pygame.image.load('Zombie1.png').convert_alpha()
enemyScaled2 = pygame.transform.scale(enemyBase2, (100, 100))
E2 = Enemy2(scrn.get_rect().center, enemyScaled2)
enemy2 = pygame.sprite.Group([E2])
enemy2.draw(scrn)
class Enemy3(pygame.sprite.Sprite):
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (550,200))
enemyBase3 = pygame.image.load('Zombie1.png').convert_alpha()
enemyScaled3 = pygame.transform.scale(enemyBase3, (100, 100))
E3 = Enemy3(scrn.get_rect().center, enemyScaled3)
enemy3 = pygame.sprite.Group([E3])
enemy3.draw(scrn)
class Enemy4(pygame.sprite.Sprite):
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (850,200))
enemyBase4 = pygame.image.load('Zombie1.png').convert_alpha()
enemyScaled4 = pygame.transform.scale(enemyBase4, (100, 100))
E4 = Enemy4(scrn.get_rect().center, enemyScaled4)
enemy4 = pygame.sprite.Group([E4])
enemy4.draw(scrn)
class Enemy5(pygame.sprite.Sprite):
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (950,200))
enemyBase5 = pygame.image.load('Zombie1.png').convert_alpha()
enemyScaled5 = pygame.transform.scale(enemyBase5, (100, 100))
E5 = Enemy5(scrn.get_rect().center, enemyScaled5)
enemy5 = pygame.sprite.Group([E5])
enemy5.draw(scrn)
class EnemyA(pygame.sprite.Sprite):
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (700,350))
enemyBaseA = pygame.image.load('Zombie2.png').convert_alpha()
enemyScaledA = pygame.transform.scale(enemyBaseA, (50, 100))
EA = EnemyA(scrn.get_rect().center, enemyScaledA)
enemyA = pygame.sprite.Group([EA])
enemyA.draw(scrn)
class EnemyB(pygame.sprite.Sprite):
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (600,350))
enemyBaseB = pygame.image.load('Zombie2.png').convert_alpha()
enemyScaledB = pygame.transform.scale(enemyBaseB, (50, 100))
EB = EnemyB(scrn.get_rect().center, enemyScaledB)
enemyB = pygame.sprite.Group([EB])
enemyB.draw(scrn)
class EnemyC(pygame.sprite.Sprite):
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (500,350))
enemyBaseC = pygame.image.load('Zombie2.png').convert_alpha()
enemyScaledC = pygame.transform.scale(enemyBaseC, (50, 100))
EC = EnemyC(scrn.get_rect().center, enemyScaledC)
enemyC = pygame.sprite.Group([EC])
enemyC.draw(scrn)
class EnemyD(pygame.sprite.Sprite):
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (800,350))
enemyBaseD = pygame.image.load('Zombie2.png').convert_alpha()
enemyScaledD = pygame.transform.scale(enemyBaseD, (50, 100))
ED = EnemyD(scrn.get_rect().center, enemyScaledD)
enemyD = pygame.sprite.Group([ED])
enemyD.draw(scrn)
class EnemyE(pygame.sprite.Sprite):
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (900,350))
enemyBaseE = pygame.image.load('Zombie2.png').convert_alpha()
enemyScaledE = pygame.transform.scale(enemyBaseE, (50, 100))
EE = EnemyE(scrn.get_rect().center, enemyScaledE)
enemyE = pygame.sprite.Group([EE])
enemyE.draw(scrn)
class EnemyF(pygame.sprite.Sprite):
    def __init__(self, center_xy, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (1000,350))
enemyBaseF = pygame.image.load('Zombie2.png').convert_alpha()
enemyScaledF = pygame.transform.scale(enemyBaseF, (50, 100))
EF = EnemyF(scrn.get_rect().center, enemyScaledF)
enemyF = pygame.sprite.Group([EF])
enemyF.draw(scrn)

spritesB1.draw(scrn)
spritesB2.draw(scrn)
pygame.display.flip()

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
        
        if self.rect.x > 1050:
            self.rect.x -= 5
        elif self.rect.x < 400:
            self.rect.x += 5

  # fire projectile
    def fire(self):
        # set position of projectile relative to player's object rect for centerx and top
        projectile = Projectile(self.rect.centerx, self.rect.top)
        
        game_sprites.add(projectile)

        # add each projectile to sprite group for all projectiles
        projectiles.add(projectile)

# sprite base image
michelBase = pygame.image.load('Michael.png').convert_alpha()
michelScaled = pygame.transform.scale(michelBase, (55, 80))
player = Player(scrn.get_rect().center, michelScaled)
controlledPlayer = pygame.sprite.Group([player])

all_sprites = pygame.sprite.Group([background, player, barrier1, barrier2])
all_enemies = pygame.sprite.Group([E1,E2,E3,E4,E5,EA,EB,EC,ED,EE,EF])
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

    controlledPlayer.update(scrn)
    projectiles.update()

    all_sprites.update(scrn)
    all_sprites.draw(scrn)
    all_enemies.update(scrn)
    all_enemies.draw(scrn)

    projectiles.draw(scrn)
    controlledPlayer.draw(scrn)

    pygame.display.flip()

class HUD():
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


# deactivates the pygame library
pygame.quit()

