import pygame

pygame.init()


class Button:
    def __init__(self, new_height: int, new_width: int, new_pos: tuple, new_text: str):
        self.height = new_height
        self.width = new_width
        self.pos = new_pos
        self.rect = pygame.rect.Rect(self.pos, (self.width, self.height))
        self.text = self.font.render(new_text, True, pygame.Color(255, 255, 255))

    def get_rect(self):
        return self.rect

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_pos(self):
        return self.pos

    def get_text(self):
        return self.text

    def set_height(self, new_height):
        self.height = new_height

    def set_width(self, new_width):
        self.width = new_width

    def set_pos(self, new_pos):
        self.pos = new_pos

    def set_text(self, new_text):
        self.text = new_text

    def set_color(self, new_color):
        self.color = new_color

    # This function checks to see whether or not the mouse is hovering
    # if it is, change the colour slightly and return True if click = True
    def hover(self, m_pos: tuple, click: bool):
        # compare the coordinates of the mouse and the items rect
        is_hover = self.rect.left < m_pos[0] < self.rect.right and self.rect.top < m_pos[1] < self.rect.bottom
        # if hovering over
        if is_hover:
            # change the colour to the highlight colour
            self.color = self.new_color
            # if player clicks while hovering return true
            if click:
                return True
        # when not hovering reset colour
        else:
            self.color = self.old_color
        return False

    # This displays the button with the text centered on it
    def display(self, screen: pygame.display):
        # Set the rect for the text to the center of the button
        text_rect = self.text.get_rect(center=self.rect.center)
        # Draw the button
        pygame.draw.rect(screen, self.color, self.rect)
        # Draw the text
        screen.blit(self.text, text_rect)

    rect = None         # button rect
    height = None       # height of the button
    width = None        # width of the button
    pos = None          # position of the button
    text = None         # text on the button
    color = pygame.Color(50, 50, 50)
    old_color = color
    if color.r + 20 < 255 and color.g + 20 < 255 and color.b + 20 < 255:
        new_color = pygame.Color(color.r + 20, color.g + 20, color.b + 20)
    else:
        new_color = pygame.Color(255, 255, 255)
    font = pygame.font.Font("freesansbold.ttf", 12)  # change this to change font and font size