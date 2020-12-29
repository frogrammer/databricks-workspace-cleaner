import base64
import nbconvert
from nbconvert.exporters import base


def clean_notebook(content: str):
    return content

def clean_notebook_processor(notebook_obj: dict):
    notebook_content = base64.decodebytes(notebook_obj['content'].encode('utf-8')).decode()
    cleaned_content = clean_notebook(notebook_content)
    notebook_obj['content'] = cleaned_content
    return notebook_obj
