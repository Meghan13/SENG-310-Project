import pygame

#Intialize the pygame
pygame.init()

#Create the screen

#Ben M
#2020-10-23

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
clock.tick(15)

running = True
player = pygame.Rect((100, 100), (100, 100))
chest1 = pygame.Rect((250, 250), (100, 100))

chest2 = pygame.Rect((500, 500), (100, 100))
inventoryPane = pygame.Rect((20, 20), (200, 200))
inventoryPane2 = pygame.Rect((20, 240), (200, 200))

inventoryOpen = False


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
            if event.key == pygame.K_e and inventoryOpen is False:
                inventoryOpen = True
            elif event.key == pygame.K_e:
                inventoryOpen = False
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
    if right and player.right < 800:
        player.x = player.x + 1
    if left and player.left > 0:
        player.x = player.x - 1
    if down and player.bottom < 600:
        player.y = player.y + 1
    if up and player.top > 0:
        player.y = player.y - 1
    screen.fill(pygame.Color(0, 0, 0))
    pygame.draw.rect(screen, pygame.Color(100, 0, 0), player)
    pygame.draw.rect(screen, pygame.Color(100, 20, 30), chest1)
    pygame.draw.rect(screen, pygame.Color(200, 30, 4), chest2)
    if inventoryOpen:
        if ((player.y - chest1.y)**2 + (player.x - chest1.x)**2) < 100000:
            pygame.draw.rect(screen, pygame.Color(100, 100, 20), inventoryPane)
        if ((player.y - chest2.y) ** 2 + (player.x - chest2.x) ** 2) < 100000:
            pygame.draw.rect(screen, pygame.Color(100, 100, 20), inventoryPane2)
    pygame.display.update()
