# Import Modules
import pygame
pygame.init()

from tkinter import *
import random


# Game settings 
projectileColor = (255, 0, 0)
projectileSpeed = 10

fps = 30
clock = pygame.time.Clock()

playerSpeed = 5


# Sprite groups
game_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()


# Text font
font = pygame.font.Font('freesansbold.ttf', 20)


# Screen settings
screenX = 1500
screenY = 800
scrn = pygame.display.set_mode((screenX, screenY))

# Base images
backgroundBase = pygame.image.load('Background.png').convert_alpha()
backgroundBase = pygame.transform.scale(backgroundBase, (screenX, screenY))

michelBase = pygame.image.load("Michael.png").convert_alpha()

carOneBase = pygame.image.load('Car1.png').convert_alpha()
carOneBase = pygame.transform.scale(carOneBase, (250, 125))

carTwoBase = pygame.image.load('Car2.png').convert_alpha()
carTwoBase = pygame.transform.scale(carTwoBase, (250, 125))

enemyBase = pygame.image.load('Zombie1.png').convert_alpha()
enemyBase = pygame.transform.scale(enemyBase, (100, 100))

# enemy spawn variables and lists
enemyImg = []
enemyX = []
enemyY = []
enemyCount = 11
enemySpawnX = 450



# Background Classification
class Background(pygame.sprite.Sprite):
    
    def __init__(self, center_xy, image):
        super().__init__() 

        self.image = image
        self.rect = self.image.get_rect(center = ((screenX / 2), (screenY /2)))

# Spawn background in the center of the screen
background = Background(scrn.get_rect().center, backgroundBase)



# car (environmental Objects) classifications and spawn positions
class CarOne(pygame.sprite.Sprite):
    
    def __init__(self, center_xy, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect(center = (500,500))

# second car classification
class CarTwo(pygame.sprite.Sprite):
    
    def __init__(self, center_xy, image):
        super().__init__() 

        self.image = image
        self.rect = self.image.get_rect(center = (1000,500))


# spawn the first car on the given position
carOne = CarOne(scrn.get_rect().center, carOneBase)
carV1 = pygame.sprite.Group([carOne])

#spawn the second car on the given position
carTwo = CarTwo(scrn.get_rect().center, carTwoBase)
carV2 = pygame.sprite.Group([carTwo])



# enemy Classification
class Enemy(pygame.sprite.Sprite):
    def __init__(self, center, spawnX, spawnY, image):
        super().__init__() 

        self.image = image
        self.rect = self.image.get_rect(center = (spawnX, spawnY))





carV1.draw(scrn)
carV2.draw(scrn)
pygame.display.flip()

scrn.blit(pygame.transform.scale(michelBase, (60, 60)), (175, 680))
scrn.blit(pygame.transform.scale(michelBase, (60, 60)), (237, 680))

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
        
        # remove projectile from the game if it goes past end of screen
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




# Spawn and assign player controls to Michael
michelBase = pygame.image.load('Michael.png').convert_alpha()
michelBase = pygame.transform.scale(michelBase, (55, 80))

player = Player(scrn.get_rect().center, michelBase)
controlledPlayer = pygame.sprite.Group([player])

# spawn enemies 
for i in range(enemyCount):
    enemyImg.append(pygame.image.load('Zombie2.png'))
    enemyImg[i] = pygame.transform.scale(enemyImg[i], (35, 60))

    enemyX.append(enemySpawnX)
    enemyY.append(200)

    scrn.blit(enemyImg[i], (enemyX[i], enemyY[i]))

    # change spawn position for the next enemy
    enemySpawnX = enemySpawnX + 60


# spawn cars onto the screen
carV1.draw(scrn)
carV2.draw(scrn)
pygame.display.flip()

# put all sprites into a group
all_sprites = pygame.sprite.Group([background, player, carOne, carTwo])


# loop until player quits the game
pygame.display.flip()
status = True
while (status):
    # Reset screen, then go to next frame
    scrn.fill(0)
    clock.tick(fps)

    # check events
    for event in pygame.event.get():
        
        # check if player quit the game
        if event.type == pygame.QUIT:
            # if player quit the game, end the loop
            status = False
           
        # check if player presses space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # if player pressed space, fire a projectile
                player.fire()

    # update all sprites
    controlledPlayer.update(scrn)
    projectiles.update()

    all_sprites.update(scrn)
    all_sprites.draw(scrn)
    

    projectiles.draw(scrn)
    controlledPlayer.draw(scrn)

    # flip screen orientation to normal again
    pygame.display.flip()


# deactivate pygame and close the window once the loop ends
pygame.quit()
