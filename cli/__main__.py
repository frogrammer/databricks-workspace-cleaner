import argparse
from utils import db
from utils.commands import start_fire_cli
from commands import *  # noQA
from databricks_cli.utils import InvalidConfigurationError
import sys

def main():
    try:
        start_fire_cli('dwc')
    except InvalidConfigurationError:
        print('Please configure databricks CLI using command "databricks configure --token".')
        pass

if __name__ == '__main__':
    main()
