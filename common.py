""" Common module
implement commonly used functions here
"""

import random


"""
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'),
         2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """


def generate_random(table):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                     'w', 'x', 'y', 'z']
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                     'W', 'X', 'Y', 'Z']
    last_values = '#&'
    random_lower_letter = lower_letters[random.randint(
        0, len(lower_letters) - 1)]
    random_upper_letter = upper_letters[random.randint(
        0, len(upper_letters) - 1)]
    random_digit = str(digits[random.randint(0, len(digits) - 1)])
    generated = random_lower_letter + random_upper_letter + random_digit + \
        random_digit + random_upper_letter + random_lower_letter + last_values
    return generated


def is_larger(current_largest, new_item):
    if new_item > current_largest:
        return True
    else:
        return False


def remove_from_list(table, id_):
    new_table = []
    ID = 0
    for data in table:
        if id_[ID] not in data[ID]:
            new_table.append(data)
    return new_table


def bubbleSort(arr, key=None):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][key] > arr[j+1][key]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def how_many_times(arr, title):
    times = 0
    for i in arr:
        if i == title:
            times += 1
    return times


def mean(arr):
    n = len(arr)
    if n == 0:
        return 0
    elements_added = 0
    for item in arr:
        elements_added += float(item)
    return round(elements_added/n)


def calculate_days(year, month, day):
    return (int(year)-1900)*365 + int(month)*30 + int(day)
