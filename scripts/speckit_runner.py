import shutil
import subprocess
from pathlib import Path


def has_specify() -> bool:
    return shutil.which("specify") is not None


def run_specify(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["specify", *args], cwd=str(cwd), text=True, capture_output=True, check=False)


def install_command() -> str:
    return "uv tool install specify-cli --from git+https://github.com/github/spec-kit.git"

