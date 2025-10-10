import subprocess
import sys
import pytest


class TestCLIIntegration:
    """Integration tests for CLI calculator."""

    def run_cli(self, *args):
        """Run the CLI with given arguments and capture output."""
        cmd = [sys.executable, "src/cli.py"] + list(args)  # ✅ cli.py, not main.py
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

    def test_cli_subtract_missing_operand_error(self):
        result = self.run_cli("subtract", "5")
        assert result.returncode == 1
        assert result.stdout.strip().startswith(
            "Operation 'subtract' requires two numbers."
        )

    def test_cli_unknown_operation_error(self):
        result = self.run_cli("unknown", "5", "3")
        assert result.returncode == 1
        assert result.stdout.strip().startswith("Unknown operation:")

    def test_cli_sqrt_integration(self):
        result = self.run_cli("sqrt", "16")
        assert result.returncode == 0
        assert result.stdout.strip() == "4"

    def test_cli_divide_zero_error(self):
        result = self.run_cli("divide", "5", "0")
        assert result.returncode == 1
        assert "Error:" in result.stdout.strip()
