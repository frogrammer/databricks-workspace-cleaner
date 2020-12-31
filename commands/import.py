from utils.db import ws_import
from firehelper import CommandRegistry
import json
from io import BytesIO
from zipfile import ZipFile, ZipInfo


def import_notebooks(path = 'notebooks.zip', import_prefix = 'IMPORT'):
    with ZipFile(path, 'r') as z:
        for fn in z.namelist():
            with z.open(fn) as f:
                notebook_obj = json.loads(f.read())
                notebook_obj['path'] = '/' + import_prefix + notebook_obj['path']
                ws_import(notebook_obj)
 
import_commands = {
    'import': {
        'notebooks': import_notebooks
    }
}

CommandRegistry.register(import_commands)
