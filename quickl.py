#! /c/Python35/python.exe
# -*- coding: utf-8 -*-

import click
import importlib
import os
import subprocess
import sys

cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))
python_location = sys.executable
quickl_location = os.path.abspath(os.path.join(os.path.dirname(__file__), 'quickl.py'))

class QuicklCommand(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.startswith('cmd_') and os.path.isdir(os.path.join(cmd_folder, filename)):
                rv.append(filename[4:])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        if name not in self.list_commands(ctx):
            #If quickl was invoked with an unknown command, displays help
            subprocess.call([python_location, quickl_location, '--help'])

            #If the unknown command was actually 'help', do not treat it as an error
            if name != 'help':
                print("\nError: quickl has no command '{0}'.".format(name))

            exit()

        mod = importlib.import_module('commands.cmd_{0}.cmd_{0}'.format(name))
        return mod.command

@click.command(cls=QuicklCommand)
@click.pass_context
def quickl(ctx):
    print("")

if __name__ == '__main__':
    quickl(obj={})
