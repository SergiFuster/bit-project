from src.tools.tools import *

drawer = "data/files"

def write():
    args = sys.argv[1:]

    data = parse_inputs(args)

    write_csv(data, os.path.join(drawer, f'{today_date()}.csv'))

def read():

    filename = sys.argv[1]

    html = to_html(os.path.join(drawer, f'{filename}.csv'))

    with open(os.path.join(drawer, f'{today_date()}.html'), 'w') as file:
        file.write(html)
if __name__ == "__main__":
    read()