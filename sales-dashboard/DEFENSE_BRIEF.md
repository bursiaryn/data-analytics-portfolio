# Project Defense Brief — Sales Dashboard

> **Tujuan:** Catatan teknis & fundamental untuk dipertanggungjawabkan di interview.
> Isi dengan **bahasa sendiri**. Yang gagal dijelaskan = yang perlu dipelajari ulang.

---

## 1. Fact Sheet (sudah terisi — context untuk defense)

| Item | Detail |
|------|--------|
| Dataset | Brazilian E-Commerce (Olist), 7 CSV files, ~110k orders, periode 2016-2018 |
| Domain | E-commerce retail |
| Output | `dashboard.png` static + Streamlit Cloud live app |
| Stack | pandas, matplotlib, seaborn, plotly, streamlit |
| Key analyses | Revenue trend, top categories (Pareto), geographic distribution per state, payment mix, delivery performance, review distribution |
| Live demo | https://data-analytics-portfolio-9ymrn6m6ijtyaamhnxndcr.streamlit.app/ |

---

## 2. Defense Questions (isi dengan bahasa sendiri)

### 2.1 Apa yang dilakukan? (1 paragraf executive)
> *Tulis di sini ringkasan proyek kalau ditanya "elevator pitch" 60 detik. Hindari jargon.*



### 2.2 Kenapa KPI ini yang dipilih (Revenue trend, top kategori, payment mix, delivery, review)?
> *Kenapa bukan customer count, AOV, atau yang lain? Apa hubungannya dengan keputusan bisnis e-commerce?*



### 2.3 Kenapa breakdown per state (bukan per city atau per region)?
> *Trade-off granularity. Kenapa state yang dipilih sebagai unit analisis utama?*



### 2.4 Asumsi apa yang dicek tentang data quality?
> *Missing values di review? Outlier di delivery time? Duplikat order? Apa yang di-handle dan kenapa?*



### 2.5 Kenapa Streamlit untuk deployment (bukan Dash, Tableau, atau Power BI)?
> *Pertimbangan: cost, learning curve, ekosistem Python, integrasi dengan pandas.*



### 2.6 Trade-off yang diterima
> *Apa yang TIDAK dilakukan karena waktu/scope? Contoh: tidak melakukan time-series forecasting, tidak buat customer lifetime value (itu di proyek terpisah).*



### 2.7 Limitasi & yang akan diubah dengan waktu lebih
> *Data 2016-2018 = stale. Tidak ada seasonality decomposition. Geographic granularity terbatas state.*



### 2.8 Business interpretation
> *Kalau klien tanya "Jadi saya harus apa berdasarkan dashboard ini?" — apa rekomendasi top-3 kamu?*



---

## 3. Likely Interview Questions

Pertanyaan yang **wajib** bisa kamu jawab tanpa lihat catatan:

1. **"Walk me through this project from start to finish."** — Latihan 2-3 menit, jangan baca slide.
2. **"Kenapa pakai Olist? Bukannya itu dataset Brazil, tidak relevan untuk Indonesia?"** — Hint: prinsip e-commerce universal; mapping ke konteks Indonesia ada di README.
3. **"Apa insight paling unexpected dari analisis ini?"** — Cari 1 finding yang surprising, bukan obvious.
4. **"Kalau kamu jadi Head of Analytics Tokopedia, dashboard ini akan kamu pakai untuk keputusan apa?"** — Translate ke konteks lokal.
5. **"Kenapa pareto analysis untuk kategori? Apa itu Pareto?"** — Bisa jelaskan 80/20 dalam 30 detik.
6. **"Bagaimana cara handle missing data di kolom review?"** — Strategi imputation vs drop, dan kenapa.
7. **"Kalau data 10x lebih besar (1M+ orders), apa yang berubah?"** — Pertanyaan scalability: chunking, parquet, sampling.
8. **"Bedanya `matplotlib` dengan `plotly`?"** — Static vs interactive; kapan pakai yang mana.

---

## 4. AI Usage — Honest Framing

Template jawaban jujur kalau ditanya:

> *"Saya gunakan AI sebagai pair programmer untuk akselerasi implementasi — generate boilerplate viz code, debug error, format docstring. Tapi keputusan analitis (kenapa state, kenapa Pareto, kenapa KPI ini) saya yang tentukan setelah baca dokumentasi Olist dan referensi business analytics. AI tidak memilih metodologi untuk saya."*

---

## 5. Glossary Konsep Kunci (harus bisa jelaskan dalam 30 detik)

| Konsep | Definisi singkat | Lokasi belajar |
|--------|------------------|----------------|
| Pareto principle (80/20) | | Wikipedia: Pareto distribution |
| Revenue trend analysis | | Towards Data Science |
| Geographic segmentation | | |
| Payment mix analysis | | |
| Streamlit caching (`@st.cache_data`) | | streamlit.io docs |
| Parquet vs CSV | | pandas docs |

---

## 6. Self-Assessment Checklist

Setelah isi defense brief ini, cek:

- [ ] Saya bisa jelaskan project ini dalam 60 detik tanpa baca catatan
- [ ] Saya bisa jawab "kenapa X bukan Y" untuk minimal 3 keputusan teknis
- [ ] Saya bisa interpret hasil analisis tanpa lihat code
- [ ] Saya tau 1 limitasi proyek ini yang akan saya improve dengan waktu lebih
- [ ] Saya tau 1 hal yang tidak saya pelajari mendalam — siap mengaku kalau ditanya
