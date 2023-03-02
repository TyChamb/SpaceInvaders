import pygame
pygame.init()
from tkinter import *
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

# create a surface object, image is drawn on it.
back = pygame.image.load("Background.png").convert_alpha()
michel = pygame.image.load("Michael.png").convert_alpha()

scrn.blit(pygame.transform.scale(back, (1500, 1000)), (0, 0))
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
    
# sprite base image
michelBase = pygame.image.load('Michael.png').convert_alpha()
michelScaled = pygame.transform.scale(michelBase, (55, 80))
player = Player(scrn.get_rect().center, michelScaled)
all_sprites = pygame.sprite.Group([player])

all_barriers = pygame.sprite.Group([barrier1, barrier2])

#background = 
# loop that stops the program when the player quits

pygame.display.flip()
status = True
while (status):
    scrn.fill(0)
    clock.tick(60)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            status = False
    
    #background.update(scrn)
    #background.draw(scrn)    

    all_sprites.update(scrn)
    all_sprites.draw(scrn)

    all_barriers.update(scrn)
    all_barriers.draw(scrn)

    pygame.display.flip()

# deactivates the pygame library
pygame.quit()

