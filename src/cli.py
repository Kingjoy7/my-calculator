import sys
import click
from calculator import add, subtract, multiply, divide, power, square_root

def perform_calculation(operation, num1, num2=None):
    """Simple calculator logic handler."""
    try:
        if operation == "add":
            return add(num1, num2)
        elif operation == "subtract":
            return subtract(num1, num2)
        elif operation == "multiply":
            return multiply(num1, num2)
        elif operation == "divide":
            return divide(num1, num2)
        elif operation == "power":
            return power(num1, num2)
        elif operation == "square_root" or operation == "sqrt":
            return square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)
    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)

@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI supporting basic operations."""
    if operation in ["sqrt", "square_root"]:
        result = perform_calculation(operation, num1)
    else:
        if num2 is None:
            click.echo(f"Operation '{operation}' requires two numbers.")
            sys.exit(1)
        result = perform_calculation(operation, num1, num2)

    click.echo(int(result) if result == int(result) else f"{result:.2f}")

if __name__ == "__main__":
    calculate()