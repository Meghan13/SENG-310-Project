import pygame
import item
import math
from searchBar import SearchBar


class Inventory:
    # Global size for all item rects
    cell_size = (48, 48)
    # Global padding between inventory cells
    cell_padding = 4

    def __init__(self, capacity: int, def_pos: tuple, def_cells_per_row: int, color: pygame.Color, cell_color: pygame.Color):
        # The inventory's contents (a list of items)
        self.contents = [None] * capacity
        # Maximum number of items the inventory can hold
        self.capacity = capacity

        # Default position of the UI in pixels
        self.def_pos = def_pos
        # Default width of the inventory in item cells
        self.def_cells_per_row = def_cells_per_row

        # Colours of inventory rect and small grid rects respectively
        self.color = color
        self.cell_color = cell_color

        # Apply defaults (defaults are used if these params are not specified by in the open() function
        self.pos = def_pos
        self.cells_per_row = def_cells_per_row
        self.rect = pygame.Rect(self.pos, self.get_size())

        self.search_bar = SearchBar(new_bar_pos = (def_pos[0], def_pos[1]-30))

        # Inventory menu is initialized to a "closed" state
        self.is_open = False

    # Getters & setters

    def get_contents(self):
        return self.contents

    def get_capacity(self):
        return self.capacity

    def get_pos(self):
        return self.pos

    def get_size(self):
        width = (self.cell_size[0] + self.cell_padding) * self.cells_per_row + self.cell_padding
        height = (self.cell_size[1] + self.cell_padding) * math.ceil(self.capacity / float(self.cells_per_row)) + self.cell_padding
        return (width, height)

    # Inventory manipulation

    def take_item(self, screen_pos: tuple):
        if isOpen:
            i = self.pos_to_index(screen_pos)
            if i is not None:
                return self.take_item(i)
        return None

    def take_item(self, index: int):
        return self.place_item(None, index)

    def place_item(self, item: item.Item, screen_pos: tuple):
        if isOpen:
            i = self.pos_to_index(screen_pos)
            if i is not None:
                return self.place_item(item, i)
        return None

    def place_item(self, item: item.Item, index: int):
        taken = self.contents[index]
        self.contents[index] = item
        return taken

    def append_item(self, item: item.Item):
        for i in range(0, self.capacity):
            if self.contents[i] is None:
                self.contents[i] = item
                break

    # Main Interface

    def menu_update(self, event):
        search_string = self.search_bar.user_search_text
        self.search_bar.update(event)
        if search_string != self.search_bar.user_search_text:
            self.search_items(self.search_bar.user_search_text)


    def items_update(self, event, cursor_item):
        if (event.type == pygame.MOUSEBUTTONDOWN and cursor_item is None) or (event.type == pygame.MOUSEBUTTONUP and cursor_item is not None):
            i = self.pos_to_index(event.pos)
            if i is not None:
                return self.place_item(cursor_item, i)

        return cursor_item

    def open(self, pos = None, cells_per_row = None):
        if pos is None:
            pos = self.def_pos
        if cells_per_row is None:
            cells_per_row = self.def_cells_per_row

        self.pos = pos
        self.cells_per_row = cells_per_row
        self.rect = pygame.Rect(self.pos, self.get_size())
        self.is_open = True

    def close(self):
        self.is_open = False

    def draw(self, screen: pygame.display):
        pygame.draw.rect(screen, self.color, self.rect)

        for i in range(0, self.capacity):
            cell_pos = self.index_to_pos(i)
            # Draw cell background
            pygame.draw.rect(screen, self.cell_color, pygame.Rect(cell_pos, self.cell_size))

            # If cell is not empty, draw contained item
            if self.contents[i] is not None:
                self.contents[i].set_pos(cell_pos)
                self.contents[i].display(screen)

        #Draw toolbar
        self.search_bar.draw(screen)

    # Utility

    def pos_to_index(self, pos: tuple):
        rel_pos = (pos[0] - self.pos[0], pos[1] - self.pos[1])
        size = self.get_size()

        if rel_pos[0] < 0 or rel_pos[0] > size[0] or rel_pos[1] < 0 or rel_pos[1] > size[1]:
            return None

        x = int((rel_pos[0] + float(self.cell_padding)/2) / (self.cell_size[0] + self.cell_padding))
        y = int((rel_pos[1] + float(self.cell_padding)/2) / (self.cell_size[1] + self.cell_padding))
        i = x + (y * self.cells_per_row)

        if i < self.capacity:
            return int(i)
        else:
            return None

    def index_to_pos(self, index: int):
        x = self.pos[0] + (index % self.cells_per_row) * (self.cell_size[0] + self.cell_padding) + self.cell_padding
        y = self.pos[1] + int(index / self.cells_per_row) * (self.cell_size[1] + self.cell_padding) + self.cell_padding
        return (x, y)

    # Use searchBar and inventory to find items from user input and highlights them
    def search_items(self, search_term):
        print('Search term: '+ search_term)
        if search_term == '':
            self.unhighlight_all_items()
            return

        for i in self.contents:
            if i is not None:
                i.set_highlight(True)
                if search_term.lower() in i.get_name().lower():
                    i.set_highlight_color(pygame.Color(255, 255, 0))
                    i.highlight_sort = True
                else:
                    i.set_highlight_color(pygame.Color(100, 100, 100))
                    i.highlight_sort = False

    def unhighlight_all_items(self):
        for i in self.contents:
            if i is not None:
                i.set_highlight(False)
                i.highlight_sort = False




