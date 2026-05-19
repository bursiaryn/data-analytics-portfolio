# Churn Analysis — IBM Telco Customer Churn

Analisis end-to-end prediksi customer churn menggunakan dataset IBM Telco.
Proyek ini mencakup EDA, segmentasi risiko, dan model ML (Logistic Regression vs Random Forest).

---

## Dashboard Preview

> Jalankan notebook 01–04 secara berurutan untuk menghasilkan dashboard.

`output/dashboard.png` — KPI cards + churn by contract + tenure + feature importance + model score.

---

## Key Results

| Metrik | Nilai |
|--------|-------|
| Churn Rate Dataset | ~26.5% |
| Model Terbaik | Random Forest |
| ROC-AUC | ~0.83 |
| Recall Churn | ~0.76 |

---

## Key Findings

| # | Temuan |
|---|--------|
| 1 | Pelanggan dengan kontrak **Month-to-month** churn 3× lebih tinggi dari kontrak 2-year |
| 2 | **Pelanggan baru** (<12 bulan) adalah kelompok paling berisiko |
| 3 | Pelanggan **tanpa TechSupport/OnlineSecurity** memiliki churn rate signifikan lebih tinggi |
| 4 | **Electronic check** sebagai metode pembayaran berkorelasi dengan churn rate tertinggi |
| 5 | **tenure** adalah faktor prediktif terkuat dalam model RF |

---

## Rekomendasi Bisnis

1. **High Risk Segment** — tawarkan upgrade ke kontrak 1-year dengan diskon bulan ke-3
2. **Early Loyalty Program** — intervensi proaktif di bulan ke-6 untuk pelanggan baru
3. **Service Bundle** — promosikan TechSupport + OnlineSecurity sebagai paket proteksi

---

## Struktur Proyek

```
churn-analysis/
├── data/raw/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv   ← dari Kaggle
├── notebooks/
│   ├── 01_data_loading_cleaning.ipynb
│   ├── 02_eda_segmentation.ipynb
│   ├── 03_model_prediction.ipynb
│   ├── 04_dashboard_final.ipynb
│   └── 05_shap_explainability.ipynb       ← explainability layer (P3)
├── output/
│   ├── df_clean.parquet
│   ├── model_results.json
│   ├── dashboard.png
│   └── figures/
├── requirements.txt
└── README.md
```

---

## Cara Menjalankan

### 1. Download Dataset

[IBM Telco Customer Churn — Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

Simpan `WA_Fn-UseC_-Telco-Customer-Churn.csv` ke folder `data/raw/`.

### 2. Install Dependencies

```bash
conda activate porto-data-analyst
conda install pandas numpy matplotlib seaborn scikit-learn jupyter pyarrow -c conda-forge -y
```

### 3. Jalankan Notebook Berurutan

```bash
jupyter notebook
```

| Notebook | Output |
|----------|--------|
| 01 | `output/df_clean.parquet` |
| 02 | `output/figures/A_*.png ... E_*.png` |
| 03 | `output/model_results.json` |
| 04 | `output/dashboard.png` |
| 05 | `output/figures/H_shap_*.png … K_shap_*.png` — explainability (global + local) |

---

## Tech Stack

- Python 3.11 — pandas, numpy
- Scikit-learn — Logistic Regression, Random Forest
- **SHAP** — model explainability (TreeExplainer, beeswarm, dependence, waterfall)
- Matplotlib, Seaborn — visualisasi
- Jupyter Notebook

---

## Dataset

**IBM Telco Customer Churn**
- 7,043 pelanggan, 21 kolom
- Sumber: [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Lisensi: Data files © Original Authors


---

## Konteks Pasar Indonesia

Analisis churn telco ini memiliki implikasi langsung untuk industri telekomunikasi dan fintech Indonesia:

- **Prepaid Dominance:** IBM Telco dataset menampilkan month-to-month contract sebagai high-churn segment — ini persis mencerminkan kondisi **Telkomsel, XL Axiata, dan Indosat Ooredoo** di Indonesia di mana ~85% pelanggan adalah prepaid (setara month-to-month). Churn equivalent mencapai 3-5%/bulan di segmen prepaid Indonesia.
- **E-wallet sebagai Retention Tool:** Di Indonesia, pelanggan yang melinking nomor mereka ke **GoPay, OVO, atau DANA** menunjukkan churn 15-20% lebih rendah — switching cost meningkat karena nomor menjadi identitas finansial, bukan sekadar kartu SIM.
- **Tenure Segmentation:** Pola "new customers churn fastest" universal — operator Indonesia menggunakan program **Welcome Bonus 30/60/90 hari** untuk memperpanjang tenure awal. Model LR + RF di proyek ini dapat langsung diadaptasi untuk prediksi churn di dataset operator lokal.
- **Business Impact Quantification:** Metodologi revenue-at-risk yang digunakan di sini (churn rate × ARPU × at-risk count) adalah standar yang digunakan oleh tim Business Intelligence Telkomsel dan XL dalam quarterly churn review.
