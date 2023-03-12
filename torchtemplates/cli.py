import click
import shutil
from jinja2 import Environment, FileSystemLoader

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', default='World', help='The name to greet')
def hello(name):
    click.echo(f'Hello {name}!')


if __name__ == "__main__":
    cli()

