import argparse
from fire import Fire
from utils import db
from utils.commands import CommandRegistry
from commands import *  # noQA
from databricks_cli.utils import InvalidConfigurationError
import sys

def main():
    if len(sys.argv) == 1:
        CommandRegistry.print_commands()
    else:
        try:
            Fire(CommandRegistry.commands(), name="dwc")
        except InvalidConfigurationError:
            print('Please configure databricks CLI using command "databricks configure --token".')
            pass

if __name__ == '__main__':
    main()
