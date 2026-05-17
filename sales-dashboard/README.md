# Sales Dashboard — Brazilian E-Commerce (Olist)

Analisis end-to-end performa penjualan menggunakan dataset nyata Olist Brazilian E-Commerce.
Proyek ini mendemonstrasikan kemampuan data wrangling multi-tabel, analisis bisnis 5 dimensi, dan penyajian insight siap presentasi.

---

## Dashboard Preview

> Jalankan notebook 03 untuk menghasilkan gambar di bawah ini.

`output/dashboard.png` — layout satu halaman dengan KPI cards + 4 chart utama.

---

## Insight Utama

| Area | Temuan |
|------|--------|
| Revenue | Peak terjadi Nov 2017 (Black Friday) dan pertumbuhan signifikan Q1 2018 |
| Kategori | `bed_bath_table` dan `health_beauty` mendominasi revenue |
| Geografi | SP (São Paulo) menyumbang >40% total revenue nasional |
| Pembayaran | Credit card digunakan di >70% transaksi |
| Pengiriman | Korelasi negatif antara lama pengiriman dan review score |

---

## Struktur Proyek

```
sales-dashboard/
├── data/raw/               ← CSV dari Kaggle (tidak di-commit)
├── notebooks/
│   ├── 01_data_loading_cleaning.ipynb   ← Load, merge, feature engineering
│   ├── 02_exploratory_analysis.ipynb    ← 5 area analisis + export chart
│   └── 03_dashboard_final.ipynb        ← Dashboard layout + export PNG
├── output/
│   ├── df_master.parquet               ← Master dataframe (dihasilkan nb01)
│   ├── dashboard.png                   ← Dashboard final (dihasilkan nb03)
│   └── figures/                        ← Chart individual dari nb02
├── requirements.txt
└── README.md
```

---

## Cara Menjalankan

### 1. Download Dataset

Download dari Kaggle: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

Ekstrak semua CSV ke folder `data/raw/`.

File yang dibutuhkan:
- `olist_orders_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_order_payments_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_customers_dataset.csv`
- `olist_products_dataset.csv`
- `product_category_name_translation.csv`

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan Notebook Secara Berurutan

```bash
jupyter notebook
```

Buka dan jalankan:
1. `notebooks/01_data_loading_cleaning.ipynb` → menghasilkan `output/df_master.parquet`
2. `notebooks/02_exploratory_analysis.ipynb` → menghasilkan chart di `output/figures/`
3. `notebooks/03_dashboard_final.ipynb` → menghasilkan `output/dashboard.png`

---

## Tech Stack

- Python 3.11
- pandas, numpy — data wrangling
- matplotlib, seaborn — visualisasi
- Jupyter Notebook — environment analisis

---

## Dataset

**Brazilian E-Commerce Public Dataset by Olist**
- 100k+ orders (Sep 2016 – Sep 2018)
- 9 tabel relasional
- Sumber: [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- Lisensi: CC BY-NC-SA 4.0


---

## Konteks Pasar Indonesia

Temuan proyek ini langsung relevan untuk analisis e-commerce Indonesia:

- **Konsentrasi Geografis:** São Paulo + Rio de Janeiro (~55% revenue Brasil) memiliki analog persis dengan DKI Jakarta + Jawa Barat yang menyumbang ~45-50% GMV Tokopedia/Shopee. Strategi ekspansi ke negara bagian lain dalam dataset ini mencerminkan peluang penetrasi ke Jawa Timur, Sumatera Utara, dan Sulawesi Selatan di Indonesia.
- **Seasonal Pattern:** Puncak Q4 (Nov–Des) di dataset Brasil setara dengan **Harbolnas 11.11 dan 12.12** di Indonesia — momen di mana Shopee dan Tokopedia mencatat GMV harian 5-10x normal. Persiapan inventory 6-8 minggu sebelumnya berlaku langsung.
- **Payment Mix:** Credit card dominan (>70%) vs Indonesia di mana **e-wallet (GoPay, OVO, ShopeePay) dan QRIS** mendominasi — mencapai >60% transaksi digital. Analisis payment mix ini menunjukkan pentingnya memahami preferensi pembayaran lokal untuk conversion optimization.
- **Kategori Produk:** *Health & beauty* sebagai top growth category juga berlaku di Indonesia — Sociolla, Tokopedia Beauty, dan TikTok Shop menunjukkan tren serupa dengan margin premium dan repeat purchase tinggi.
