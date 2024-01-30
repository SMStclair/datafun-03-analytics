# Project Module 3 
"""Python module that demonstrates skills in fetching data from the web, 
processing it using Python collections, and writing the processed data 
to different file formats."""

# Standard library imports
import csv
import pathlib 
from io import StringIO
from pathlib import Path
import io

# External import
import requests 
import pandas as pd

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
    file_path = Path(folder_name).joinpath(filename)  # use pathlib to join paths

    # Create the folder if it doesn't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Parse CSV data
    csv_data = parse_csv_data(data)

    with file_path.open('w', newline='', encoding='utf-8-sig') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(csv_data)
        print(f"CSV data saved to {file_path}")

def write_excel_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)  # use pathlib to join paths

    # Create the folder if it doesn't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

def write_json_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)  # use pathlib to join paths

    # Create the folder if it doesn't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open('wb') as file:
        file.write(data)
        print(f"Binary data saved to {file_path}")

#Function 1: Process text data

def process_txt_file(folder_name, input_filename, output_filename):
    # Fetch the data
    txt_url = 'https://shakespeare.mit.edu/twelfth_night/full.html'
    response = requests.get(txt_url)
    
    if response.status_code == 200:
        data = response.text
        write_txt_file(folder_name, input_filename, data)
        processed_data = data  
        write_txt_file(folder_name, output_filename, processed_data)
    else:
        print(f"Failed to fetch data: {response.status_code}")

#Function 2. Process CSV Data

def parse_csv_data(csv_text):
    csv_data = []
    csv_reader = csv.reader(StringIO(csv_text))
    for row in csv_reader:
        csv_data.append(row)
    return csv_data

def process_csv_file(csv_folder_name, input_filename, output_filename):
    # Fetch the data
    csv_url = 'https://github.com/ValdisW/datasets/blob/master/video-game-sales.csv'
    response = requests.get(csv_url)
    
    if response.status_code == 200:
        data = response.text
        write_csv_file(csv_folder_name, input_filename, data)
        processed_data = data 
        write_csv_file(csv_folder_name, output_filename, processed_data)
    else:
        print(f"Failed to fetch data: {response.status_code}")

#Function 3: Process Excel Data

def process_excel_file(excel_folder_name, input_filename, output_filename):
    # Fetch the data
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/blob/master/fullmoon.xls'
    response = requests.get(excel_url)
    
    if response.status_code == 200:
        data = response.content
        write_excel_file(excel_folder_name, input_filename, data)

        # Use pandas to read Excel data directly from binary data
        excel_data = pd.read_excel(io.BytesIO(data), sheet_name='Sheet1')  # Update 'Sheet1' to the actual sheet name

        # Convert the read Excel data to CSV format
        processed_data = excel_data.to_csv(index=False)
        
        # Write the processed data to a CSV file
        csv_output_filename = output_filename.replace('.xls', '.csv')
        write_csv_file(excel_folder_name, csv_output_filename, processed_data)
        
    else:
        print(f"Failed to fetch data: {response.status_code}")

#Function 4: Process Json Data

def process_json_file(json_folder_name, input_filename, output_filename):
    # Fetch the data
    json_url = 'https://github.com/LearnWebCode/json-example/blob/master/animals-1.json'
    response = requests.get(json_url)
    
    if response.status_code == 200:
        data = response.content
        write_json_file(json_folder_name, input_filename, data)
        write_json_file(json_folder_name, output_filename, data)
       
    else:
        print(f"Failed to fetch data: {response.status_code}")

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

    txt_url = 'https://shakespeare.mit.edu/twelfth_night/full.html'

    csv_url = 'https://github.com/ValdisW/datasets/blob/master/video-game-sales.csv' 

    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/blob/master/fullmoon.xls' 
    
    json_url = 'https://github.com/LearnWebCode/json-example/blob/master/animals-1.json'

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