from utils.db import list_all_notebooks, ws_export, ws_import
from utils.commands import CommandRegistry
import json
from io import BytesIO
from zipfile import ZipFile

def clean_notebooks(path:str = 'notebooks.zip'):
    notebook_list = list_all_notebooks()
    notebook_objs = ws_export(notebook_list)
    for notebook_obj in notebook_objs:
        ws_import(notebook_obj)
 
    print('done')
    


clean_commands = {
    'clean': {
        'notebooks': clean_notebooks
    }
}

CommandRegistry.register(clean_commands)
