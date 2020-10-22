import pygame

#Intialize the pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

running = True
rect1 = pygame.Rect((100, 100),(100, 100))
rect2 = pygame.Rect((100, 100),(100, 200))



while running:
    pygame.draw.rect(screen, pygame.Color(100, 100, 100), rect1)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False