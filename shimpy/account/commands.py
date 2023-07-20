import click

@click.group()
def account():
    pass

@account.command()
def new():
    """Create New Wallet Account"""
    click.echo("New Wallet Account")
