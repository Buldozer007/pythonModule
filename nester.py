"""This module helps you to find nested list in other list"""



def print_lol(the_list , level=0):
    """So , how it works ? It works very simple .
    Cycle helps to find item that is list (using isinstance BIF)
    ,and if it's a list function is printing it and if it's not a
    list it's just printing current item. If there is a nested list
     it will be used tab-stop."""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1)
        else:
            for tab_stop in range(level):
                print("\t" , end='')
            print(each_item)