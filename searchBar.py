import pygame
from Code import button
from Code import inventory
from sortingStuff import sort_by_name
from Code import pygame_textinput


def search_bar_button():
    # bar = button.Button(20, 20, (10, 10), "Text", pygame.Color(139, 82, 45))
    # bar.txt_surface = Front.render(text, True, bar.colour)
    pass


def search_items():
    pass


#Create TextInput Obj
# textinput = pygame_textinput.TextInput(text_color = (255, 255, 255))
textinput = pygame_textinput.TextInput(text_color = (0, 0, 0))
screen = pygame.display.set_mode((800,600))
# bar = pygame.display.set_mode((1000, 60))
clock = pygame.time.Clock()
clock.tick(15)

running = True

while running:
    screen.fill(pygame.Color(0, 0, 0))
    bar = pygame.Rect((550, 10), (200, 40))
    pygame.draw.rect(screen, pygame.Color(225, 225, 225), bar)

    # bar.fill((225,225,225))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if bar.collidepoint(x, y):
                screen.blit(textinput.get_surface(), (550, 10))
            textinput.update(events)
        textinput.update(events)



    pygame.display.update()
    clock.tick(30)
