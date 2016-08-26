# -*- coding: utf-8 -*-

import click

command_name = 'example'
short_help_message = "This is an example command."

@click.command(command_name, short_help=short_help_message)
def command():
    """Example command."""
    click.echo('Hello World ! This is an example command')
