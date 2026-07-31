"""
===========================================================
ApexPlanet Data Analytics Internship
Utility Functions
Author : Srinivas
===========================================================
"""

from pathlib import Path
from datetime import datetime
import pandas as pd


# ---------------------------------------------------------
# Create Required Directories
# ---------------------------------------------------------

def create_directories(*directories):
    """
    Create project directories if they do not exist.
    """
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------
# Log Messages
# ---------------------------------------------------------

def write_log(log_file, message):
    """
    Write timestamped messages to the pipeline log.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")


# ---------------------------------------------------------
# Validate Dataset
# ---------------------------------------------------------

def validate_dataset(dataset_path):
    """
    Validate whether the dataset exists.
    """
    if not Path(dataset_path).exists():
        raise FileNotFoundError(
            f"Dataset not found:\n{dataset_path}"
        )


# ---------------------------------------------------------
# Load Dataset
# ---------------------------------------------------------

def load_dataset(dataset_path):
    """
    Load CSV dataset into a pandas DataFrame.
    """
    return pd.read_csv(dataset_path)


# ---------------------------------------------------------
# Export Dataset Summary
# ---------------------------------------------------------

def export_summary(df, output_file):
    """
    Export dataset summary statistics.
    """
    with open(output_file, "w", encoding="utf-8") as file:

        file.write("DATASET SUMMARY\n")
        file.write("=" * 50 + "\n\n")

        file.write(f"Rows    : {df.shape[0]}\n")
        file.write(f"Columns : {df.shape[1]}\n\n")

        file.write("Column Names\n")
        file.write("-" * 50 + "\n")

        for column in df.columns:
            file.write(f"- {column}\n")

        file.write("\n")

        file.write("Descriptive Statistics\n")
        file.write("-" * 50 + "\n")

        file.write(df.describe(include="all").to_string())