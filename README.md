# Ray — Data & AI Analytics Portfolio

Data analyst spesialisasi **FMCG, retail, dan e-commerce Indonesia**.
Mengubah data menjadi keputusan bisnis yang terukur.

🚀 **Live demo:** [Sales Dashboard interaktif →](https://data-analytics-portfolio-9ymrn6m6ijtyaamhnxndcr.streamlit.app/)
(filter per state · kategori · periode · download top products)

---

## 5 Portfolio Projects

| # | Proyek | Domain | Teknik Utama | Status |
|---|---|---|---|---|
| 1 | [Sales Dashboard](sales-dashboard/) · [🚀 Live](https://data-analytics-portfolio-9ymrn6m6ijtyaamhnxndcr.streamlit.app/) | E-commerce Revenue | EDA, KPI Dashboard, Pareto Analysis, Streamlit | Complete |
| 2 | [Customer Churn](churn-analysis/) | Telco Retention | ML Classification, LR + RF, AUC 0.83, **SHAP** | Complete |
| 3 | [Cohort + RFM](cohort-rfm/) | Customer Lifecycle | Cohort Retention, RFM Scoring, CLV | Complete |
| 4 | [A/B Testing](ab-testing/) | Experimentation | Z-test, Bootstrap CI, Power Analysis | Complete |
| 5 | [Supply Chain](supply-chain/) | Operations Analytics | ABC, ROP + Safety Stock, Late Delivery ML, **SHAP** | Complete |

---

## Skills Demonstrated

**Analytics:** EDA · Cohort Analysis · RFM Segmentation · A/B Testing · ABC Inventory  
**Machine Learning:** Logistic Regression · Random Forest · Feature Importance · AUC/ROC · **SHAP Explainability**  
**Statistics:** Z-test · Chi-square · Bootstrap CI · Power Analysis · Effect Size  
**Visualization:** Matplotlib · Seaborn · Plotly · Streamlit · 1-page dashboard layout · KPI cards  
**Deployment:** Streamlit Community Cloud (live demo URL ✅)  
**Tools:** Python · Pandas · Scikit-learn · Scipy · Statsmodels · Jupyter  

---

## Quick Start

```bash
# 1. Clone repo
git clone <repo-url>
cd porto

# 2. Setup environment (semua proyek, satu perintah)
conda env create -f environment.yml
conda activate porto-data-analyst

# 3. Mulai dari sales-dashboard
cd sales-dashboard/notebooks
jupyter notebook
```

> **Catatan:** `cohort-rfm` bergantung pada output `sales-dashboard`.
> Jalankan `01_data_loading_cleaning.ipynb` di sales-dashboard terlebih dahulu.

---

## Project Highlights

### Sales Dashboard — Brazilian E-Commerce
Analisis revenue trend, kategori produk, distribusi geografis, payment mix, dan review score
dari 110k+ transaksi Olist. Output: dashboard PNG siap presentasi + 5 figure individu.

### Customer Churn — IBM Telco
Prediksi churn 7,043 pelanggan telco menggunakan Logistic Regression + Random Forest.
AUC 0.83, recall churn 78% — mengidentifikasi 8 dari 10 pelanggan yang akan pergi.

### Cohort + RFM — Customer Retention
Cohort retention heatmap 13 bulan + RFM scoring 5-quintile + estimasi CLV per 8 segmen.
Reuses Olist dataset — mendemonstrasikan multi-layer customer analytics dari satu sumber data.

### A/B Testing — Landing Page Experiment
Z-test proporsi + bootstrap 10,000 iterasi + power analysis. Verdict NO-GO didemonstrasikan
sebagai contoh null result yang valid — ~70% A/B test industri tidak beat baseline.

### Supply Chain — DataCo Analytics
ABC inventory classification (Pareto 80/20) + bottleneck analysis + Reorder Point dengan safety
stock Z=1.645 (95% service level) + prediksi keterlambatan RF dengan AUC >0.90.

---

## Roadmap

- **P3:** ✅ Streamlit interactive dashboard · ✅ SHAP explainability (churn + supply-chain) · ⏳ Claude API narrative
- **P4:** Dataset Indonesia (BPS/open data) + GitHub Actions notebook validation

---

## Contact

rosyidmail@gmail.com
