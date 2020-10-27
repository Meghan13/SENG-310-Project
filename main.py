import pygame

#Create the screen
from Code import item
from Code import inventory as inv
from Code import button
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
clock.tick(15)

running = True
player = pygame.Rect((100, 100), (100, 100))
player_inventory = inv.Inventory(49, (400, 10), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))
but = button.Button(20, 100, (10, 10), "Hello world")
# rect2 = pygame.Rect((150, 150), (100, 100))

right = False
left = False
up = False
down = False

# item1 = item.Item(0, "Name", "This is an item", 20, (10, 10), "/Assets/temp.png")
player_inventory.open()

while running:
    # rect2 = item1.get_rect()d
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # since the button was click, check if hovering
            if but.hover(pygame.mouse.get_pos(), True):
                print("Hello")
        # Check if key was pressed
        if event.type == pygame.KEYDOWN:
            # Check direction
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
    if right and rect1.right < 800:
        rect1.x = rect1.x + 1
    if left and rect1.left > 0:
        rect1.x = rect1.x - 1
    if down and rect1.bottom < 600:
        rect1.y = rect1.y + 1
    if up and rect1.top > 0:
        rect1.y = rect1.y - 1

    screen.fill(pygame.Color(0, 0, 0))
    player_inventory.draw(screen)
    but.hover(pygame.mouse.get_pos(), False)
    but.display(screen)
    # pygame.draw.rect(screen, pygame.Color(100, 0, 0), rect2)
    pygame.display.update()
