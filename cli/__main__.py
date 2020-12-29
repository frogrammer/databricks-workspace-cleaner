from fire import Fire
from utils import db
from utils.commands import CommandRegistry
from commands import *  # noQA

def main():
    Fire(CommandRegistry.commands(), name="dwc")

if __name__ == '__main__':
    main()
