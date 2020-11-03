from typing import Tuple

import pygame
import sys
import os
import math

from inventory import Inventory

"""
    HactuallyBenji
    https://opensource.com/article/17/12/game-python-moving-player
"""


class Player(pygame.sprite.Sprite):

    def __init__(self, bounds):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 1
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        self.animation = 4
        self.sprite_scale = (150, 175)
        self.bounds = (bounds[0] - self.sprite_scale[0], bounds[1] - self.sprite_scale[1])

        #found this if we need more than one player
        for i in range(1, 5):
            img = pygame.image.load('Assets/player_right.png')
            #img.convert_alpha()  # optimise alpha
            #img.set_colorkey(ALPHA)  # set alpha
            img = pygame.transform.scale(img, self.sprite_scale)
            self.images.append(img)
            self.image = self.images[0]

            self.rect = self.image.get_rect()


    # Player movement control
    def control(self, x, y):
        self.movex += x
        self.movey += y

    # Update player position and direction
    def update(self):
        self.rect.x = min(max(self.rect.x + self.movex*self.speed, 110), self.bounds[0]-110)
        self.rect.y = min(max(self.rect.y + self.movey*self.speed, 110), self.bounds[1]-110)

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*self.animation:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // self.animation], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*self.animation:
                self.frame = 0
            self.image = self.images[self.frame//self.animation]

    """
    # Check to see if the player is in range of chest.
    # Returns boolean value for whether or not inventory should be accessible
    """
    def is_chest_in_player_range(self, inventory: Inventory, desired_range: int):
        if not inventory.chest_button:
            return False

        return ((self.rect.centerx - inventory.chest_button.rect.centerx)**2 + (self.rect.centery - inventory.chest_button.rect.centery)**2) < desired_range**2

    """
        Returns distance from player to specified chest
    """
    def distance_from_chest(self, chest: Inventory):
        if chest.chest_button:
            return math.sqrt((self.rect.centerx - chest.chest_button.rect.centerx)**2 + (self.rect.centery - chest.chest_button.rect.centery)**2)

    """
       Finds the nearest chest from a list of chests passed in 
    """
    def get_nearest_chest(self, chests: list):
        closest = self.distance_from_chest(chests[0])
        closest_chest = chests[0]
        for chest in chests:
            if self.distance_from_chest(chest) < closest:
                closest = self.distance_from_chest(chest)
                closest_chest = chest
        return closest_chest
