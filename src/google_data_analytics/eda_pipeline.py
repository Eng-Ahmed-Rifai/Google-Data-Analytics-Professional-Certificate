"""Exploratory Data Analysis and Cleaning Pipeline.

Implements automated schema validation, missing value diagnosis, outlier detection,
and statistical summary generation for tabular business data.
"""

from typing import Dict, Any, List
import pandas as pd
import numpy as np


class DataQualityAudit:
    """Automated data profiling and validation auditor."""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def summary_profile(self) -> Dict[str, Any]:
        """Generate high-level profile of dataframe."""
        total_rows, total_cols = self.df.shape
        missing_counts = self.df.isnull().sum()
        missing_pct = (missing_counts / total_rows) * 100
        duplicate_rows = self.df.duplicated().sum()

        column_report = {}
        for col in self.df.columns:
            column_report[col] = {
                "dtype": str(self.df[col].dtype),
                "null_count": int(missing_counts[col]),
                "null_percentage": round(float(missing_pct[col]), 2),
                "unique_values": int(self.df[col].nunique())
            }

        return {
            "total_records": total_rows,
            "total_columns": total_cols,
            "duplicate_rows": int(duplicate_rows),
            "duplicate_percentage": round(float((duplicate_rows / total_rows) * 100), 2) if total_rows > 0 else 0.0,
            "columns": column_report
        }

    def detect_outliers_iqr(self, numeric_column: str, multiplier: float = 1.5) -> pd.Series:
        """Identify outliers using the Interquartile Range (IQR) technique."""
        if numeric_column not in self.df.columns:
            raise KeyError(f"Column '{numeric_column}' not found.")
        series = self.df[numeric_column].dropna()
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - (multiplier * iqr)
        upper_bound = q3 + (multiplier * iqr)
        return self.df[(self.df[numeric_column] < lower_bound) | (self.df[numeric_column] > upper_bound)]
