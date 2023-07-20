import click

@click.group()
def nft():
    pass

@nft.command()
def mint():
    """Mint New NFT"""
    click.echo("Mint NFT")
