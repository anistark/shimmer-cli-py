import click

@click.group()
def address():
    pass

@address.command()
def new():
    """Create New Address for Account"""
    click.echo("New Address for Account")
