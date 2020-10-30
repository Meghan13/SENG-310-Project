from typing import Tuple

import pygame
import sys
import os

from Code.inventory import Inventory

"""
    HactuallyBenji
    https://opensource.com/article/17/12/game-python-moving-player
"""

worldx = 960
worldy = 720
fps = 40
animation = 4
world = pygame.display.set_mode([worldx, worldy])

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []

        #found this if we need more than one player
        for i in range(1, 5):
            img = pygame.image.load('../Assets/character.png')
            #img.convert_alpha()  # optimise alpha
            #img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):

        self.movex += x
        self.movey += y

    def update(self):

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*animation:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // animation], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*animation:
                self.frame = 0
            self.image = self.images[self.frame//animation]

    """
        Check to see if the player is in range of chest.
        Returns boolean value for whether or not inventory should be accessible
    """
    def is_in_player_range(self, inventory: Inventory, desired_range: int):
        return ((self.rect.x - inventory.rect.x)**2 + (self.rect.y - inventory.rect.y)**2) < desired_range**2



backdrop = pygame.image.load('../Assets/backdrop.jpg')
backdrop_alt = pygame.image.load('../Assets/backdrop_alt.jpg')

clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

player = Player()  # spawn player
player.rect.x = 150  # go to x
player.rect.y = 150  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
stride = 10


while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-stride, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(stride, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, -stride)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, stride)
            if event.key == pygame.K_SPACE:
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(stride, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-stride, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, stride)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, -stride)

    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)
