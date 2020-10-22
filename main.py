import pygame

#Intialize the pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

running = True
rect1 = pygame.Rect((100, 100),(100, 100))
rect2 = pygame.Rect((150, 150),(100, 100))

right = False
left = False
up = False
down = False

while running:
    for event in pygame.event.get():
        #Check if key was pressed
        if event.type == pygame.KEYDOWN:
            #Check direction
            if event.key == pygame.K_d:
                right = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_s:
                down = True
        if event.type == pygame.KEYUP:
            # Check direction
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_s:
                down = False
        if event.type == pygame.QUIT:
            running = False
    if right:
        rect1.x = rect1.x + 1
    if left:
        rect1.x = rect1.x - 1
    if down:
        rect1.y = rect1.y + 1
    if up:
        rect1.y = rect1.y - 1
    screen.fill(pygame.Color(0, 0, 0))
    pygame.draw.rect(screen, pygame.Color(100, 0, 0), rect1)
    pygame.display.update()