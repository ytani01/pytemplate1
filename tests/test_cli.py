from click.testing import CliRunner
from pytemplate1.__main__ import cli


def test_add_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["add", "1", "3"], prog_name="pytemplate1")
    assert result.exit_code == 0
    assert "Result: 4.0\n" == result.stdout


def test_sub_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["sub", "5", "2"], prog_name="pytemplate1")
    assert result.exit_code == 0
    assert "Result: 3.0\n" == result.stdout


def test_mul_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["mul", "2", "3"], prog_name="pytemplate1")
    assert result.exit_code == 0
    assert "Result: 6.0\n" == result.stdout


def test_div_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["div", "6", "2"], prog_name="pytemplate1")
    assert result.exit_code == 0
    assert "Result: 3.0\n" == result.stdout


def test_div_by_zero_command(caplog):
    runner = CliRunner()
    result = runner.invoke(cli, ["div", "6", "0"], prog_name="pytemplate1")
    assert (
        result.exit_code == 0
    )  # Click commands usually exit with 0 even on error if handled
    assert any("Error: Cannot divide by zero!" in r.message for r in caplog.records)


def test_debug_option(caplog):
    runner = CliRunner()
    result = runner.invoke(cli, ["add", "1", "1", "-d"], prog_name="pytemplate1")
    assert result.exit_code == 0
    assert any("Debug logging enabled." in r.message for r in caplog.records)
    assert "Result: 2.0\n" == result.stdout


def test_help_option():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"], prog_name="pytemplate1")
    assert result.exit_code == 0
    assert "Usage: pytemplate1 [OPTIONS] COMMAND [ARGS]..." in result.stdout


def test_interactive_mode():
    runner = CliRunner()
    result = runner.invoke(
        cli, ["interactive"], input="add 1 2\nsub 5 3\nexit\n", prog_name="pytemplate1"
    )
    assert result.exit_code == 0
    assert "Interactive mode. Type 'exit' or 'quit' to end.\n" in result.stdout
    assert "Result: 3.0\n" in result.stdout
    assert "Result: 2.0\n" in result.stdout
