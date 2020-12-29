from fire import Fire
from utils import db
from utils.commands import CommandRegistry
from commands import *  # noQA
from databricks_cli.utils import InvalidConfigurationError

def main():
    try:
        Fire(CommandRegistry.commands(), name="dwc")
    except InvalidConfigurationError:
        print('Please configure databricks CLI using command "databricks configure".')
        pass

if __name__ == '__main__':
    main()
