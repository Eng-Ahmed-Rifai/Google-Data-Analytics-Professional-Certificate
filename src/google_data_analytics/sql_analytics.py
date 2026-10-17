"""SQL Analytics Query Builders and Templates for BigQuery.

Contains standardized, reusable SQL analytical patterns for cohort retention,
rolling moving averages, and data cleansing operations.
"""

class BigQueryAnalyticsTemplates:
    """Standardized SQL query templates for data analysts."""

    @staticmethod
    def rolling_average_query(table_name: str, date_col: str, metric_col: str, window_days: int = 7) -> str:
        """Generate rolling moving average query."""
        return f"""
SELECT
    {date_col},
    {metric_col},
    AVG({metric_col}) OVER (
        ORDER BY {date_col}
        ROWS BETWEEN {window_days - 1} PRECEDING AND CURRENT ROW
    ) AS rolling_avg_{window_days}d
FROM
    `{table_name}`
ORDER BY
    {date_col} ASC;
""".strip()

    @staticmethod
    def deduplication_query(table_name: str, partition_cols: str, order_col: str) -> str:
        """Generate deduplication query using ROW_NUMBER() window function."""
        return f"""
WITH RankedRecords AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY {partition_cols}
            ORDER BY {order_col} DESC
        ) AS rank_index
    FROM
        `{table_name}`
)
SELECT
    * EXCEPT(rank_index)
FROM
    RankedRecords
WHERE
    rank_index = 1;
""".strip()
