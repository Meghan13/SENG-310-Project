import pygame
from searchBar import SearchBar
from button import Button


class Toolbar:
    WIDTH = None            # Width of the toolbar
    HEIGHT = 40             # Height of the toolbar
    BUTTON_WIDTH = 100      # Width of the buttons
    BUTTON_HEIGHT = 30      # Height of the buttons
    but_color = None        # Color of the buttons
    search_bar = None       # Search bar
    buttons = []            # List of buttons
    by_id = None            # Button for sorting by id
    by_name = None          # Button for sorting by name
    by_type = None          # Button for sorting by type
    by_num = None           # Button for sorting by number
    by_highlight = None     # Button for sorting by highlighted search items
    draw_rect = None        # The rect to draw under the buttons
    is_active = False       # Represents whether or not the toolbar is active or not

    def __init__(self, new_width: int, inv_pos: tuple, new_color: pygame.Color, new_but_color: pygame.Color):
        # Make sure the list of buttons is unique to each inventory
        self.buttons = []

        # set the color of the buttons and the rect for displaying behind the buttons
        self.but_color = new_color
        self.draw_rect = pygame.Rect((inv_pos[0], inv_pos[1] - self.HEIGHT), (new_width, self.HEIGHT))

        # base the size of the buttons on the width of the inventory
        but_width = new_width/8

        # Create the buttons relative to the inventory
        self.by_id = Button(self.BUTTON_HEIGHT, int(but_width), (self.draw_rect.topleft[0] + 5, self.draw_rect.topleft[1]+5), "Sort", new_but_color)
        self.by_name = Button(self.BUTTON_HEIGHT, int(but_width), (self.draw_rect.topleft[0] + but_width + 10, self.draw_rect.topleft[1]+5), "A-Z", new_but_color)
        self.by_type = Button(self.BUTTON_HEIGHT, int(but_width), (self.draw_rect.topleft[0] + 2 * but_width + 15, self.draw_rect.topleft[1]+5), "Type", new_but_color)
        self.by_num = Button(self.BUTTON_HEIGHT, int(but_width), (self.draw_rect.topleft[0] + 3 * but_width + 20, self.draw_rect.topleft[1]+5), "Amount", new_but_color)
        self.by_highlight = Button(self.BUTTON_HEIGHT, int(but_width), (self.draw_rect.topleft[0] + 4 * but_width + 25, self.draw_rect.topleft[1]+5), "Highlight", new_but_color)

        # ADd them all to a list for ease of use
        self.buttons.append(self.by_id)
        self.buttons.append(self.by_name)
        self.buttons.append(self.by_type)
        self.buttons.append(self.by_num)
        self.buttons.append(self.by_highlight)

        # Create a search bar
        self.search_bar = SearchBar(pygame.Color(0, 0, 0), (self.draw_rect.midleft[0] + 5 * but_width + 30, self.draw_rect.topleft[1]+5),
                                    but_width*2, self.BUTTON_HEIGHT, (self.draw_rect.midleft[0] + 5 * but_width + 15 + but_width*2, self.draw_rect.topleft[1]+5),
                                    30, 30)

    def update(self, event):
        # Update the search bar
        self.search_bar.update(event)
        # set an counter integer to 0
        num = 0
        # If mouse button was pressed, check which button was pressed and return the number of that button (0-4)
        if event.type == pygame.MOUSEBUTTONUP:
            for i in self.buttons:
                if i.hover(pygame.mouse.get_pos(), True):
                    if self.is_active:
                        return num
                num = num + 1

    def get_text(self):
        return self.search_bar.user_search_text

    def set_active(self, active: bool):
        self.is_active = active

    def display(self, screen):
        # If the toolbar is active, draw everything
        if self.is_active:
            pygame.draw.rect(screen, self.but_color, self.draw_rect)
            for but in self.buttons:
                but.hover(pygame.mouse.get_pos(), False)
                but.display(screen)
            self.search_bar.draw(screen)
