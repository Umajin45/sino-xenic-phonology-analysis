from pathlib import Path
import pandas as pd

# Project root detection
ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"


def load_raw_csv(filename: str) -> pd.DataFrame:
    """Load a CSV file from data/raw."""
    return pd.read_csv(RAW_DIR / filename)


def load_processed_csv(filename: str) -> pd.DataFrame:
    """Load a CSV file from data/processed."""
    return pd.read_csv(PROCESSED_DIR / filename)

