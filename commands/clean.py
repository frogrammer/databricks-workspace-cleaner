from utils.stdout import stdout_print
from utils.db import list_all_notebooks, ws_export, ws_import, delete_empty_folders
from firehelper import CommandRegistry
import json
from io import BytesIO
from zipfile import ZipFile
from tabulate import tabulate

def clean_notebooks():
    notebook_list = list_all_notebooks()
    notebook_objs = ws_export(notebook_list)
    for notebook_obj in notebook_objs:
        ws_import(notebook_obj)
    stdout_print(tabulate(notebook_list))

def clean_empty_folders():
    folders = delete_empty_folders()
    stdout_print(tabulate(folders))



clean_commands = {
    'clean': {
        'notebooks': clean_notebooks,
        'folders': clean_empty_folders
    }
}

CommandRegistry.register(clean_commands)
