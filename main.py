import pygame
from item import Item
from inventory import Inventory as Inv
from button import Button


# MAIN PROPS -------------------------------------------------------------------------------

WIDTH = 1600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
clock.tick(15)

# If script is running
running = True
# If any inventory menus are open
inventory_menu_open = False

# Replace with Player class when complete
player = pygame.Rect((100, 100), (100, 100))

player_inventory = Inv(49, (400, 40), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))

# List of all chests
chests = []

# Chest opened this frame, if any
new_opened_chest = None


# FUNCTION DEFS ----------------------------------------------------------------------------

# Given a position and size, creates and return a new (button, inv) tuple representing a chest
def create_chest(pos, size, label):
    inv = Inv(21, (10, 40), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))
    btn = Button(size[0], size[1], pos, label, pygame.Color(139, 82, 45))
    return (btn, inv)


# SCENE POPULATION -------------------------------------------------------------------------

for i in range(0,4):
    pos = (10 + i*25, 10)
    size = (20, 20)
    chests.append(create_chest(pos, size, str(i+1)))

item1 = Item(0, "weapon", "Hello", "This is a test", 10, (10, 10), "./Assets/sword.png")
item1.set_highlight_color(pygame.Color(100, 100, 100))

item2 = Item(1, "weapon", "Goodbye", "This is a test", 10, (10, 10), "./Assets/sword.png")
item2.set_highlight(True)

chests[0][1].place_item(item1, 0)
chests[1][1].place_item(item2, 1)


# MASTER LOOP ------------------------------------------------------------------------------

while running:
    # Handle each event this frame
    for event in pygame.event.get():

        # Handle game window being closed
        if event.type == pygame.QUIT:
            pygame.quit()

        # Handle player movement
        # player.update(event)

        # Handle a chest being opened
        new_opened_chest = None
        if event.type == pygame.MOUSEBUTTONUP:
            for chest in chests:
                #If chest is clicked
                if chest[0].hover(pygame.mouse.get_pos(), True):
                    new_opened_chest = chest
                    break

        # Handle the inventory button being pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:









        # Inventory button pressed

                if player_inventory.isOpen:
                    player_inventory.close()
                    opened_chest = None
                else:
                    player_inventory.open()

        # Mouse button pressed
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for i in chests:
                    if i[0].hover(pygame.mouse.get_pos(), True):
                        if i == opened_chest:
                            opened_chest = None
                        else:
                            opened_chest = i

    # Draw background
    screen.fill(pygame.Color(0, 0, 0))

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


