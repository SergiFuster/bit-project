from src.tools.tools import *

drawer = "data/files"

def main():
    args = sys.argv[1:]

    data = parse_inputs(args)

    write_csv(data, os.path.join(drawer, f'{today_date()}.csv'))

if __name__ == "__main__":
    main()