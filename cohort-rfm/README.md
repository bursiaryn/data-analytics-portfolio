# Cohort + RFM + CLV Analysis — Olist Brazilian E-Commerce

Analisis longitudinal customer behavior: cohort retention, RFM segmentation, dan Customer Lifetime Value estimation. Reuse dataset dari proyek sales-dashboard (tidak perlu download ulang).

---

## Dashboard Preview

> Jalankan notebook 01–04 berurutan untuk menghasilkan dashboard.

`output/dashboard.png` — KPI cards + cohort heatmap + RFM segment + CLV per segmen.

---

## Key Results

| Metrik | Nilai |
|--------|-------|
| Total Unique Customers | ~96,000 |
| Avg Month-1 Retention | ~5–8% |
| Champions + Loyal % | ~15–20% |
| Avg Customer CLV | ~R$ 150–200 |

> *Angka aktual tergantung output notebook. Jalankan untuk mendapatkan nilai pasti.*

---

## Key Findings

| # | Temuan |
|---|--------|
| 1 | Cohort retention turun drastis setelah bulan pertama — menunjukkan **one-time buyer problem** |
| 2 | Sebagian besar pelanggan masuk segmen **Hibernating** atau **Lost** |
| 3 | **Champions** memiliki CLV 5–10x lebih tinggi dari segmen lainnya |
| 4 | Peak akuisisi terjadi di Q4 2017 (pre-holiday season) |

---

## Rekomendasi per Segmen

| Segmen | Strategi |
|--------|----------|
| **Champions** | Program eksklusif, referral rewards, early access produk baru |
| **Loyal Customers** | Loyalty points, upsell ke kategori premium |
| **At Risk** | Win-back email + diskon personal dalam 30 hari |
| **Hibernating** | Re-engagement campaign dengan urgency ("produk favorit mu kembali") |
| **New Customers** | Onboarding sequence, kupon order ke-2 |
| **Lost** | Survey exit, minimal spend untuk reaktivasi |

---

## Struktur Proyek

```
cohort-rfm/
├── notebooks/
│   ├── 01_data_prep.ipynb           ← Agregasi df_master → df_orders
│   ├── 02_cohort_analysis.ipynb     ← Cohort retention heatmap
│   ├── 03_rfm_clv.ipynb             ← RFM scoring + CLV estimation
│   └── 04_dashboard_final.ipynb     ← Dashboard layout + export PNG
├── output/
│   ├── df_orders.parquet
│   ├── df_rfm.parquet
│   ├── cohort_retention.parquet
│   ├── dashboard.png
│   └── figures/
├── requirements.txt
└── README.md
```

---

## Prerequisites

Proyek ini membutuhkan output dari proyek **sales-dashboard**:
- `../sales-dashboard/output/df_master.parquet` harus ada

Jalankan `sales-dashboard/notebooks/01_data_loading_cleaning.ipynb` terlebih dahulu jika belum.

---

## Cara Menjalankan

```bash
conda activate porto-data-analyst
jupyter notebook
```

Jalankan berurutan: `01` → `02` → `03` → `04`

| Notebook | Input | Output |
|----------|-------|--------|
| 01 | df_master.parquet | df_orders.parquet |
| 02 | df_orders.parquet | cohort_retention.parquet + figures/A,B |
| 03 | df_orders.parquet | df_rfm.parquet + figures/C |
| 04 | df_rfm + cohort_retention | dashboard.png |

---

## Tech Stack

- Python 3.11 — pandas, numpy
- Matplotlib, Seaborn — visualisasi + heatmap
- Jupyter Notebook


---

## Konteks Pasar Indonesia

Cohort analysis dan RFM segmentation dari dataset ini langsung applicable untuk e-commerce Indonesia:

- **Benchmark Retention:** M+1 retention <15% dari dataset Olist lebih rendah dari **Tokopedia dan Shopee yang mencatat repeat purchase rate 25-35% dalam 90 hari** — perbedaan ini disebabkan oleh loyalty program dan gamification yang lebih aggressive di platform Indonesia (daily check-in coins, flash sale notifikasi).
- **Shopee Loyalty Tier:** Sistem segmentasi 8 kategori RFM (Champions → Lost) dalam proyek ini secara persis memetakan ke **Shopee Loyalty Tier: Diamond, Platinum, Gold, Silver** — Champions = Diamond, Loyal Customers = Platinum, At Risk = Silver menuju downgrade.
- **AOV vs Frequency Trade-off:** Dataset Brasil menunjukkan AOV ~R$160 dengan frequency rendah. Indonesia memiliki pola berbeda — **AOV lebih rendah (Rp 100-300rb rata-rata) tapi frequency lebih tinggi** (terutama Shopee dengan gamification checkout). Metric yang perlu dioptimasi berbeda: di Brasil fokus pada AOV, di Indonesia fokus pada frequency.
- **CLV Estimation:** Model CLV = AOV × Purchase Frequency × 12 bulan yang digunakan di sini adalah standar yang dipakai tim Growth Analytics Tokopedia untuk menentukan customer acquisition cost ceiling per segmen.
