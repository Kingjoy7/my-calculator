"""
Integration Tests - CLI + Calculator Working Together
"""
import subprocess
import sys
import pytest


class TestCLIIntegration:
    """Integration tests for CLI calculator."""

    def run_cli(self, *args):
        """Run the CLI with given arguments and capture output."""
        cmd = [sys.executable, "src/cli.py"] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        return result

    def test_cli_add_integration(self):
        result = self.run_cli("add", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "8"

    def test_cli_subtract_integration(self):
        result = self.run_cli("subtract", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "2"

    def test_cli_multiply_integration(self):
        result = self.run_cli("multiply", "4", "7")
        assert result.returncode == 0
        assert result.stdout.strip() == "28"

    def test_cli_divide_integration(self):
        result = self.run_cli("divide", "15", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "5"

    def test_cli_sqrt_integration(self):
        result = self.run_cli("sqrt", "16")
        assert result.returncode == 0
        assert result.stdout.strip() == "4"

    def test_cli_subtract_missing_operand_error(self):
        result = self.run_cli("subtract", "5")
        assert result.returncode == 1
        assert result.stdout.strip().startswith("Operation 'subtract' requires two numbers.")

    def test_cli_divide_zero_error(self):
        result = self.run_cli("divide", "10", "0")
        assert result.returncode == 1
        assert "Cannot divide by zero" in result.stdout

    def test_cli_unknown_operation_error(self):
        result = self.run_cli("invalid", "1", "2")
        assert result.returncode == 1
        assert "Unknown operation" in result.stdout


class TestCalculatorModuleIntegration:
    """Integration tests for calculator module functions."""

    def test_chained_operations(self):
        """Test using results from one operation in another."""
        from src.calculator import add, multiply, divide
        step1 = add(5, 3)         # 8
        step2 = multiply(step1, 2)  # 16
        step3 = divide(step2, 4)    # 4
        assert step3 == 4.0

    def test_complex_calculation_integration(self):
        """Test complex calculation using multiple functions."""
        from src.calculator import power, square_root, add
        a_squared = power(3, 2)       # 9
        b_squared = power(4, 2)       # 16
        sum_squares = add(a_squared, b_squared)  # 25
        hypotenuse = square_root(sum_squares)    # 5
        assert hypotenuse == 5.0