import pygame
from enum import Enum
# Initialize the pygame
pygame.init()


class Item:
    def __init__(self, item_id: int, item_type: str, item_name: str, item_info: str, item_num: int, item_pos: tuple, image_dir: str, max_stack=99):
        self.i_id = item_id
        self.type = item_type
        self.name = item_name
        self.info = item_info
        self.num = item_num
        self.pos = item_pos
        self.rect = pygame.Rect(self.pos, (self.WIDTH, self.HEIGHT))
        self.image = pygame.image.load(image_dir)
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.max_stack = max_stack

    def get_id(self):
        return self.i_id

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_info(self):
        return self.info

    def get_num(self):
        return self.num

    def get_max_stack(self):
        return self.max_stack

    def get_pos(self):
        return self.pos

    def get_rect(self):
        return self.rect

    def get_image(self):
        return self.image

    def get_width(self):
        return self.WIDTH

    def get_height(self):
        return self.HEIGHT

    def get_highlight(self):
        return self.is_highlighted

    def set_id(self, item_id: int):
        self.i_id = item_id

    def set_type(self, new_type: str):
        self.type = new_type

    def set_name(self, item_name: str):
        self.name = item_name

    def set_info(self, item_info: str):
        self.info = item_info

    def set_num(self, item_num: int):
        self.num = item_num

    def set_max_stack(self, new_max: int):
        self.max_stack = new_max

    def set_pos(self, item_pos: tuple):
        self.pos = item_pos
        self.rect = pygame.Rect(self.pos, (self.WIDTH, self.HEIGHT))

    def set_highlight(self, highlight_bool: bool):
        self.is_highlighted = highlight_bool

    def set_highlight_color(self, new_color: pygame.Color):
        self.highlight_color = new_color

    # This function takes in a screen and displays the items image at that coordinate
    def display(self, screen: pygame.display):
        screen.blit(self.image, self.pos)
        s = pygame.Surface((self.rect.width, self.rect.height))
        if self.is_highlighted:
            s.set_alpha(100)
        else:
            s.set_alpha(0)

        s.fill(self.highlight_color)
        screen.blit(s, self.rect.topleft)

    # This function displays the item description to the screen just above the cursor
    def description(self, screen: pygame.display, m_pos: tuple):
        # Check to see if mouse is over (second variable not used yet)
        if self.hover(m_pos, False):
            # create a text object based on our global item font
            text = self.font.render("id:"+str(self.i_id)+"   "+self.info, True, pygame.Color(255, 255, 255))
            # display text
            screen.blit(text, (m_pos[0], m_pos[1] - 10))
        # reset the text to be the number of items
        text = self.font.render(str(self.num), True, pygame.Color(255, 255, 255))
        # display the number of items
        screen.blit(text, (self.rect.midbottom[0]-5, self.rect.midbottom[1]-10))

    # This function checks to see whether or not the mouse is hovering over
    # an items rect
    def hover(self, m_pos: tuple, click: bool):
        # compare the coordinates of the mouse and the items rect
        return self.rect.left < m_pos[0] < self.rect.right and self.rect.top < m_pos[1] < self.rect.bottom

    # Scales an item rect and image separately in x and y
    def scale(self, x_scale: float, y_scale: float):
        self.WIDTH = int(self.WIDTH * x_scale)
        self.HEIGHT = int(self.HEIGHT * y_scale)
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))

    font = pygame.font.Font("freesansbold.ttf", 12)  # change this to change font and font size
    i_id = None   # unique item id
    type = None   # item type
    name = None   # item name
    info = None   # item description
    num = None    # amount of an item
    pos = None    # position for the item and rect
    rect = None   # item rect for collisions/hover detection
    image = None  # a string which stores the location of the image for an item
    max_stack = 99
    is_highlighted = False
    highlight_sort = False
    highlight_color = pygame.color.Color(255, 255, 0)

    WIDTH = 64    # a constant width for the image and rect
    HEIGHT = 64   # a constant height for the image and rect
