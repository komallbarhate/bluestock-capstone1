from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parent


def run_script(script_name):
    script_path = PROJECT_ROOT / script_name

    if not script_path.exists():
        raise FileNotFoundError(f"Script not found: {script_path}")

    print(f"\nRunning {script_name}...")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"{script_name} failed with exit code {result.returncode}"
        )

    print(f"{script_name} completed successfully.")


def main():
    print("=" * 60)
    print("BLUESTOCK MUTUAL FUND ANALYTICS PIPELINE")
    print("=" * 60)

    scripts = [
        "data_ingestion.py",
        "live_nav_fetch.py",
        "clean_data.py",
        "load_database.py"
    ]

    for script in scripts:
        run_script(script)

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()