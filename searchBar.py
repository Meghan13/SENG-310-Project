import pygame
import button
from sortingStuff import sort_by_name
import pygame_textinput


class SearchBar:
    text_colour = pygame.Color(23, 23, 23)  # text colour
    BAR_HEIGHT = 40  # height of search bar
    BAR_WIDTH = 200  # width of search bar
    BAR_POS = (550, 10)  # screen position of search bar
    CLEAR_BUTTON_POS = (BAR_POS[0] + 165, BAR_POS[1] + 5)  # screen position of clear button relative to search bar
    CLEAR_BUTTON_WIDTH = 30
    CLEAR_BUTTON_HEIGHT = 30

    def __init__(self, new_text_colour, new_bar_pos, new_bar_width,
                 new_bar_height, new_clear_button_pos,
                 new_clear_button_width, new_clear_button_height):
        # Create TextInput Obj
        self.textinput = pygame_textinput.TextInput(text_color=new_text_colour)
        self.bar = pygame.Rect(new_bar_pos, (new_bar_width, new_bar_height))
        # self.screen = screen
        self.text_input_active = True
        self.textinput.max_string_length = 10
        self.user_search_text = ""
        self.clear_button = pygame.Rect(new_clear_button_pos, (new_clear_button_width, new_clear_button_height))

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Handles clicking on clear button
            if self.clear_button.collidepoint(x, y):
                self.search_bar_clear_button([event])
            # Handles clicking of search bar
            elif self.bar.collidepoint(x, y):
                # self.screen.blit(self.textinput.get_surface(), self.BAR_POS)
                self.textinput.update([event])
                self.text_input_active = True

            # Handles toggling of active search bar
            elif not self.bar.collidepoint(x, y):
                self.textinput.cursor_visible = False
                self.text_input_active = False
                self.textinput.update([event])

        # Handles search upon pressing enter/return key
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.text_input_active:

        # print(self.user_search_text) #For debugging

        if self.text_input_active:
            self.textinput.update([event])
            self.user_search_text = self.textinput.input_string

    def search_bar_clear_button(self, events):
        self.textinput.input_string = ""
        self.textinput.update(events)

    def get_user_search_text(self):
        return self.user_search_text

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color(225, 225, 225), self.bar)
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), self.clear_button)
        screen.blit(self.textinput.get_surface(), self.bar.topleft)


# The following code Tests SearchBar class
def test():
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    clock.tick(15)
    screen.fill(pygame.Color(0, 0, 0))
    running = True
    search_bar = SearchBar(screen)

    while running:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            search_bar.update(event)
            search_bar.draw(screen)

        pygame.display.update()
        clock.tick(30)
# test()