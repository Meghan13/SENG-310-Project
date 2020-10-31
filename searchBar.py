import pygame
import button
import inventory
from sortingStuff import sort_by_name
import pygame_textinput


class SearchBar:
    text_colour = pygame.Color(23, 23, 23)  # text colour
    BAR_HEIGHT = 40  # height of search bar
    BAR_WIDTH = 200  # width of search bar
    BAR_POS = (550, 10) # screen position of search bar

    def __init__(self, screen, new_text_colour = text_colour, new_bar_pos = BAR_POS, new_bar_width = BAR_WIDTH, new_bar_height = BAR_HEIGHT):
        # Create TextInput Obj
        self.textinput = pygame_textinput.TextInput(text_color=new_text_colour)
        self.bar = pygame.Rect(new_bar_pos, (new_bar_width, new_bar_height))
        self.screen = screen
        self.text_input_active = True
        self.user_search_text = ""

    def update(self, events):
        pygame.draw.rect(screen, pygame.Color(225, 225, 225), self.bar)
        for event in events:
            self.bar = pygame.Rect(self.BAR_POS, (self.BAR_WIDTH, self.BAR_HEIGHT))

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.bar.collidepoint(x, y):
                    self.screen.blit(self.textinput.get_surface(), self.BAR_POS)
                    self.textinput.update(events)
                    self.text_input_active = True

                elif not self.bar.collidepoint(x, y):
                    self.textinput.cursor_visible = False
                    self.text_input_active = False
                    self.textinput.update(events)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.text_input_active:
                self.user_search_text = self.textinput.input_string
                print(self.user_search_text) #For debugging

        if self.text_input_active:
            self.textinput.update(events)
        self.screen.blit(self.textinput.get_surface(), self.BAR_POS)

    def search_bar_clear_button(self):
        pass

    def search_items(self):
        pass

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
    search_bar.update(events)

    pygame.display.update()
    clock.tick(30)
