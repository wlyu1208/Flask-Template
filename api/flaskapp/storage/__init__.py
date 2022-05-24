from pathlib import Path

import click
from flask import current_app
from flask.cli import with_appcontext

@click.group('storage', help='Manage storage.')
def storage_cli():
    pass

@storage_cli.command(help='Initialize storage')
@with_appcontext
def init():
    if current_app.config['STORAGE_TYPE'] == 'local':
        root_path = Path(current_app.config['STORAGE_PATH'])
        dataset_path = root_path / 'dataset'
        current_app.logger.debug(f'Make directory {dataset_path}')
        dataset_path.mkdir(parents=True, exist_ok=True)
    else:
        raise ValueError(f"{current_app.config['STORAGE_TYPE']} is unknown storage type.")
    click.echo('Storage is initialized.')