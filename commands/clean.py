from firehelper import CommandRegistry
from tabulate import tabulate
from utils.db import (delete_empty_folders, list_all_notebooks, ws_export_list,
                      ws_import)


def clean_notebooks():
    notebook_list = list_all_notebooks()
    [ws_import(notebook['path'], notebook['language'], 'SOURCE', notebook['obj']['content'], True) for notebook in ws_export_list(notebook_list, format='SOURCE')]
    print(tabulate([[notebook['path'], notebook['language']]for notebook in notebook_list]))

def clean_empty_folders():
    folders = delete_empty_folders()
    print(tabulate(folders))



clean_commands = {
    'clean': {
        'notebooks': clean_notebooks,
        'folders': clean_empty_folders
    }
}

CommandRegistry.register(clean_commands)
