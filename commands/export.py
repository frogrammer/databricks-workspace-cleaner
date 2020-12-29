from utils.nbconvert import clean_notebook_processor
from utils.db import list_all_notebooks, export
from utils.commands import CommandRegistry
import json
from io import BytesIO
from zipfile import ZipFile

def export_notebooks(export_path:str = None):
    notebook_list = list_all_notebooks()
    notebook_objs = export(notebook_list)
    with ZipFile('notebooks.zip', 'w') as z:
        for idx, notebook in enumerate(notebook_objs):
            notebook_str = json.dumps(notebook)
            z.writestr(idx + '.json', notebook_str)
    print('done')
    


export_commands = {
    'export': {
        'notebooks': export_notebooks
    }
}

CommandRegistry.register(export_commands)