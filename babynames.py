"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import sys

YEAR = ['1900', '1910', '1920', '1930', '1940', '1950', '1960', '1970', '1980', '1990', '2000', '2010']

def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    if name in name_data:                           # Check if name of data input is exist.
        if year in name_data[name]:                 # Check if year of data input is in dictionary name_data.
            value = name_data[name][year]           # Get the value 'rank' of key 'year'.
            if int(rank) < int(value):              # To compare 2 str type, must switch the type to int.
                name_data[name][year] = rank        # Update lower rank value.
        else:
            name_data[name][year] = rank            # Add new rank value of key name_data[name][year].
    else:
        name_data[name] = {year: rank}              # Add new value of name_data[name].


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    with open(filename, 'r') as f:
        year = ''
        for line in f:

            baby_info = line

            if baby_info.split()[0] in YEAR:                  # Separate words by blanks and check if it is in constant.
                year += line.strip()                          # Delete the blanks and record the year.
            else:
                data = []                                     # A list to store words processed.
                info = baby_info.split(',')                   # Separate words by ','.
                for word in info:
                    index = word.strip()                      # Delete the blanks near by each word.
                    data.append(index)

                rank = data[0]
                name1 = data[1]
                name2 = data[2]

                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for filename in filenames:
        add_file(name_data, filename)

    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    matching_names = []                             # A list to store names processed.
    for name in name_data:
        for i in range(len(name)-len(target)+1):    # Times to check. For example, Jerry <-> er, needs to check 4 times.
            check = ''                              # Store string processed to check
            for j in range(len(target)):
                check += name[i+j]                  # Amounts of character to add in string 'check'
            if check.lower() == target.lower():
                matching_names.append(name)         # Add names in list'matching_names'.

    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
