import pygame
from Code import item
import math


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

        # Inventory menu is initialized to a "closed" state
        self.isOpen = False

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

    # Visual

    def open(self, pos = None, cells_per_row = None):
        if pos is None:
            pos = self.def_pos
        if cells_per_row is None:
            cells_per_row = self.def_cells_per_row

        self.pos = pos
        self.cells_per_row = cells_per_row
        self.rect = pygame.Rect(self.pos, self.get_size())
        self.isOpen = True

    def close(self):
        self.isOpen = False

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

    # Utility

    def pos_to_index(self, pos: tuple):
        rel_pos = (pos[0] - self.pos[0], pos[1] - self.pos[1])
        size = self.get_size

        if rel_pos[0] < 0 or rel_pos[0] > size[0] or rel_pos[1] < 0 or rel_pos[1] > size[1]:
            return None

        x = (rel_pos[0] + float(cellPadding) / 2) / (self.cell_size[0] + self.cell_padding)
        y = (rel_pos[1] + float(cellPadding) / 2) / (self.cell_size[1] + self.cell_padding)
        i = x + (y * self.cells_per_row)

        if i < self.capacity:
            return i
        else:
            return None

    def index_to_pos(self, index: int):
        x = self.pos[0] + (index % self.cells_per_row) * (self.cell_size[0] + self.cell_padding) + self.cell_padding
        y = self.pos[1] + int(index / self.cells_per_row) * (self.cell_size[1] + self.cell_padding) + self.cell_padding
        return (x, y)

    # Main Interface

    #def menu_update(self, event):
        # Pass events to menu bar here

    def items_update(self, event, cursor_item):
        if event.type == pygame.MOUSEBUTTONUP:
            i = self.pos_to_index(event.pos)
            if i is not None:
                return self.place_item(cursor_item, i)

        return cursor_item


