import pygame
import item
import math
from toolbar import Toolbar
import sortingStuff as sort

class Inventory:
    # Global size for all item rects
    cell_size = (64, 64)
    # Global padding between inventory cells
    cell_padding = 4

    def __init__(self, capacity: int, def_pos: tuple, def_cells_per_row: int, color: pygame.Color, cell_color: pygame.Color, name: str, chest_button=None):
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

        #self.search_bar = SearchBar(new_bar_pos = (def_pos[0], def_pos[1]-30))
        self.tool_bar = Toolbar(self.rect.width, self.rect.topleft, pygame.Color(100, 100, 100), color)
        self.tool_bar.set_name(name)

        # A reference to the chest this inventory is bound to, if any
        self.chest_button = chest_button

        self.is_pinned = False
        # Inventory menu is initialized to a "closed" state
        self.is_open = False

    # Getters & setters

    def get_contents(self):
        return self.contents

    def get_capacity(self):
        return self.capacity

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        prev_pos = self.pos
        self.pos = pos
        delta = (pos[0] - prev_pos[0], pos[1] - prev_pos[1])
        self.rect.move_ip(delta)
        self.tool_bar.move_by(delta)

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
        if self.contents[index] is not None and item is not None and self.contents[index].get_id() == item.get_id():
            total_num = item.num + self.contents[index].num
            if total_num <= item.max_stack:
                self.contents[index].set_num(total_num)
                taken = None
            else:
                item.set_num(total_num - item.max_stack)
                self.contents[index].set_num(item.max_stack)
                taken = item

        else:
            taken = self.contents[index]
            self.contents[index] = item

        return taken

    def append_item(self, item: item.Item):
        if item is None:
            return

        for i in range(0, self.capacity):
            if (self.contents[i] is None) or (self.contents[i].get_id() == item.get_id() and self.contents[i].num < item.max_stack):
                remaining = self.place_item(item, i)
                if remaining is not None:
                    self.append_item(remaining)
                return

    # Main Interface

    def menu_update(self, event):
        # Update returns the number of the button that was pressed, set that to a number that we can use
        sort_num = self.tool_bar.update(event)

        # Yandere Dev let's GOOOOOOOOOOO!
        if sort_num == 0:
            print(len(self.contents))
            sorted = sort.sort_by_id(self.contents)
        elif sort_num == 1:
            sorted = sort.sort_by_name(self.contents)
        elif sort_num == 2:
            sorted = sort.sort_by_type(self.contents)
        elif sort_num == 3:
            sorted = sort.sort_by_number(self.contents)
            self.contents = sorted
            return
        elif sort_num == 4:
            sorted = sort.sort_by_highlight(self.contents)
        else:
            return

        self.contents = [None] * self.capacity
        for i in sorted:
            self.append_item(i)



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

        self.set_pos(pos)
        self.cells_per_row = cells_per_row
        self.rect = pygame.Rect(self.pos, self.get_size())
        self.is_open = True
        self.tool_bar.set_active(True)

    def close(self):
        self.tool_bar.set_active(False)
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

        for i in range(0, self.capacity):
            # Display amount of items and description
            if self.contents[i] is not None:
                self.contents[i].description(screen, pygame.mouse.get_pos())

        # Draw toolbar and get text from  text_input
        self.tool_bar.display(screen)
        self.search_items(self.tool_bar.get_text())

        #if self.is_pinned:
        #   corners =



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
        #print('Search term: ' + search_term)
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




