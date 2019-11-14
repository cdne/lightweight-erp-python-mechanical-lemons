""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

def choose_crm():
    crm_menu_active = True
    while crm_menu_active is True:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        table = data_manager.get_table_from_file('crm/customers.csv')
        if option == '1':
            show_table(table)
        elif option == '2':
            add(table)
            data_manager.write_table_to_file('crm/customers.csv', table)
        elif option == '3':
            id_ = ui.get_inputs(['ID of item to remove: '], 'Crm')[0]
            remove(table, id_)
            data_manager.write_table_to_file('crm/customers.csv', table)
        elif option == '4':
            id_ = ui.get_inputs(['ID of item to update: '], 'Crm')[0]
            update(table, id_)
            data_manager.write_table_to_file('crm/customers.csv', table)
        elif option == '5':
            longest_name = get_longest_name_id(table)
            ui.print_result(longest_name,'Crm data - the customer id with the longest name: ')
        elif option == '6':
            subscribers_list = get_subscribed_emails(table)
            get_subscribed_emails(table)
            ui.print_result(subscribers_list,'Crm data - subscribers list: ')
        elif option == '0':
            crm_menu_active = False

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    ui.print_menu('CRM', ['Show table', 'Add', 'Remove', 'Update', 'What is the id of the customer with the longest name?', 'Which customers has subscribed to the newsletter?'], 'Return to main menu')
    choose_crm()


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    table = data_manager.get_table_from_file('crm/customers.csv')
    ui.print_table(table, ['id', 'name', 'email', 'subscribed'])
    


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    item = ui.get_inputs(['Id: ', 'Name: ', 'Email: ', 'Subscribed: '], 'Please provide product data: ')
    table.append(item)
    ui.print_table(table, ['id', 'name', 'email', 'subscribed'])
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

    for i in range(len(table)):
        if table[i][0] == id_:
            table.pop(i)
    ui.print_table(table, ['id', 'name', 'email', 'subscribed'])
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    list_labels = ['id: ', 'name: ', 'email: ', 'subscribed: ']
    for i in range(len(table)):
        if table[i][0] == id_:
            item = ui.get_inputs(list_labels, 'Crm')
            table.pop(i)
            table.insert(i, item)
    ui.print_table(table, ['id', 'name', 'email', 'subscribed'])
    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    dictionary = {}
    for i in range(len(table)):
        try:
            dictionary[len(table[i][1])].append([str(table[i][1]), table[i][0]])
        except KeyError:
            dictionary[len(table[i][1])] = [[str(table[i][1]), table[i][0]]]
    dictionary_longest_name = {}
    longest_names = list(dictionary.keys())[0]
    for key in dictionary:
        if key > longest_names:
            longest_names = key            
        dictionary_longest_name = dictionary[longest_names] 
    
    for i in dictionary_longest_names:
        split_name = list(dictionary_longest_name[i][0].split(""))
        temp_biggest = "a"
        if split_name[0] > temp_biggest:
            temp_biggest = split_name[0]

    return split_name

# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")

def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """
    EMAIL_SUBSCRIPTION = 3
    EMAIL = 2
    NAME = 1
    formated_email_name = ''
    formated_list = []
    for customer in table:
        if customer[EMAIL_SUBSCRIPTION] == '1':
            formated_email_name = customer[EMAIL] + ';' + customer[NAME]
            formated_list.append(formated_email_name)
    return formated_list