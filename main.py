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

but1 = button.Button(20, 20, (10, 10), "1", pygame.Color(139, 82, 45))
but2 = button.Button(20, 20, (35, 10), "2", pygame.Color(139, 82, 45))
but3 = button.Button(20, 20, (60, 10), "3", pygame.Color(139, 82, 45))
but4 = button.Button(20, 20, (85, 10), "4", pygame.Color(139, 82, 45))

chest1 = inv.Inventory(49, (400, 10), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))
chest2 = inv.Inventory(49, (400, 10), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))
chest3 = inv.Inventory(49, (400, 10), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))
chest4 = inv.Inventory(49, (400, 10), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))
chests = [(but1, chest1), (but2, chest2), (but3, chest3), (but4, chest4)]

opened_chest = None

item1 = item.Item(0, "Hello", "This is a test", 10, (10, 10), "./Assets/sword.png")
item2 = item.Item(1, "Goodbye", "This is a test", 10, (10, 10), "./Assets/sword.png")
chests[0][1].place_item(item1, 0)
chests[1][1].place_item(item1, 1)
chests[2][1].place_item(item1, 2)
chests[3][1].place_item(item1, 3)


while running:
    screen.fill(pygame.Color(0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in chests:
                    if i[0].hover(pygame.mouse.get_pos(), True):
                        opened_chest = i

    for i in chests:
        i[0].hover(pygame.mouse.get_pos(), False)
        i[0].display(screen)
    if opened_chest:
        opened_chest[1].draw(screen)
    pygame.display.update()
