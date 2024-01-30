"""Develop a Python module that demonstrates proficiency in loops, project folder creation using pathlib, and importing modules."""

#Imports
import pathlib
import time
import os
import Sean_StClair_utils

#Function 1: Create a function to generate folders for a given range
def create_folders_for_range(start, end):
    
    #call function 1
    for year in range(start, end +1):
        pathlib.Path(str(year)).mkdir(exist_ok=True)


#Function 2: Develop a function to create folders from a list of names
def create_folders_from_list(folder_names, to_lowercase=False, remove_spaces=False):
    
    #call function 2 and add options
    for item in folder_names:
        folder_name = str(item)
        
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(' ', '_')

        pathlib.Path(folder_name).mkdir(exist_ok=True)


#Function 3: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix
def create_prefixed_folders(folder_names, prefix):
    
    #call function 3
    compre = [prefix + i for i in folder_names if i != ""]
    for item in compre:
        if not os.path.exists(item):
            os.mkdir(item)

#Function 4: Write a function to create folders periodically 
def create_folders_periodically(duration_secs):
    
    #call function 4
    period_folder = 1
    while period_folder <= 6:
        pathlib.Path("folder-" + str(period_folder)).mkdir(exist_ok=True)
        period_folder += 1
        time.sleep(5)


#Create a path object
project_path = (pathlib.Path.cwd())

#Define the new sub folder path
data_path = project_path.joinpath("data")

#Create new if it doesn't exist
data_path.mkdir(exist_ok=True)

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {Sean_StClair_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start=2020, end=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

if __name__ =='__main__':
    main()