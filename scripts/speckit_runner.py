import shutil
import subprocess
from pathlib import Path


def has_specify() -> bool:
    return shutil.which("specify") is not None


def has_uv() -> bool:
    return shutil.which("uv") is not None


def run_command(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=str(cwd), text=True, capture_output=True, check=False)


def run_specify(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return run_command(["specify", *args], cwd)


def run_uv(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return run_command(["uv", *args], cwd)


def install_command() -> str:
    return "uv tool install specify-cli --from git+https://github.com/github/spec-kit.git"


def format_result(command: list[str], result: subprocess.CompletedProcess[str]) -> str:
    lines = [
        f"## `{' '.join(command)}`",
        "",
        f"- exit code: `{result.returncode}`",
    ]
    stdout = result.stdout.strip()
    stderr = result.stderr.strip()
    if stdout:
        lines.extend(["", "stdout:", "", "```text", stdout, "```"])
    if stderr:
        lines.extend(["", "stderr:", "", "```text", stderr, "```"])
    return "\n".join(lines)
