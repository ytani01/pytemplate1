import click
from .calculator import Calculator
from .logger import get_logger

logger = get_logger(__name__)

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('-d', '--debug', is_flag=True, help='Enable debug logging.')
def cli(debug):
    if debug:
        logger.setLevel(click.UNSET)
        logger.debug("Debug logging enabled.")

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def add(a, b):
    calc = Calculator()
    result = calc.add(a, b)
    logger.info(f"Result: {result}")

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def sub(a, b):
    calc = Calculator()
    result = calc.sub(a, b)
    logger.info(f"Result: {result}")

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def mul(a, b):
    calc = Calculator()
    result = calc.mul(a, b)
    logger.info(f"Result: {result}")

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def div(a, b):
    calc = Calculator()
    try:
        result = calc.div(a, b)
        logger.info(f"Result: {result}")
    except ValueError as e:
        logger.error(f"Error: {e}")

if __name__ == '__main__':
    cli()
