import pygame
from item import Item
import random
import itemUtil as item_util
from inventory import Inventory as Inv
from button import Button
from player import Player


# MAIN PROPS -------------------------------------------------------------------------------

WIDTH = 1600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# If script is running
running = True

# The player and their inventory
player = Player((WIDTH, HEIGHT))
player_inventory = Inv(49, (1000, 70), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))

# List of all chests
chests = []

#item_source = Button(100, 100, (750, 400), 'Click for items!', pygame.Color(200, 0, 45))

# If any inventory menus are open
inventory_menu_open = False
# If inventory menu state should change this frame
inventory_menu_toggled = False
# Chest opened this frame, if any
new_opened_chest = None

# Item held by the cursor
cursor_item = None


#Rects for creating the room
floor_rect = pygame.Rect((100, 100), (WIDTH-200, HEIGHT-200))
top_wall = pygame.Rect(floor_rect.topleft, (floor_rect.width, 10))
right_wall = pygame.Rect((floor_rect.topright[0]-10, floor_rect.topright[1]), (10, floor_rect.height))
bottom_wall = pygame.Rect((floor_rect.bottomleft[0], floor_rect.bottomleft[1] - 10), (floor_rect.width, 10))
left_wall = pygame.Rect(floor_rect.topleft, (10, floor_rect.height))

# Button for adding items
item_source = Button(30, 150, (floor_rect.centerx-75, floor_rect.bottom-30), "Go forage", pygame.Color(139, 82, 45))


# test_bar = SearchBar(screen)



# FUNCTION DEFS ----------------------------------------------------------------------------

# Given a position and size, creates and return a new (button, inv) tuple representing a chest
def create_chest(pos, size, label):
    inv = Inv(21, (500, 70), 7, pygame.Color(0, 64, 0), pygame.Color(0, 128, 0))
    btn = Button(size[0], size[1], pos, label, pygame.Color(139, 82, 45))
    return (btn, inv)


# Brutally compiles and returns a list of all open inventories
def open_inventories():
    all_open = [c[1] for c in chests if c[1].is_open]
    if player_inventory.is_open:
        all_open.insert(0, player_inventory)
    return all_open

def give_random_items():
    num_stacks = random.randint(5, 10)
    for i in range(0, num_stacks):
        id = random.randint(0, 9)
        stack_size = random.randint(1, 50)
        player_inventory.append_item(item_util.create_item_by_id(id, stack_size))

def draw_house():
    pygame.draw.rect(screen, pygame.Color(180, 110, 66), floor_rect)
    pygame.draw.rect(screen, pygame.Color(90, 55, 33), top_wall)
    pygame.draw.rect(screen, pygame.Color(90, 55, 33), right_wall)
    pygame.draw.rect(screen, pygame.Color(90, 55, 33), bottom_wall)
    pygame.draw.rect(screen, pygame.Color(90, 55, 33), left_wall)


# SCENE POPULATION -------------------------------------------------------------------------

for i in range(0, 4):
    pos = (120 + i * 110, 120)
    size = (50, 100)
    chests.append(create_chest(pos, size, "Chest " + str(i + 1)))

#item1 = Item(0, "tool", "pickaxe", "This is a test", 10, (10, 10), "./Assets/pickaxe.png")
# item1.set_highlight_color(pygame.Color(100, 100, 100))

#item2 = Item(1, "food", "Apple", "This is a test", 10, (10, 10), "./Assets/apple.png")
# item2.set_highlight(True)

#item3 = Item(1, "food", "Apple", "This is a test", 95, (10, 10), "./Assets/apple.png")

#chests[0][1].place_item(item1, 0)
# chests[0][1].place_item(item2, 1)

for i in range(0, 10):
    chests[0][1].place_item(item_util.create_item_by_id(i, 33), i)


player.rect.x = 150  # go to x
player.rect.y = 150  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
stride = 8


# MASTER LOOP ------------------------------------------------------------------------------

while running:

    events = pygame.event.get()

    # Placate text input module by violating all concept of code architecture
    # Also intercept key events while text is being entered
    textbox_active = False
    if inventory_menu_open:
        for inv in open_inventories():
            if inv.tool_bar.search_bar.text_input_active:
                textbox_active = True

                if len(events) == 0:
                    inv.tool_bar.search_bar.textinput.update([])

    # --- Handle each event this frame ---
    for event in events:



        # Mitigate weird bugs caused by probably implementing this event loop wrong
        if event.type == pygame.MOUSEMOTION:
            continue

        # Handle game window being closed
        if event.type == pygame.QUIT:
            pygame.quit()

        # Handle player movement
        # player.update(event)

        # Handle a chest being opened
        new_opened_chest = None
        if event.type == pygame.MOUSEBUTTONUP:
            for chest in chests:
                # If chest is clicked
                if chest[0].hover(pygame.mouse.get_pos(), True):
                    new_opened_chest = chest
                    break

            # Handle clicking on item source
            if item_source.hover(pygame.mouse.get_pos(), True):
                give_random_items()

        # Handle the inventory button being pressed
        inventory_menu_toggled = False
        if event.type == pygame.KEYDOWN and not textbox_active:
            if event.key == pygame.K_i:
                inventory_menu_toggled = True

            # BenM's code
            # control the player
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-stride, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(stride, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, -stride)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, stride)

        # control the player
        if event.type == pygame.KEYUP and not textbox_active:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(stride, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-stride, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, stride)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, -stride)

        # --- Stuff that only happens when inventories are not open ---
        if not inventory_menu_open:

            # If a chest was clicked or the inventory button pressed,
            # open the appropriate inventories.
            if inventory_menu_toggled or (new_opened_chest is not None):
                inventory_menu_open = True
                player_inventory.open()
                if new_opened_chest:
                    new_opened_chest[1].open()

        # --- Stuff that only happens when inventories are open ---
        else:

            # Handle interactions with open inventories
            for inv in open_inventories():
                inv.menu_update(event)
                cursor_item = inv.items_update(event, cursor_item)

            # If chest is clicked, replace open chest inventory
            if new_opened_chest is not None:
                if new_opened_chest[1] in open_inventories():
                    new_opened_chest[1].close()
                else:
                    if len(open_inventories()) > 1:
                        open_inventories()[1].close()
                    new_opened_chest[1].open()

            # If the inventory menu is closed, close all open inventories and return
            # the cursor item to the player inventory
            if inventory_menu_toggled:
                print('!')
                inventory_menu_open = False

                if cursor_item is not None:
                    player_inventory.append_item(cursor_item)
                    cursor_item = None

                for inv in open_inventories():
                    inv.close()

    # --- Update objects ---

    #if not inventory_menu_open:


    #else:


    # --- Draw objects ---

    # Draw background
    screen.fill(pygame.Color(0, 0, 0))

    # Draw the house
    draw_house()

    # Draw random button
    # Draw chests
    for c in chests:
        c[0].hover(pygame.mouse.get_pos(), False)
        c[0].display(screen)

    # Draw item source
    item_source.display(screen)
    item_source.hover(pygame.mouse.get_pos(), False)
    # Draw player
    player.update()
    player_list.draw(screen)

    # Draw open inventories
    for inv in open_inventories():
        inv.draw(screen)

    # Draw cursor item
    if cursor_item:
        cursor_item.set_pos(pygame.mouse.get_pos())
        cursor_item.display(screen)

    pygame.display.update()
    clock.tick(60)


