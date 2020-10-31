import pygame
from searchBar import SearchBar
from button import Button


class Toolbar:
    WIDTH = None
    HEIGHT = 40
    BUTTON_HEIGHT = 30
    BUTTON_WIDTH = 100
    but_color = None
    search_bar = None
    sort_button = None
    buttons = []
    by_id = None
    by_name = None
    by_type = None
    by_num = None
    by_highlight = None
    draw_rect = None

    def __init__(self, new_width: int, inv_pos: tuple, new_color: pygame.Color, new_but_color: pygame.Color):
        self.but_color = new_color
        self.draw_rect = pygame.Rect((inv_pos[0], inv_pos[1] - self.HEIGHT), (new_width, self.HEIGHT))
        # Create the buttons relative to the inventory
        self.by_id = Button(self.BUTTON_HEIGHT, int(new_width / 6), (self.draw_rect.topleft[0] + 5, self.draw_rect.topleft[1]+5), "by_id", new_but_color)
        self.by_name = Button(self.BUTTON_HEIGHT, int(new_width / 6), (self.draw_rect.topleft[0] + (new_width / 6) + 10, self.draw_rect.topleft[1]+5), "by_name", new_but_color)
        self.by_type = Button(self.BUTTON_HEIGHT, int(new_width / 6), (self.draw_rect.topleft[0] + 2 * (new_width / 6) + 15, self.draw_rect.topleft[1]+5), "by_name", new_but_color)
        self.by_num = Button(self.BUTTON_HEIGHT, int(new_width / 6), (self.draw_rect.topleft[0] + 3 * (new_width / 6) + 20, self.draw_rect.topleft[1]+5), "by_num", new_but_color)
        self.by_highlight = Button(self.BUTTON_HEIGHT, int(new_width / 6), (self.draw_rect.topleft[0] + 4 * (new_width / 6) + 25, self.draw_rect.topleft[1]+5), "by_num", new_but_color)
        # ADd them all to a list for ease of use
        self.buttons.append(self.by_id)
        self.buttons.append(self.by_name)
        self.buttons.append(self.by_type)
        self.buttons.append(self.by_num)
        self.buttons.append(self.by_highlight)
        # Create a search bar
        self.search_bar = SearchBar(pygame.Color(0, 0, 0), (self.draw_rect.midleft[0] + 5 * (new_width / 6) + 30, self.draw_rect.topleft[1]+5),
                                    self.BUTTON_WIDTH*2, self.BUTTON_HEIGHT, (self.draw_rect.midleft[0] + 5 * (new_width / 6) + 15 + self.BUTTON_WIDTH*2, self.draw_rect.topleft[1]+5),
                                    30, 30)

    def update(self, event):
        self.search_bar.update(event)
        num = 0

        if event.type == pygame.MOUSEBUTTONUP:
            for i in self.buttons:
                if i.hover(pygame.mouse.get_pos(), True):
                    return num
                num = num + 1

    def get_text(self):
        return self.search_bar.user_search_text

    def display(self, screen):
        pygame.draw.rect(screen, self.but_color, self.draw_rect)
        for but in self.buttons:
            but.hover(pygame.mouse.get_pos(), False)
            but.display(screen)
        self.search_bar.draw(screen)
