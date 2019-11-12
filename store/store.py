""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def store_options():
    run_menu = True
    while run_menu == True:
        table = data_manager.get_table_from_file('store/games.csv')
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == '1':  
            show_table(table)
            input('Press enter to continue...')
            ui.print_menu('Store',
                         ['Show Table', 'Add', 'Remove', 'Update','Count', 'Average'],
                         'Return To Main Menu', )
        elif option == '2':
            add(table)
            print(add(table))
        elif option == '3':
            get_id = ui.get_inputs(['Enter the id you want to remove'], '')
            remove(table, get_id)
        elif option == '4':
            print('g')
        elif option == '5':
            print('g')
        elif option == '6':
            print('g')
        elif option == '0':
            run_menu = False
        else:
            raise KeyError("There is no such option.")


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.
    Returns:
        None
    """

    ui.print_menu('Store', 
    ['Show Table', 'Add', 'Remove', 'Update','Count', 'Average'], 'Return To Main Menu', )
    store_options()


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['id', 'title', 'manufacturer', 'price', 'in_stock']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    new_data = []
    new_id = ui.get_inputs(['Enter id: '], '')
    # new_game_title = ui.get_inputs(['Enter game title: '], '')
    # new_manufacturer = ui.get_inputs(['Enter manufacturer: '], '')
    # new_price = ui.get_inputs(['Enter price: '], '')
    # new_stock = ui.get_inputs(['Enter how many are in stock: '], '')

    new_data.append(new_id)
    table.append(new_data)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    new_table = common.remove_from_list(table, id_)
    data_manager.write_table_to_file('store/games.csv', new_table)
    return new_table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
