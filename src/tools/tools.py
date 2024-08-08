import sys, os, csv
from datetime import datetime

def write_csv(data, filename):

    with open(os.path.join(filename), mode='w', newline="") as file:
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


 
    
