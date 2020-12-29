from databricks_cli.configure import provider as db_cfg
from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.sdk.service import WorkspaceService

def get_config():
    return db_cfg.get_config()

def get_client():
    cfg = get_config()
    api_opts = {
        'user': cfg.username,
        'password': cfg.password,
        'host': cfg.host,
        'token': cfg.token
    }

    return ApiClient(**api_opts)

def __list_all():
    cli = get_client()
    ws = WorkspaceService(cli)
    all_obj = ws.list('/')['objects']
    while len([o for o in all_obj if o['object_type'] == 'DIRECTORY']):
        for dir in [o for o in all_obj if o['object_type'] == 'DIRECTORY']:
            dir_obj = []
            try:
                dir_obj = ws.list(dir['path'])['objects']
            except KeyError:
                pass

            all_obj = all_obj + dir_obj
            all_obj.remove(dir)
            del dir
    return all_obj


def list_all_notebooks():
    all_obj = __list_all()
    return [o for o in all_obj if o['object_type'] == 'NOTEBOOK']


def list_all_libraries():
    all_obj = __list_all()
    return [o for o in all_obj if o['object_type'] == 'LIBRARY']


def ws_export(list_of_objects):
    cli = get_client()
    ws = WorkspaceService(cli)
    export_objs = []
    for path in [o['path'] for o in list_of_objects]:
        export_obj = ws.export_workspace(path)
        export_obj['path'] = path
        export_objs = export_objs + [export_obj]
    return export_objs


def ws_import(obj: dict):
    cli = get_client()
    ws = WorkspaceService(cli)
    args = obj
    permitted_languages = ['SCALA', 'SQL', 'PYTHON', 'R']
    try:
        args['language'] = [l for l in permitted_languages if l.lower().startswith(obj['file_type'])][0]
    except:
        raise 'language' + obj['language'] + 'not permitted.'
    args['overwrite'] = True
    args['format'] = 'SOURCE'
    del args['file_type']
    ws.mkdirs('/'.join(args['path'].split('/')[:-1]))
    ws.import_workspace(**args)