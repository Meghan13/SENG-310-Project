import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def hello_world(sort_option):
    print("Ben K Wrote This")
    item = [("Matthew", 5, pygame.Rect((10, 10), (10, 10))), ("Andrew", 53, pygame.Rect((30, 10), (10, 10))),
            ("Ben K", 10, pygame.Rect((50, 10), (10, 10))), ("Meghan", 22, pygame.Rect((50, 10), (10, 10))),
            ("Ben M", 543216, pygame.Rect((50, 10), (10, 10)))]
    if sort_option == 0:
        item.sort(key=byName)
    if sort_option == 1:
        item.sort(reverse=True, key=byName)
    if sort_option == 2:
        item.sort(key=byNum)
    if sort_option == 2:
        item.sort(reverse=True, key=byNum)

    rect_coords = (10, 10)
    for i in item:
        print(i)


def byName(e):
    return e[0]


def byNum(e):
    return e[1]


hello_world(0)
hello_world(1)
hello_world(2)
hello_world(3)
