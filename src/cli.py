import sys
import click
from calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI supporting basic operations."""
    try:
        # Define operation mapping
        operations = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide,
            "power": power,
            "sqrt": square_root,
        }

        # Check if the operation exists
        if operation not in operations:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Handle operations that require one or two numbers
        if operation == "sqrt":
            result = operations[operation](num1)
        else:
            if num2 is None:
                click.echo(f"Operation '{operation}' requires two numbers.")
                sys.exit(1)
            result = operations[operation](num1, num2)

        # Format and display result
        click.echo(int(result) if result == int(result) else f"{result:.2f}")

    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
