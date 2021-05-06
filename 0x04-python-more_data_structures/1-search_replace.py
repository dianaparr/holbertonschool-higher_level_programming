#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # search is the value to search for in the my_list
    # replace is the value to replace with in the my_list
    # Use list comprehension
    return [replace if search == element else element for element in my_list]
