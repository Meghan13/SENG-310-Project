# Created by Ben Kung
import pygame

import item


# Sort functions that take a list of items and sort by specified method


# helper function that removes the nulls from the list
# and returns the count of number of nulls removed
def remove_null(list):
    num = 0
    null_pos = []
    # loop through and find the position of all nulls
    for index in range(0, len(list)):
        if list[index] is None:
            num += 1
            null_pos.append(index)
    # flip order to not create problems with pop()
    null_pos.reverse()
    # remove all the nulls
    for index in range(0, len(null_pos)):
        list.pop(null_pos[index])
    return num


# sort min to max id, creates new list
# uses insertion sort algorithm
# takes a list of item and returns a new list of items sorted
def sort_by_id(list):
    new_list = []
    # remove nulls to sort
    null_num = remove_null(list)
    # insertion sort
    while len(list) >= 1:
        index = 0
        for place in range(0, len(list)):
            if list[place].get_id() < list[index].get_id():
                index = place
        new_list.append(list[index])
        list.pop(index)
    # add nulls back
    for index in range(0, null_num):
        new_list.append(None)

    return new_list


# sort by name A-Z, creates new list
# uses insertion sort
def sort_by_name(list):
    new_list = []
    # remove nulls to sort
    null_num = remove_null(list)
    # insertion sort
    while len(list) >= 1:
        index = 0
        for place in range(0, len(list)):
            if list[place].get_name() < list[index].get_name():
                index = place
        new_list.append(list[index])
        list.pop(index)
    # add nulls back
    for index in range(0, null_num):
        new_list.append(None)
    return new_list


# sort by item type A-Z, creates new list
# uses insertion sort
def sort_by_type(list):
    new_list = []
    null_num = remove_null(list)
    while len(list) >= 1:
        index = 0
        for place in range(0, len(list)):
            if list[place].get_type() < list[index].get_type():
                index = place
        new_list.append(list[index])
        list.pop(index)
    # add nulls back
    for index in range(0, null_num):
        new_list.append(None)
    return new_list


# sort by item quantity lowest to highest
# uses insertion sort
def sort_by_number(list):
    new_list = []
    null_num = remove_null(list)

    dictionary = {}
    # count the total number of each item and stores as a dictionary
    for item in range(0, len(list)):
        if list[item].get_name() in dictionary:
            dictionary[list[item].get_name()] += list[item].get_num()
        else:
            dictionary[list[item].get_name()] = list[item].get_num()
    for x, y in dictionary.items():
        print(x, y)

    # perform insertion sort
    while len(dictionary) >= 1:
        # get the minimum item name
        key_min = min(dictionary.keys(), key=(lambda k: dictionary[k]))
        print(key_min, "min key", dictionary[key_min], "value")
        pop_list = [] # store all places to pop
        # add all instances of min item to front of the list
        for item in range(0, len(list)):
            if list[item].get_name() == key_min:
                new_list.append(list[item])
                pop_list.append(item)
        # remove item from list
        pop_list.sort(reverse = True)
        for index in range(0, len(pop_list)):
            list.pop(pop_list[index])
        # remove key
        dictionary.pop(key_min)

    # add nulls back
    for index in range(0, null_num):
        new_list.append(None)
    return new_list
'''
# sort by item quantity lowest to highest
# original sort with bugs
# uses insertion sort
def sort_by_number(list):
    new_list = []
    null_num = remove_null(list)
    while len(list) >= 1:
        index = 0
        for place in range(0, len(list)):
            if list[place].get_num() < list[index].get_num():
                index = place
        new_list.append(list[index])
        list.pop(index)
    # add nulls back
    for index in range(0, null_num):
        new_list.append(None)
    return new_list
'''
# forgot to add extra nulls when removing items, Failed attempt to program
'''
def sort_by_number(list):
    # remove nulls
    null_num = remove_null(list)
    new_list = []
    new_list_pointer = 0
    dictionary = {}
    # count the total number of each item and stores as a dictionary
    for item in range(0, len(list)):
        if list[item].get_name() in dictionary:
            dictionary[list[item].get_name()] += list[item].get_num()
        else:
            dictionary[list[item].get_name()] = list[item].get_num()
    # perform insertion sort
    while len(list) >= 1 and len(dictionary) >= 1:
        min_value = 2000000000 # large number
        key_to_remove = ""
        # look for smallest value in dictionary
        for item in dictionary:
            if dictionary[item] < min_value:
                key_to_remove = item

        # remove smallest item from dictionary and add to new list
        # get value
        added_value = dictionary.get(key_to_remove)
        print(added_value, ", Value", key_to_remove, ", Key")
        dictionary.pop(key_to_remove)
        flag = False # check to only add once
        pop_list = [] # store the pop positions
        # loop through list to find the item
        for item in range(0, len(list)):
            if flag == False:
                print(list[item].get_name(), key_to_remove)
                if list[item].get_name() == key_to_remove:
                    while added_value > 0:
                        # add a max stack if more than max stack in items, else add the remaining
                        if added_value > list[item].get_max_stack():
                            print("Adding max stack for ", list[item].get_name())
                            print("Added value is ", added_value)
                            new_list.append(list[item])
                            new_list[new_list_pointer].set_num(list[item].get_max_stack())
                            # increment the rear of the list
                            new_list_pointer += 1
                            # change the value of how many items left
                            added_value -= list[item].get_max_stack()
                            print("Added value is after ", added_value)
                            pop_list.append(item)
                        else:
                            print("Adding part stack for ", list[item].get_name())
                            print("Added value is ", added_value)
                            new_list.append(list[item])
                            new_list[new_list_pointer].set_num(added_value)
                            new_list_pointer += 1
                            added_value = 0
                            print("Added value is after ", added_value)
                            pop_list.append(item)
                    flag = True
            else:
                if list[item].get_name() == key_to_remove:
                    print("removing extra ", list[item].get_name())
                    pop_list.append(item)
        # remove all items from list
        for index in range(0, len(pop_list)):
            print("Removing", list[index].get_name())
            list.pop(pop_list[index])
    # add nulls back in
    for index in range(0, null_num):
        new_list.append(None)
    return new_list
'''
# currently using placeholder boolean to determine
# whether is highlighted, will use later method to
# determine later
# sort using bucket sort algorithm
def sort_by_highlight(list):
    highlight_list = []
    non_highlight_list = []
    null_num = remove_null(list)
    # do a first pass to separate highlighted items from non highlighted
    for i in range(0, len(list)):
        if list[i].highlight_sort:
            highlight_list.append(list[i])
        else:
            non_highlight_list.append(list[i])
    # add non highlighted to the back
    highlight_list.extend(non_highlight_list)
    # add nulls back
    for index in range(0, null_num):
        highlight_list.append(None)
    return highlight_list


def tester():
    item1 = item.Item(0, "Weapon", "Sword", "An ancient sword passed down", 1, (0, 0), "./Assets/sword.png")
    item2 = item.Item(1, "Food", "Apple", "An apple picked fresh from a tree", 16, (0, 0), "./Assets/apple.png")
    item3 = item.Item(2, "Mineral", "Gem", "A precious gemstone", 3, (0, 0), "./Assets/gem.png")
    item4 = None
    item5 = None
    item6 = item.Item(2, "Mineral", "Gem", "A precious gemstone", 15, (0, 0), "./Assets/gem.png")

    item_list = [item1, item4, item3, item2, item5, item6]

    print("starting list")
    for i in range(0, len(item_list)):
        if item_list[i] is not None:
            print(item_list[i].get_name())

    # sort by item number
    item_list = sort_by_number(item_list)
    print("Sorting by number")
    for i in range(0, len(item_list)):
        if item_list[i] is not None:
            print(item_list[i].get_name(), item_list[i].get_num())
        else:
            print("Null")
'''
    # sort by id
    item_list = sort_by_id(item_list)
    print("Sorting by id")
    for i in range(0, len(item_list)):
        if item_list[i] is not None:
            print(item_list[i].get_name())
        else:
            print("Null")

    # sort by item name
    item_list = sort_by_name(item_list)
    print("Sorting by name")
    for i in range(0, len(item_list)):
        if item_list[i] is not None:
            print(item_list[i].get_name())
        else:
            print("Null")

    # sort by item type
    item_list = sort_by_type(item_list)
    print("Sorting by type")
    for i in range(0, len(item_list)):
        if item_list[i] is not None:
            print(item_list[i].get_name())
        else:
            print("Null")

 

    # sort by highlight
    item1.set_highlight(False)
    item2.set_highlight(True)
    item3.set_highlight(True)

    item_list = sort_by_highlight(item_list)
    print("Sorting by highlight")
    for i in range(0, len(item_list)):
        print(item_list[i].get_name())
'''

#tester()