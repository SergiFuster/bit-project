import sys, os, csv, pandas as pd
from datetime import datetime

def to_html(filepath):
    data = read_csv(filepath)
    html = data.to_html()
    return html

def read_csv(filepath):
    try:
        data = pd.read_csv(filepath)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    return data

def write_csv(data, filepath):

    with open(os.path.join(filepath), mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def parse_inputs(args):

    if not args:
        print("No arguments provided")
        sys.exit(1)

    try:        
        data = [arg.split(',') for arg in args]
    except ValueError:
        print("All arguments must be lists")
        sys.exit(1)
    return data

def today_date():
    return datetime.now().strftime("%Y-%m-%d")


 
    
