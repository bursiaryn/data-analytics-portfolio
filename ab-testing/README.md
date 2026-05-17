# A/B Test Analysis — Landing Page Experiment

Analisis statistik end-to-end eksperimen A/B: dari validasi eksperimen hingga business decision Go/No-Go. Mendemonstrasikan 4 metode statistik: Z-test, Chi-square, T-test, dan Bootstrap CI.

---

## Dashboard Preview

> Jalankan notebook 01–05 secara berurutan.

`output/dashboard.png` — Verdict GO/NO-GO + conversion test + revenue distribution + bootstrap CI + power curve.

---

## Ringkasan Eksperimen

| Skenario | Test | Verdict |
|----------|------|---------|
| Conversion Rate (landing page) | Z-test + Chi-square | Lihat output |
| Revenue per User | T-test (Welch) + Bootstrap CI | Lihat output |
| Experiment Design | Power Analysis + MDE | — |

> *Verdict aktual tergantung dataset. Dataset ini dirancang untuk menunjukkan bahwa new page **tidak** secara signifikan mengalahkan old page — justru ini poin edukasi terpenting: tidak semua A/B test menghasilkan Go.*

---

## Key Findings

| # | Temuan |
|---|--------|
| 1 | Dataset memiliki **assignment error** (~3,800 rows mismatch) — validasi eksperimen wajib dilakukan sebelum analisis |
| 2 | Perbedaan conversion rate sangat kecil → tidak cukup bukti statistik untuk Go |
| 3 | Bootstrap CI memberikan estimasi yang lebih robust dibandingkan parametric test untuk distribusi skewed |
| 4 | Untuk mendeteksi lift sekecil 0.5%, dibutuhkan >100k sampel per grup — penting untuk planning eksperimen |

---

## Pelajaran untuk Client

1. **Validasi eksperimen** sebelum analisis — kesalahan assignment merusak validitas
2. **Statistical significance ≠ practical significance** — lihat effect size (Cohen's h/d)
3. **Jangan stop eksperimen lebih awal** — tunggu sample size yang cukup untuk 80% power
4. **No-Go adalah hasil yang valid** — informasi berharga untuk iterasi berikutnya

---

## Struktur Proyek

```
ab-testing/
├── data/raw/
│   └── ab_data.csv                       ← dari Kaggle
├── notebooks/
│   ├── 01_data_loading_eda.ipynb         ← Validasi + cleaning + generate revenue
│   ├── 02_conversion_rate_test.ipynb     ← Z-test + Chi-square + CI
│   ├── 03_revenue_bootstrap_test.ipynb   ← T-test + Bootstrap 10k iterasi
│   ├── 04_power_sample_size.ipynb        ← Power curve + MDE table + novelty check
│   └── 05_dashboard_final.ipynb          ← Dashboard + export PNG
├── output/
│   ├── df_clean.parquet
│   ├── test_results.json
│   ├── dashboard.png
│   └── figures/
├── requirements.txt
└── README.md
```

---

## Cara Menjalankan

### 1. Download Dataset

[A/B Testing Dataset — Kaggle](https://www.kaggle.com/datasets/zhangluyuan/ab-testing)

Simpan `ab_data.csv` ke `data/raw/`.

### 2. Install Dependencies

```bash
conda activate porto-data-analyst
conda install scipy statsmodels -c conda-forge -y
```

### 3. Jalankan Notebook Berurutan

```bash
jupyter notebook
# 01 → 02 → 03 → 04 → 05
```

| Notebook | Output |
|----------|--------|
| 01 | df_clean.parquet |
| 02 | figures/A, B + print verdict |
| 03 | test_results.json + figures/C, D |
| 04 | figures/E, F |
| 05 | dashboard.png |

---

## Tech Stack

- Python 3.11 — pandas, numpy
- SciPy — chi2_contingency, ttest_ind, norm
- Statsmodels — proportions_ztest, NormalIndPower
- Matplotlib, Seaborn — visualisasi
- Jupyter Notebook


---

## Konteks Pasar Indonesia

Metodologi A/B testing dalam proyek ini relevan langsung untuk experimentation di platform Indonesia:

- **Scale Advantage:** Tokopedia dan Shopee dengan **>100 juta active users** dapat mendeteksi conversion lift sekecil 0.5% hanya dalam 2-3 hari — jauh lebih cepat dari dataset Kaggle ini yang membutuhkan ratusan ribu sample. Untuk seller marketplace skala menengah, minimum experiment runtime adalah **7-14 hari** untuk menghindari novelty effect dan day-of-week bias.
- **Null Result sebagai Norma:** ~70% A/B test di industri e-commerce Indonesia gagal mengalahkan baseline — **hasil NO-GO adalah informasi berharga**, bukan kegagalan. Tim product Tokopedia/Bukalapak menjalankan 50-100 experiment paralel per kuartal dengan expected win rate ~30%.
- **Conversion Rate Benchmark:** Dataset ini menampilkan conversion rate ~12% (tinggi karena sudah filtered ke existing users). **Conversion rate Indonesia di landing page iklan: 1-3%; di cart/checkout: 60-75%**. Konteks metrik kritis untuk interpretasi lift yang meaningful.
- **Power Analysis Aplikasi:** Tabel MDE (Minimum Detectable Effect) dari proyek ini langsung dapat digunakan sebagai template untuk **pre-experiment planning** di campaign Ramadan, Harbolnas, atau flash sale — menentukan berapa lama experiment harus berjalan sebelum mengambil keputusan Go/No-Go.
