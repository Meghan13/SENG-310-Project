import pygame
import button
import inventory
from sortingStuff import sort_by_name
import pygame_textinput


def search_bar_button():
    # bar = button.Button(20, 20, (10, 10), "Text", pygame.Color(139, 82, 45))
    # bar.txt_surface = Front.render(text, True, bar.colour)
    pass


def search_items():
    pass


#Create TextInput Obj
textinput = pygame_textinput.TextInput(text_color = (128, 128, 128))
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
clock.tick(15)

running = True
text_input_active = True
while running:

    screen.fill(pygame.Color(0, 0, 0))
    bar = pygame.Rect((550, 10), (200, 40))

    pygame.draw.rect(screen, pygame.Color(225, 225, 225), bar)

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if bar.collidepoint(x, y):
                screen.blit(textinput.get_surface(), (550, 10))
                textinput.update(events)
                text_input_active = True
            elif not bar.collidepoint(x, y):
                textinput.cursor_visible = False
                text_input_active = False
                textinput.update(events)

    if text_input_active:
        textinput.update(events)
    screen.blit(textinput.get_surface(), (550, 10))



    pygame.display.update()
    clock.tick(30)
