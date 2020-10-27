# Created by Ben Kung

import pygame
import Code.item

from Code import item

# Sort functions that take a list of items and sort by specified method


# sort min to max id, creates new list
# uses insertion sort algorithm
# takes a list of item and returns a new list of items sorted
def sort_by_id(list):
    index = 0
    new_list = []
    while len(list) >= 1:
        index = 0
        for place in range(0, len(list)):
            if list[place].get_id() < list[index].get_id():
                index = place
        new_list.append(list[index])
        list.pop(index)
    return new_list


# sort by name A-Z, creates new list
#uses insertion sort
def sort_by_name(list):
    index = 0
    new_list = []
    while len(list) >= 1:
        index = 0
        for place in range(0, len(list)):
            if list[place].get_name() < list[index].get_name():
                index = place
        new_list.append(list[index])
        list.pop(index)
    return new_list


# sort by item quantity lowest to highest
# uses insertion sort
def sort_by_number(list):
    index = 0
    new_list = []
    while len(list) >= 1:
        index = 0
        for place in range(0, len(list)):
            if list[place].get_num() < list[index].get_num():
                index = place
        new_list.append(list[index])
        list.pop(index)
    return new_list


def tester():
    item1 = item.Item(0, "Sword", "An ancient sword passed down through your family", 1, (0, 0), "./Assets/sword.png")
    item2 = item.Item(1, "Apple", "An apple picked fresh from a tree", 32, (0, 0), "./Assets/apple.png")
    item3 = item.Item(2, "Gem", "A precious gemstone", 3, (0, 0), "./Assets/gem.png")
    item_list = [item3, item2, item1]

    for i in range(0,len(item_list)):
        print(item_list[i].get_name())

    # sort by id
    item_list = sort_by_id(item_list)
    print("Sorting by id")
    for i in range(0,len(item_list)):
        print(item_list[i].get_name())

    # sort by item name
    item_list = sort_by_name(item_list)
    print("Sorting by name")
    for i in range(0,len(item_list)):
        print(item_list[i].get_name())

    # sort by item number
    item_list = sort_by_number(item_list)
    print("Sorting by number")
    for i in range(0,len(item_list)):
        print(item_list[i].get_name())


tester()