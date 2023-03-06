#global variables 
fps = 60
projectileColor = (255, 0, 0)
playerSpeed = 5
projectileSpeed = 10

# import pygame, then create projectile and game sprite groups
import pygame

game_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

# screen size and tick system
pygame.init()

screen = pygame.display.set_mode((800, 800))

clock = pygame.time.Clock()




# projectile classification
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
    
    def __init__(self, position, image):
        super().__init__() 
        self.image = image
        self.rect = self.image.get_rect(center = (400,650))

    # player movement
    def update(self, surf):
        # if player presses d, move 5 pixels to the right, and if they press a, move 5 pixels to the left
        keys = pygame.key.get_pressed()
        self.rect.x += (keys[pygame.K_d]-keys[pygame.K_a]) * (playerSpeed) 

        # if player attempts to move off the screen, pull them back to the edge
        self.rect.clamp_ip(surf.get_rect())

    # fire projectile
    def fire(self):
        # set position of projectile relative to player's object rect for centerx and top
        projectile = Projectile(self.rect.centerx, self.rect.top)
        
        game_sprites.add(projectile)

        # add each projectile to sprite group for all projectiles
        projectiles.add(projectile)

# sprite base image
micheal = pygame.image.load('Michael.png').convert_alpha()
micheal = pygame.transform.scale(micheal, (55, 80))

player = Player(screen.get_rect().center, micheal)

controlledPlayer = pygame.sprite.Group([player])


# repeat until player quits
run = True

while run:
    # begin new frame 
    clock.tick(fps)

    for event in pygame.event.get():
        # if player quits, stop program
        if event.type == pygame.QUIT:
            run = False

        # if space is pressed, fire a projectile
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()

    # update screen at the end of each frame
    controlledPlayer.update(screen)
    projectiles.update()

    screen.fill(0)

    projectiles.draw(screen)
    controlledPlayer.draw(screen)

    pygame.display.flip()


# when loop ends, end program
pygame.quit()
exit()
