import click
import logging
from .calculator import Calculator
from .logger import get_logger

logger = get_logger(__name__)

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

def set_logging_level(debug):
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug logging enabled.")
    else:
        logger.setLevel(logging.INFO)

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging.")
def add(a, b, debug):
    set_logging_level(debug)
    calc = Calculator()
    result = calc.add(a, b)
    click.echo(f"Result: {result}")


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging.")
def sub(a, b, debug):
    set_logging_level(debug)
    calc = Calculator()
    result = calc.sub(a, b)
    click.echo(f"Result: {result}")


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging.")
def mul(a, b, debug):
    set_logging_level(debug)
    calc = Calculator()
    result = calc.mul(a, b)
    click.echo(f"Result: {result}")


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging.")
def div(a, b, debug):
    set_logging_level(debug)
    calc = Calculator()
    try:
        result = calc.div(a, b)
        click.echo(f"Result: {result}")
    except ValueError as e:
        logger.error(f"Error: {e}")


@cli.command()
def interactive():
    """Run in interactive mode."""
    click.echo("Interactive mode. Type 'exit' or 'quit' to end.")
    calc = Calculator()
    while True:
        try:
            line = click.prompt(">>>", type=str, prompt_suffix=" ").strip()
            if line.lower() in ["exit", "quit"]:
                break

            parts = line.split()
            if len(parts) != 3:
                click.echo("Invalid input. Usage: <command> <num1> <num2>")
                continue

            command = parts[0].lower()
            try:
                num1 = float(parts[1])
                num2 = float(parts[2])
            except ValueError:
                click.echo("Invalid numbers. Please enter numeric values.")
                continue

            if command == "add":
                result = calc.add(num1, num2)
                click.echo(f"Result: {result}")
            elif command == "sub":
                result = calc.sub(num1, num2)
                click.echo(f"Result: {result}")
            elif command == "mul":
                result = calc.mul(num1, num2)
                click.echo(f"Result: {result}")
            elif command == "div":
                try:
                    result = calc.div(num1, num2)
                    click.echo(f"Result: {result}")
                except ValueError as e:
                    click.echo(f"Error: {e}")
            else:
                click.echo(f"Unknown command: {command}")

        except Exception as e:
            click.echo(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    cli()



if __name__ == "__main__":
    cli()
