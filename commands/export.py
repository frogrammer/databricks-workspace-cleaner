from utils.db import list_all_notebooks, ws_export
from utils.commands import CommandRegistry
import json
from io import BytesIO
from zipfile import ZipFile

def export_notebooks(path:str = 'notebooks.zip'):
    notebook_list = list_all_notebooks()
    notebook_objs = ws_export(notebook_list)
    with ZipFile(path, 'w') as z:
        for idx, notebook in enumerate(notebook_objs):
            notebook_str = json.dumps(notebook)
            z.writestr(str(idx) + '.json', notebook_str)
    print('done')
    


export_commands = {
    'export': {
        'notebooks': export_notebooks
    }
}

CommandRegistry.register(export_commands)
