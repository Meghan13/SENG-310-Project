from item import Item

names = [
    'Pickaxe',
    'Sword',
    'Bow',
    'Apple',
    'Carrot',
    'Meat',
    'Coin',
    'Key',
    'Gem',
    'Arrow',
]


def create_item_by_id(id: int, count: int):
    # print(names[id])
    return create_item_by_name(names[id], count)


def create_item_by_name(name: str, count: int):
    if name == 'Pickaxe':
        return Item(0, "tool", name, "Good for breaking things", min(count, 1), (10, 10), "./Assets/pickaxe.png", 1)
    elif name == 'Sword':
        return Item(1, "tool", name, "Cuts and stabs", min(count, 1), (10, 10), "./Assets/sword.png", 1)
    elif name == 'Bow':
        return Item(2, "tool", name, "Useless without arrows...", min(count, 1), (10, 10), "./Assets/bow.png", 1)
    elif name == 'Apple':
        return Item(3, "food", name, "Keep the doctors away", min(count, 99), (10, 10), "./Assets/apple.png", 99)
    elif name == 'Carrot':
        return Item(4, "food", name, "The envy of rabbits far and wide", min(count, 99), (10, 10), "./Assets/carrot.png", 99)
    elif name == 'Meat':
        return Item(5, "food", name, "Meat fibers!", min(count, 99), (10, 10), "./Assets/meat.png", 99)
    elif name == 'Coin':
        return Item(6, "currency", name, "Exchange for goods and services", min(count, 999), (10, 10), "./Assets/coin.png", 999)
    elif name == 'Key':
        return Item(7, "currency", name, "Unlocks something", min(count, 99), (10, 10), "./Assets/key.png", 99)
    elif name == 'Gem':
        return Item(8, "currency", name, "Probably valuable", min(count, 99), (10, 10), "./Assets/gem.png", 99)
    elif name == 'Arrow':
        return Item(9, "ammo", name, "Useless without a bow...", min(count, 99), (10, 10), "./Assets/arrow.png", 99)

