from click.testing import CliRunner

from shimpy.cli import shimpy

def test_shimpy_cli():
    runner = CliRunner()
    result = runner.invoke(shimpy, ["Asia/Kolkata"])
    assert result.exit_code == 0
    assert "Hello, India!" in result.output
