from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
TASK_FILES = [ROOT / f"task_{i}.py" for i in range(1, 6)]


def run_script(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True,
        cwd=ROOT,
        timeout=5,
    )


def test_task_files_exist() -> None:
    for path in TASK_FILES:
        assert path.exists(), f"Не найден файл {path.name}"


def test_task_files_run_without_error() -> None:
    for path in TASK_FILES:
        result = run_script(path)
        assert result.returncode == 0, (
            f"{path.name} завершился с ошибкой:\n"
            f"STDOUT:\n{result.stdout}\n"
            f"STDERR:\n{result.stderr}"
        )
