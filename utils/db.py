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

def list_all_notebooks():
    cli = get_client()
    ws = WorkspaceService(cli)
    all_notebooks = ws.list('/')['objects']
    while len([o for o in all_notebooks if o['object_type'] == 'DIRECTORY']):
        for dir in [o for o in all_notebooks if o['object_type'] == 'DIRECTORY']:
            dir_notebooks = []
            try:
                dir_notebooks = ws.list(dir['path'])['objects']
            except KeyError:
                pass

            all_notebooks = all_notebooks + dir_notebooks
            all_notebooks.remove(dir)
            del dir
    return all_notebooks
