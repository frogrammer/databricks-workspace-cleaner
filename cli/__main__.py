from fire import Fire
from utils import db

def main():
    client = db.get_client()
    notebooks = db.list_all_notebooks()
    # Fire(name="dwc")

if __name__ == '__main__':
    main()
