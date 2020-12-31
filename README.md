# databricks-workspace-cleaner

dwc is a tool to clear run cells from notebooks, for example where there might be concern about data held in run cells, or as preparation for commit to source control.

You can also use it to import/export multiple notebooks with this capability, in use cases where dbc export may not be possible due to volume limits.

## Installation

In a python 3.7 environment install this repository, e.g:
pip install git+https://github.com/frogrammer/fire-commands.git

## Databricks Workspace Login

The dwc CLI is built using the databricks CLI sdk https://github.com/databricks/databricks-cli, and uses its authentication mechanism to login to a workspace.
To login to an azure databricks workspace using a user token:

echo MY_TOKEN >> token.txt
databricks configure --host MY_HOST -f token.txt
rm token.txt 

## Commands
|Command|Sub-Command|Parameters|Description|
|--------|---------|--------|--------|
|list|notebooks||List all notebooks in workspace.|
|list|libraries||List all libraries in workspace.|
|export|notebooks|path: location to output zip of notebooks|Exports all notebooks from a workspace as base64 source code. The process will remove annotations for run cells|
|import|notebooks|path: location of notebooks.zip|import notebooks into workspace, overwriting existing.|
|clean|folders||Delete all empty folders in workspace.|
|clean|notebooks||Remove annotations for run cells from all notebooks in workspace.|