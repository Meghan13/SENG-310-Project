import pygame
from Code import item
from Code import inventory as inv
from Code import button

WIDTH = 1600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
clock.tick(15)

running = True
player = pygame.Rect((100, 100), (100, 100))
player_inventory = inv.Inventory(49, (400, 40), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))

but1 = button.Button(20, 20, (10, 10), "1", pygame.Color(139, 82, 45))
but2 = button.Button(20, 20, (35, 10), "2", pygame.Color(139, 82, 45))
but3 = button.Button(20, 20, (60, 10), "3", pygame.Color(139, 82, 45))
but4 = button.Button(20, 20, (85, 10), "4", pygame.Color(139, 82, 45))

chest1 = inv.Inventory(21, (10, 40), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))
chest2 = inv.Inventory(21, (10, 40), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))
chest3 = inv.Inventory(21, (10, 40), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))
chest4 = inv.Inventory(21, (10, 40), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))
chests = [(but1, chest1), (but2, chest2), (but3, chest3), (but4, chest4)]

opened_chest = None
item1 = item.Item(0, "weapon", "Hello", "This is a test", 10, (10, 10), "./Assets/sword.png")
item1.set_highlight_color(pygame.Color(100, 100, 100))

item2 = item.Item(1, "weapon", "Goodbye", "This is a test", 10, (10, 10), "./Assets/sword.png")
item2.set_highlight(True)

chests[0][1].place_item(item1, 0)
chests[1][1].place_item(item2, 1)

while running:
    screen.fill(pygame.Color(0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                if player_inventory.isOpen:
                    player_inventory.close()
                    opened_chest = None
                else:
                    player_inventory.open()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in chests:
                    if i[0].hover(pygame.mouse.get_pos(), True):
                        if i == opened_chest:
                            opened_chest = None
                        else:
                            opened_chest = i

    for i in chests:
        i[0].hover(pygame.mouse.get_pos(), False)
        i[0].display(screen)
    if opened_chest:
        opened_chest[1].draw(screen)
        if not player_inventory.isOpen:
            player_inventory.open()
    if player_inventory.isOpen:
        player_inventory.draw(screen)
    pygame.display.update()
