"""Shimpy"""

import time
import arrow
import click

from .node import commands as node
# from .account import commands as account
# from .address import commands as address

@click.group()
def shimpy():
    pass

shimpy.add_command(node.info)
# shimpy.add_command(address.version)
