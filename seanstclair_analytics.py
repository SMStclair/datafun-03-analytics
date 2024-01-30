# Project Module 3 
"""Python module that demonstrates skills in fetching data from the web, 
processing it using Python collections, and writing the processed data 
to different file formats."""

# Standard library imports
import csv
import json
import pathlib 
from io import StringIO
from pathlib import Path
import io

# External import
import requests 
import pandas as pd
import xlrd
from collections import Counter

# Import local modules
import Sean_StClair_utils
import seanstclairprojsetup

#Data acquisition

def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_txt_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch json data: {response.status_code}")

#Write Data

def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)  # use pathlib to join paths

    # Create the folder if it doesn't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open('w', encoding='utf-8-sig') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

def write_csv_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w', newline='', encoding='utf-8') as file:
        file.write(data)
        print(f"CSV data saved to {file_path}")

def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

def write_json_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w') as file:
        json.dump(data, file, indent=4)
        print(f"JSON data saved to {file_path}")

#Function 1: Process text data

def process_txt_file(input_file, output_file):
    #get count of words in text file
    try:
        with open(input_file, 'r') as file:
            text = file.read()
        words = text.split()
        word_count = Counter(words)

        with open(output_file, 'w') as file:
            for word, count in word_count.items():
                file.write(f"{word}: {count}\n")
        print(f"Word count saved to {output_file}")
    except Exception as e:
        print(f"Error processing text data: {e}")


#Function 2. Process CSV Data
def process_csv_file(input_file, output_file):
    # Calculate the average and median amount of global sales for video games.
    try:
        df = pd.read_csv(input_file)

        average_global_sales = df['Global_sales'].mean()
        median_global_sales = df['Global_sales'].mean()

        with open(output_file, 'w') as file:
            file.write(f"Average Global Sales: {average_global_sales}\n")
            file.write(f"Median Global Sales: {median_global_sales}\n")

        print(f"Averages saved to {output_file}")
    except Exception as e:
        print(f"Error processing CSV data: {e}")

#Function 3: Process Excel Data

def process_excel_file(input_file, output_file):
    try:
        df = pd.read_excel(input_file)
        # Sort list of sample cases from highest to lowest
        sorted_df = df.sort_values('cases', ascending=False)
        sorted_output_file = output_file.replace('.txt', '.xlsx')
        sorted_df.to_excel(sorted_output_file, index=False)
        print(f"Data sorted by cases and saved to {sorted_output_file}")
    except Exception as e:
        print(f"Error processing Excel data: {e}")

#Function 4: Process Json Data

def process_json_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
        #Parsed Song Name of random songs data set
        with open(output_file, 'w') as file:
            for title in data:
                songName = title.get('songName', [])
                file.write(f"{title['title']}: {', '.join(songName)}\n")
        
        print(f"Song name extracted and saved to {output_file}")
    except Exception as e:
        print(f"Error processing JSON data: {e}")

# Exception reporting
def fetch_txt_data(folder_name, url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        # Will raise an HTTPError 
        # if the HTTP request returns an unsuccessful status code

        # Assuming the response content is text data
        file_path = Path(folder_name) / 'data.txt'
        with open(file_path, 'w') as file:
            file.write(response.text)
        print(f"Text data saved to {file_path}")

    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

def main():
    ''' Main function to demonstrate module capabilities. '''
   
    print(f"Name: {'datafun-03-analytics-SeanStClair'}")

    txt_url = 'https://github.com/tadzik/5e-spells/blob/master/spelllist.txt'

    csv_url = 'https://github.com/ValdisW/datasets/blob/master/video-game-sales.csv' 

    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/blob/master/fullmoon.xls' 
    
    json_url = 'https://gist.github.com/Jetrom17/380adb1d9d7b6f23a948759b48fce64e#file-music-info-json'

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename, json_url)

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')

if __name__ == "__main__":
    main()