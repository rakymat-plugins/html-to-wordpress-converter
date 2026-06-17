import os
import shutil
import subprocess
from pathlib import Path


def specify_executable(cwd: Path | None = None) -> str | None:
    found = shutil.which("specify")
    if found:
        return found
    if cwd:
        local = cwd / ".uv-bin" / ("specify.exe" if os.name == "nt" else "specify")
        if local.exists():
            return str(local)
    return None


def has_specify(cwd: Path | None = None) -> bool:
    return specify_executable(cwd) is not None


def has_uv() -> bool:
    return shutil.which("uv") is not None


def uv_env(cwd: Path) -> dict[str, str]:
    env = os.environ.copy()
    env.setdefault("UV_CACHE_DIR", str(cwd / ".uv-cache"))
    env.setdefault("UV_TOOL_DIR", str(cwd / ".uv-tools"))
    env.setdefault("UV_TOOL_BIN_DIR", str(cwd / ".uv-bin"))
    return env


def run_command(command: list[str], cwd: Path, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=str(cwd),
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
        env=env,
    )


def run_specify(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    executable = specify_executable(cwd) or "specify"
    return run_command([executable, *args], cwd)


def run_uv(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return run_command(["uv", *args], cwd, env=uv_env(cwd))


def install_command() -> str:
    return "uv tool install specify-cli --from git+https://github.com/github/spec-kit.git"


def format_result(command: list[str], result: subprocess.CompletedProcess[str]) -> str:
    lines = [
        f"## `{' '.join(command)}`",
        "",
        f"- exit code: `{result.returncode}`",
    ]
    stdout = (result.stdout or "").strip()
    stderr = (result.stderr or "").strip()
    if stdout:
        lines.extend(["", "stdout:", "", "```text", stdout, "```"])
    if stderr:
        lines.extend(["", "stderr:", "", "```text", stderr, "```"])
    return "\n".join(lines)
