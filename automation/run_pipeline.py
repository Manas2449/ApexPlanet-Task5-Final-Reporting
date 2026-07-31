"""
===========================================================
ApexPlanet Data Analytics Internship
Professional Automation Pipeline

Author : Srinivas
===========================================================
"""

from datetime import datetime
import pandas as pd

from config import (
    OUTPUT_DIR,
    LOG_DIR,
    DATASET_PATH,
    SUMMARY_REPORT,
    PIPELINE_LOG,
)

from utils import (
    create_directories,
    validate_dataset,
    load_dataset,
    export_summary,
    write_log,
)


def export_dataset_info(df):
    """Export dataset information."""

    info_file = OUTPUT_DIR / "dataset_info.txt"

    with open(info_file, "w", encoding="utf-8") as f:
        f.write("DATASET INFORMATION\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Rows    : {df.shape[0]}\n")
        f.write(f"Columns : {df.shape[1]}\n\n")

        f.write("Data Types\n")
        f.write("-" * 60 + "\n")
        f.write(df.dtypes.to_string())


def export_missing_values(df):
    """Export missing value report."""

    missing_file = OUTPUT_DIR / "missing_values.txt"

    with open(missing_file, "w", encoding="utf-8") as f:
        f.write("MISSING VALUE REPORT\n")
        f.write("=" * 60 + "\n\n")
        f.write(df.isnull().sum().to_string())


def export_statistics(df):
    """Export descriptive statistics."""

    stats_file = OUTPUT_DIR / "descriptive_statistics.txt"

    with open(stats_file, "w", encoding="utf-8") as f:
        f.write(df.describe(include="all").to_string())


def export_correlation(df):
    """Export correlation matrix."""

    numeric = df.select_dtypes(include="number")

    correlation = numeric.corr()

    correlation.to_csv(
        OUTPUT_DIR / "correlation_matrix.csv",
        index=True,
    )


def pipeline_status():
    """Generate pipeline completion report."""

    status_file = OUTPUT_DIR / "pipeline_status.txt"

    with open(status_file, "w", encoding="utf-8") as f:
        f.write("PIPELINE STATUS\n")
        f.write("=" * 60 + "\n\n")
        f.write("Status : SUCCESS\n")
        f.write(
            f"Completed : {datetime.now()}\n"
        )


def main():

    print("=" * 65)
    print(" ApexPlanet Professional Automation Pipeline ")
    print("=" * 65)

    create_directories(
        OUTPUT_DIR,
        LOG_DIR,
    )

    write_log(
        PIPELINE_LOG,
        "Pipeline Started",
    )

    validate_dataset(DATASET_PATH)

    write_log(
        PIPELINE_LOG,
        "Dataset Validated",
    )

    df = load_dataset(DATASET_PATH)

    write_log(
        PIPELINE_LOG,
        "Dataset Loaded",
    )

    export_summary(
        df,
        SUMMARY_REPORT,
    )

    export_dataset_info(df)

    export_missing_values(df)

    export_statistics(df)

    export_correlation(df)

    pipeline_status()

    write_log(
        PIPELINE_LOG,
        "Reports Generated",
    )

    write_log(
        PIPELINE_LOG,
        "Pipeline Completed Successfully",
    )

    print("\nPipeline Executed Successfully.\n")

    print("Generated Files")

    print("-----------------------------")

    for file in OUTPUT_DIR.iterdir():
        print(f"✔ {file.name}")

    print("\nDone.")


if __name__ == "__main__":
    main()