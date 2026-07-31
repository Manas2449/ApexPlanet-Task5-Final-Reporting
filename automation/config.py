"""
===========================================================
ApexPlanet Data Analytics Internship
Configuration File
Author : Srinivas
===========================================================
"""

from pathlib import Path

# ---------------------------------------------------------
# Project Paths
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_DIR = PROJECT_ROOT / "datasets"

OUTPUT_DIR = PROJECT_ROOT / "automation" / "outputs"

LOG_DIR = PROJECT_ROOT / "automation" / "logs"

REPORT_DIR = PROJECT_ROOT / "report"

# ---------------------------------------------------------
# Dataset
# ---------------------------------------------------------

DATASET_NAME = "cleaned_supermarket_sales.csv"

DATASET_PATH = DATASET_DIR / DATASET_NAME

# ---------------------------------------------------------
# Output Files
# ---------------------------------------------------------

SUMMARY_REPORT = OUTPUT_DIR / "dataset_summary.txt"

PIPELINE_LOG = LOG_DIR / "pipeline.log"