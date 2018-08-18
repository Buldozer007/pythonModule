"""This module helps you to find nested list in other list"""



def print_lol(the_list):
    """So , how it works ? It works very simple .
    Cycle helps to find item that is list (using isinstance BIF)
    ,and if it's a list function is printing it and if it's not a
    list it's just printing current item."""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)