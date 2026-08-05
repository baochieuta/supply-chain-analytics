"""Reusable data cleaning functions for the DataCo supply chain dataset."""
import pandas as pd


def load_raw(path: str) -> pd.DataFrame:
    """Load the raw DataCo CSV, handling its non-UTF-8 encoding."""
    return pd.read_csv(path, encoding="latin-1")


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Placeholder for column standardization, dedup, and type fixes."""
    df = df.drop_duplicates()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df
