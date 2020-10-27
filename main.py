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

item1 = item.Item(0, "Hello", "This is a test", 10, (10, 10), "./Assets/sword.png")
item2 = item.Item(1, "Goodbye", "This is a test", 10, (10, 10), "./Assets/sword.png")
player_inventory.place_item(item1, 0)
player_inventory.place_item(item2, 1)
item1.set_highlight(True)

player_inventory.open()

while running:
    screen.fill(pygame.Color(0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        but.update(event)
    but.display(screen)
    # pygame.draw.rect(screen, pygame.Color(100, 0, 0), rect2)
    pygame.display.update()
