import click

from xander.cli import config
from xander.cli.banner import banner

@click.group()
def main():
    '''
    Summary:
    xander network device config builder.
    '''
    banner()

main.add_command(config.config, name = 'config')