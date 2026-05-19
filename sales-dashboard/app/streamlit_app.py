"""Interactive sales dashboard — Brazilian E-Commerce (Olist).

Companion to the static notebook dashboard (03_dashboard_final.ipynb).
Built by Ray as part of his Data & AI Analytics portfolio.
"""
from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

from data_loader import apply_filters, load_master


PALETTE = {
    "BLUE":    "#2563EB",
    "LIGHT":   "#93C5FD",
    "LIGHTER": "#DBEAFE",
    "RED":     "#DC2626",
    "AMBER":   "#F59E0B",
    "GREEN":   "#059669",
    "GRAY":    "#6B7280",
    "BG":      "#F8FAFC",
}

st.set_page_config(
    page_title="Sales Dashboard — Ray",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ── Header ────────────────────────────────────────────────────────────────
st.title("📊 Sales Performance Dashboard")
st.caption(
    "Brazilian E-Commerce (Olist) · Sep 2016 – Sep 2018 · Delivered orders only · "
    "Built by Ray ([GitHub](https://github.com/bursiaryn/data-analytics-portfolio))"
)

df = load_master()


# ── Sidebar Filters ───────────────────────────────────────────────────────
with st.sidebar:
    st.header("🔎 Filter")

    min_date, max_date = df["order_date"].min(), df["order_date"].max()
    date_range = st.date_input(
        "Periode",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        format="YYYY-MM-DD",
    )
    if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
        date_range = (date_range[0], date_range[1])
    else:
        date_range = (min_date, max_date)

    all_states = sorted(df["customer_state"].dropna().unique())
    states = st.multiselect("State (negara bagian)", all_states, default=[])

    all_cats = sorted(df["category"].dropna().unique())
    categories = st.multiselect("Kategori produk", all_cats, default=[])

    all_pays = sorted(df["payment_type"].dropna().unique())
    payment_types = st.multiselect("Metode pembayaran", all_pays, default=[])

    st.divider()
    st.caption(
        "💡 Biarkan kosong = semua data. "
        "Filter berlaku langsung ke seluruh chart."
    )


df_f = apply_filters(
    df,
    date_range=date_range,
    states=states or None,
    categories=categories or None,
    payment_types=payment_types or None,
)

if df_f.empty:
    st.warning("Tidak ada data yang cocok dengan filter. Coba longgarkan kriteria.")
    st.stop()


# ── Tabs ──────────────────────────────────────────────────────────────────
tab_dash, tab_id, tab_about = st.tabs(
    ["📊 Dashboard", "🇮🇩 Konteks Indonesia", "ℹ️ About"]
)


# ── TAB: Dashboard ────────────────────────────────────────────────────────
with tab_dash:
    # KPI cards
    total_revenue = df_f["revenue"].sum()
    total_orders = df_f["order_id"].nunique()
    aov = df_f.groupby("order_id")["revenue"].sum().mean()
    avg_score = df_f.drop_duplicates("order_id")["review_score"].mean()
    on_time_rate = 1 - df_f.drop_duplicates("order_id")["is_late"].mean()

    k1, k2, k3, k4, k5 = st.columns(5)
    k1.metric("Total Revenue", f"R$ {total_revenue/1e6:.2f}M")
    k2.metric("Total Orders", f"{total_orders:,}")
    k3.metric("Avg Order Value", f"R$ {aov:,.0f}")
    k4.metric("Avg Review", f"{avg_score:.2f} / 5.0" if pd.notna(avg_score) else "—")
    k5.metric("On-Time Delivery", f"{on_time_rate:.1%}" if pd.notna(on_time_rate) else "—")

    st.divider()

    # Row: revenue trend + top category
    col_trend, col_cat = st.columns([1.4, 1])

    with col_trend:
        st.subheader("Monthly Revenue & Order Volume")
        monthly = (
            df_f.groupby("order_month_str")
            .agg(revenue=("revenue", "sum"), orders=("order_id", "nunique"))
            .reset_index()
            .sort_values("order_month_str")
        )
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(
            go.Scatter(
                x=monthly["order_month_str"],
                y=monthly["revenue"] / 1e6,
                name="Revenue (R$ M)",
                line=dict(color=PALETTE["BLUE"], width=3),
                fill="tozeroy",
                fillcolor="rgba(37,99,235,0.15)",
                hovertemplate="%{x}<br>Revenue: R$ %{y:.2f}M<extra></extra>",
            ),
            secondary_y=False,
        )
        fig.add_trace(
            go.Bar(
                x=monthly["order_month_str"],
                y=monthly["orders"],
                name="Orders",
                marker_color=PALETTE["GRAY"],
                opacity=0.35,
                hovertemplate="%{x}<br>Orders: %{y:,}<extra></extra>",
            ),
            secondary_y=True,
        )
        fig.update_yaxes(title_text="Revenue (R$ Juta)", secondary_y=False)
        fig.update_yaxes(title_text="# Orders", secondary_y=True, showgrid=False)
        fig.update_layout(
            height=380,
            margin=dict(l=0, r=0, t=10, b=0),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
            hovermode="x unified",
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_cat:
        st.subheader("Top 10 Kategori — Revenue")
        cat_rev = (
            df_f.groupby("category")["revenue"].sum()
            .nlargest(10).reset_index()
            .sort_values("revenue")
        )
        fig = px.bar(
            cat_rev,
            x="revenue",
            y="category",
            orientation="h",
            color="revenue",
            color_continuous_scale=[PALETTE["LIGHTER"], PALETTE["BLUE"]],
        )
        fig.update_layout(
            height=380,
            margin=dict(l=0, r=0, t=10, b=0),
            coloraxis_showscale=False,
            yaxis_title=None,
            xaxis_title="Revenue (R$)",
        )
        fig.update_traces(hovertemplate="%{y}<br>R$ %{x:,.0f}<extra></extra>")
        st.plotly_chart(fig, use_container_width=True)

    # Row: state + payment + review
    col_state, col_pay, col_rev = st.columns([1.3, 1, 1])

    with col_state:
        st.subheader("Revenue per State (Top 15)")
        state_rev = (
            df_f.groupby("customer_state")["revenue"].sum()
            .nlargest(15).reset_index()
            .sort_values("revenue")
        )
        fig = px.bar(
            state_rev,
            x="revenue",
            y="customer_state",
            orientation="h",
            color="revenue",
            color_continuous_scale=[PALETTE["LIGHTER"], PALETTE["BLUE"]],
        )
        fig.update_layout(
            height=360,
            margin=dict(l=0, r=0, t=10, b=0),
            coloraxis_showscale=False,
            yaxis_title=None,
            xaxis_title="Revenue (R$)",
        )
        fig.update_traces(hovertemplate="%{y}<br>R$ %{x:,.0f}<extra></extra>")
        st.plotly_chart(fig, use_container_width=True)

    with col_pay:
        st.subheader("Metode Pembayaran")
        pay_dist = (
            df_f.drop_duplicates("order_id")["payment_type"]
            .value_counts()
            .reset_index()
        )
        pay_dist.columns = ["payment_type", "count"]
        fig = px.pie(
            pay_dist,
            names="payment_type",
            values="count",
            hole=0.55,
            color_discrete_sequence=[
                PALETTE["BLUE"], PALETTE["LIGHT"],
                PALETTE["LIGHTER"], "#BFDBFE",
            ],
        )
        fig.update_traces(textposition="outside", textinfo="percent+label")
        fig.update_layout(
            height=360,
            margin=dict(l=0, r=0, t=10, b=0),
            showlegend=False,
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_rev:
        st.subheader("Distribusi Review Score")
        score_dist = (
            df_f.drop_duplicates("order_id")["review_score"]
            .value_counts()
            .sort_index()
            .reset_index()
        )
        score_dist.columns = ["score", "count"]
        score_colors = [
            PALETTE["RED"] if s <= 2
            else (PALETTE["AMBER"] if s == 3 else PALETTE["BLUE"])
            for s in score_dist["score"]
        ]
        fig = go.Figure(
            go.Bar(
                x=score_dist["score"].astype(str),
                y=score_dist["count"],
                marker_color=score_colors,
                hovertemplate="Score %{x}<br>%{y:,} orders<extra></extra>",
            )
        )
        fig.update_layout(
            height=360,
            margin=dict(l=0, r=0, t=10, b=0),
            xaxis_title="Score (1–5)",
            yaxis_title="# Orders",
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Top products table
    st.subheader("Top 20 Produk (per Revenue)")
    top_prod = (
        df_f.groupby("product_id")
        .agg(
            revenue=("revenue", "sum"),
            orders=("order_id", "nunique"),
            avg_price=("price", "mean"),
            category=("category", "first"),
        )
        .nlargest(20, "revenue")
        .reset_index()
    )
    top_prod["revenue"] = top_prod["revenue"].round(2)
    top_prod["avg_price"] = top_prod["avg_price"].round(2)

    st.dataframe(
        top_prod,
        use_container_width=True,
        hide_index=True,
        column_config={
            "product_id": st.column_config.TextColumn("Product ID", width="medium"),
            "revenue": st.column_config.NumberColumn("Revenue (R$)", format="%.2f"),
            "orders": st.column_config.NumberColumn("Orders"),
            "avg_price": st.column_config.NumberColumn("Avg Price (R$)", format="%.2f"),
            "category": st.column_config.TextColumn("Category"),
        },
    )

    csv = top_prod.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Download top 20 sebagai CSV",
        csv,
        file_name="top_products.csv",
        mime="text/csv",
    )


# ── TAB: Indonesia Context ────────────────────────────────────────────────
with tab_id:
    st.subheader("🇮🇩 Kenapa Dataset Brasil Relevan untuk Indonesia?")
    st.markdown(
        """
Olist adalah marketplace e-commerce Brasil — analog dengan **Tokopedia / Shopee** di Indonesia.
Tiga pola di dashboard ini secara struktural mirip dengan dinamika pasar Indonesia:

| Pola di dataset Brasil | Analog Indonesia |
|---|---|
| São Paulo + Rio de Janeiro menyumbang mayoritas revenue | DKI Jakarta + Jawa Barat ≈ 45–50% GMV nasional |
| Peak Q4 (November–Desember) | **Harbolnas 11.11 & 12.12** + Ramadan/Lebaran |
| Credit card dominan, *boleto* untuk segmen unbanked | **GoPay/OVO/QRIS** dominan; transfer bank untuk segmen tertentu |
| Kategori *bed_bath_table*, *health_beauty*, *sports_leisure* | Mirror pola kategori top di Shopee/Tokopedia |
| On-time delivery jadi driver review score | **JNE/J&T/SiCepat** — SLA pengiriman kritis untuk repeat purchase |

### Rekomendasi bisnis (universal)
1. **Geografi:** Alokasikan akuisisi ke kota-kota tier-2 (Surabaya, Medan, Makassar) — pertumbuhan tinggi, kompetisi lebih rendah dari Jakarta.
2. **Seasonality:** Inventory & ads budget di-front-load 6–8 minggu sebelum 11.11.
3. **Logistik:** SLA on-time delivery → leading indicator review score → repeat purchase.
        """
    )

    # Quick comparison chart
    st.markdown("#### Konsentrasi geografis — top 5 state (filter aktif)")
    top5 = (
        df_f.groupby("customer_state")["revenue"].sum()
        .nlargest(5)
        .reset_index()
    )
    top5["share_pct"] = top5["revenue"] / df_f["revenue"].sum() * 100
    fig = px.bar(
        top5,
        x="customer_state",
        y="share_pct",
        text="share_pct",
        color_discrete_sequence=[PALETTE["BLUE"]],
    )
    fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    fig.update_layout(
        height=300,
        margin=dict(l=0, r=0, t=10, b=0),
        yaxis_title="% dari total revenue",
        xaxis_title=None,
    )
    st.plotly_chart(fig, use_container_width=True)

    total_top5 = top5["share_pct"].sum()
    st.info(
        f"5 state teratas menyumbang **{total_top5:.1f}%** revenue — "
        "sebanding dengan dominasi Jabodetabek + Bandung di pasar e-commerce Indonesia."
    )


# ── TAB: About ────────────────────────────────────────────────────────────
with tab_about:
    st.subheader("Tentang Project Ini")
    st.markdown(
        """
**Dashboard interaktif** ini adalah versi web dari static dashboard
(`sales-dashboard/output/dashboard.png`) di portfolio Ray.

**Tech stack:**
- Streamlit · Plotly · Pandas · PyArrow
- Data: 110,197 transaksi delivered, 21 kolom, dari [Olist Brazilian E-Commerce Dataset (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**Portfolio lengkap:** 5 proyek end-to-end (sales, churn, cohort+RFM, A/B testing, supply chain).
Lihat repo: [github.com/bursiaryn/data-analytics-portfolio](https://github.com/bursiaryn/data-analytics-portfolio)

**Kontak:** Ray — Data Analyst | Fokus FMCG, Retail, E-Commerce Indonesia
        """
    )

    st.caption(
        "Prepared by Ray  |  Tools: Python, Pandas, Streamlit, Plotly  |  "
        "Source: Olist Brazilian E-Commerce Dataset (Kaggle)"
    )
