"""Data access layer for the Streamlit sales dashboard.

Single responsibility: load df_master.parquet (cached) and apply user filters.
Kept thin on purpose — all viz/aggregation logic lives in streamlit_app.py.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Iterable

import pandas as pd
import streamlit as st


DATA_PATH = Path(__file__).parent.parent / "output" / "df_master.parquet"


@st.cache_data(show_spinner="Loading 110k transactions…")
def load_master() -> pd.DataFrame:
    df = pd.read_parquet(DATA_PATH)
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    df["order_date"] = df["order_purchase_timestamp"].dt.date
    df["order_month_str"] = df["order_purchase_timestamp"].dt.to_period("M").astype(str)
    return df


def apply_filters(
    df: pd.DataFrame,
    *,
    date_range: tuple[date, date] | None = None,
    states: Iterable[str] | None = None,
    categories: Iterable[str] | None = None,
    payment_types: Iterable[str] | None = None,
) -> pd.DataFrame:
    mask = pd.Series(True, index=df.index)
    if date_range:
        start, end = date_range
        mask &= df["order_date"].between(start, end)
    if states:
        mask &= df["customer_state"].isin(list(states))
    if categories:
        mask &= df["category"].isin(list(categories))
    if payment_types:
        mask &= df["payment_type"].isin(list(payment_types))
    return df.loc[mask]
