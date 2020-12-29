from fire import Fire
from utils import db
from utils.commands import CommandRegistry
from commands import *  # noQA
from databricks_cli.utils import InvalidConfigurationError

def main():
    try:
        Fire(CommandRegistry.commands(), name="dwc")
    except InvalidConfigurationError:
        raise 'Please configure databricks CLI using command "databricks configure".'

if __name__ == '__main__':
    main()
