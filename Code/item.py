import pygame

# Initialize the pygame
pygame.init()


# item init
# Function to set the all the attributes of the item
# item_id   :    unique id associated with this item
# item_name :    name associated with this item
# item_num  :    number of this item in the stack
# item_pos  :    position of the top left corner of the item
class Item:
    def __init__(self, item_id: int, item_name: str, item_info: str, item_num: int, item_pos: tuple, image_dir: str):
        self.i_id = item_id
        self.name = item_name
        self.info = item_info
        self.num = item_num
        self.pos = item_pos
        self.rect = pygame.Rect(self.pos, (self.WIDTH, self.HEIGHT))
        self.image = pygame.image.load(image_dir)

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

    i_id = None
    name = None
    info = None
    num = None
    pos = None
    rect = None
    image = None
    WIDTH = 16
    HEIGHT = 16
