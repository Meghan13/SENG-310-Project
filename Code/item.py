import pygame
from enum import Enum
# Initialize the pygame
pygame.init()

# item init
# Function to set the all the attributes of the item
# item_id   :    unique id associated with this item
# item_name :    name associated with this item
# item_num  :    number of this item in the stack
# item_pos  :    position of the top left corner of the item


class Item :
    def __init__(self, item_id: int, item_name: str, item_info: str, item_num: int, item_pos: tuple, image_dir: str):
        self.i_id = item_id
        self.name = item_name
        self.info = item_info
        self.num = item_num
        self.pos = item_pos
        self.rect = pygame.Rect(self.pos, (self.WIDTH, self.HEIGHT))
        self.image = pygame.image.load(image_dir)
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))

    def get_id(self):
        return self.i_id

    def get_name(self):
        return self.name

    def get_info(self):
        return self.info

    def get_num(self):
        return self.num

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

    def set_name(self, item_name: str):
        self.name = item_name

    def set_info(self, item_info: str):
        self.info = item_info

    def set_num(self, item_num: int):
        self.num = item_num

    def set_pos(self, item_pos: tuple):
        self.pos = item_pos
        self.rect = pygame.Rect(self.pos, (self.WIDTH, self.HEIGHT))

    def highlight(self, highlight_bool: bool):
        self.is_highlighted = highlight_bool

    # This function takes in a screen and displays the items image at that coordinate
    def display(self, screen: pygame.display):
        pygame.draw.rect(screen, pygame.Color(50, 50, 50), self.rect)
        screen.blit(self.image, self.pos)

    # This function displays the item description to the screen just above the cursor
    def description(self, screen: pygame.display, m_pos: tuple):
        # Check to see if mouse is over (second variable not used yet)
        if self.hover(m_pos, False):
            # create a text object based on our global item font
            text = self.font.render(self.info, True, pygame.Color(255, 255, 255))
            # display text
            screen.blit(text, (m_pos[0], m_pos[1] - 10))
        # reset the text to be the number of items
        text = self.font.render(str(self.num), True, pygame.Color(255, 255, 255))
        # display the number of items
        screen.blit(text, self.rect.midbottom)

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
    name = None   # item name
    info = None   # item description
    num = None    # amount of an item
    pos = None    # position for the item and rect
    rect = None   # item rect for collisions/hover detection
    image = None  # a string which stores the location of the image for an item
    is_highlighted = False
    WIDTH = 48    # a constant width for the image and rect
    HEIGHT = 48   # a constant height for the image and rect
