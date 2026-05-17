# Ray — Data & AI Analytics Portfolio

> Operating manual untuk Claude Code. Baca ini sebelum memulai pekerjaan apapun di repo ini.

---

## 1. Tentang Portfolio Ini

Portfolio ini milik **Ray**, data analyst yang menargetkan klien FMCG, retail, dan e-commerce Indonesia.
Berisi **5 proyek analytics end-to-end** menggunakan dataset publik nyata (bukan sintetis).

**Tujuan utama:** Mendemonstrasikan kemampuan mengubah data menjadi keputusan bisnis —
bukan sekadar menampilkan metrik teknis.

**Target audience:** Hiring manager, klien potensial, dan rekan sesama analis di Indonesia.

---

## 2. Peran Profesional Ray

Setiap pekerjaan di repo ini harus mencerminkan **4 peran** berikut. Saat menulis kode,
analisis, atau narasi — tanya selalu: "apakah output ini memenuhi standar keempat peran?"

### Decision Analyst

Setiap analisis harus menjawab satu pertanyaan: **"Jadi, apa yang harus dilakukan bisnis?"**
- Selalu sertakan rekomendasi prioritas (High/Medium/Low impact x effort)
- Gunakan framing "Go / No-Go / Investigate Further" untuk keputusan binary
- Kuantifikasi dampak bisnis dalam satuan uang atau % jika memungkinkan
- Hindari analisis yang berakhir dengan "hasil bervariasi" tanpa arahan jelas

### Analytics Translator

Jembatan antara rigor statistik dan stakeholder non-teknis.
- Setiap cell markdown harus bisa dibaca oleh orang tanpa background statistik
- Hindari jargon tanpa penjelasan: "p-value <0.05" harus diikuti "artinya ada bukti statistik bahwa..."
- Selalu sertakan konteks pasar Indonesia (lihat Section 7)
- Gunakan tabel sederhana dan bullet points, bukan paragraf panjang

### Prompt Architect

Mendesain sistem yang memanfaatkan LLM secara optimal dalam workflow analitik.
- Saat menulis fungsi yang menghasilkan teks/narasi: pertimbangkan apakah Claude API
  bisa menghasilkan insight lebih kaya dari string template biasa
- Prompt harus spesifik, berisi konteks bisnis, dan meminta output terstruktur
- Dokumentasikan setiap prompt template yang dibuat (simpan di `notebooks/prompts/`)
- Default model: `claude-sonnet-4-6` untuk inference; `claude-haiku-4-5` untuk
  high-volume task (annotation, classification batch)

### Statistical Data Scientist

Menjaga rigor metodologis agar analisis dapat dipertanggungjawabkan.
- Selalu cek asumsi sebelum menjalankan test statistik (normalitas, homoskedastisitas, independence)
- Laporkan confidence interval, bukan hanya point estimate
- Bandingkan minimal 2 model (baseline + candidate) sebelum menyimpulkan
- Set random seed (`np.random.seed(42)`, `random_state=42`) di semua notebook
- Effect size wajib dilaporkan bersama p-value (Cohen's d, h, atau f-squared)

---

## 3. Struktur Portfolio

```
D:\ray\porto\
├── CLAUDE.md                   <- File ini
├── README.md                   <- Portfolio overview (link ke 5 proyek)
├── .gitignore
├── environment.yml             <- Single conda env untuk semua proyek
│
├── sales-dashboard/            -- Proyek 1: Revenue & Sales Analytics
├── churn-analysis/             -- Proyek 2: Customer Churn Prediction
├── cohort-rfm/                 -- Proyek 3: Cohort Retention + RFM/CLV
├── ab-testing/                 -- Proyek 4: A/B Testing & Experimentation
└── supply-chain/               -- Proyek 5: Supply Chain Optimization
```

### Struktur standar per proyek:

```
<project>/
├── data/raw/          <- Raw CSV (gitignored, harus didownload manual)
├── notebooks/
│   ├── 0N_*.ipynb     <- Numbered notebooks (01 = loading, last = dashboard)
│   └── viz_helpers.py <- Shared viz library (kpi_card, annotate_top_n, add_benchmark_line)
├── output/
│   ├── *.parquet      <- Processed data (gitignored)
│   ├── dashboard.png  <- Final 1-page dashboard
│   └── figures/       <- Individual chart exports
├── requirements.txt   <- Pip fallback (gunakan environment.yml utama)
└── README.md          <- Project docs + Konteks Pasar Indonesia
```

### Cross-project dependency:

```
sales-dashboard/output/df_master.parquet
        └──>  cohort-rfm/notebooks/01_data_prep.ipynb
```

Jalankan sales-dashboard notebook 01-02 sebelum cohort-rfm jika output belum ada.

---

## 4. Tech Stack & Environment

### Conda Environment

```
conda activate porto-data-analyst
```

Lihat `environment.yml` di root untuk full spec.

### Stack per Layer

| Layer | Tools |
|---|---|
| Data Wrangling | pandas, numpy, pyarrow |
| Visualization | matplotlib, seaborn (plotly untuk future interactive) |
| Statistics | scipy.stats, statsmodels |
| Machine Learning | scikit-learn (LR, RF, gradient boosting) |
| Explainability | shap (P3 roadmap) |
| AI/LLM | anthropic SDK — claude-sonnet-4-6 (P3 roadmap) |
| Notebooks | jupyter, nbconvert |
| Deployment | streamlit (P3 roadmap) |

### Windows-specific Notes

- Shell: PowerShell (bukan bash) untuk semua terminal command
- `conda` tidak selalu ada di PATH di Claude Code — gunakan full path jika perlu:
  `C:\Users\Lenovo\miniconda3\envs\porto-data-analyst\python.exe`
- File encoding: gunakan `encoding='utf-8'` untuk semua read/write
- Dataset DataCo supply chain: gunakan `encoding='latin-1'`
- Path separator: gunakan `pathlib.Path` — jangan hardcode backslash

---

## 5. Konvensi Kerja

### Notebook Standards

- Setiap notebook dimulai dengan markdown cell: judul, tujuan, output yang dihasilkan
- Setiap section punya heading markdown (`## 1. Section Name`)
- Cell output besar: gunakan `.head()`, `.describe()`, atau sample — jangan dump seluruh dataframe
- Setiap notebook berakhir dengan: simpan output ke parquet/JSON + konfirmasi print
- Dashboard notebook selalu berakhir dengan **Executive Summary** markdown cell

### Code Standards

- Variabel: `snake_case`; Konstanta warna: `ALL_CAPS` (misal `BLUE = '#2563EB'`)
- Impor: grouped (stdlib -> third-party -> local), alphabetical dalam group
- Magic numbers: assign ke named constant, jangan hardcode di tengah kode
- `random_state=42` dan `np.random.seed(42)` wajib di semua ML/bootstrap notebook
- Tidak perlu docstring panjang — nama fungsi yang jelas sudah cukup

### Visualization Standards

- Warna: gunakan PALETTE dari `viz_helpers.py` — jangan definisikan ulang hex codes
- Semua chart: judul bold, label axis, font DejaVu Sans
- Dashboard layout: `matplotlib.gridspec.GridSpec`, `figsize=(20-22, 14-16)`, `dpi=150`
- Setiap figure punya footer: "Prepared by Ray | Tools: ... | Source: ..."
- Benchmark line wajib di chart yang menampilkan rate/performance (gunakan `add_benchmark_line()`)

### Executive Summary Standards

Wajib ada di setiap dashboard notebook, berisi:

1. Tabel: Dimensi | Insight (3-5 baris)
2. Business Recommendation: 3 poin, numbered, mulai dengan **Bold action word**
3. Blockquote Indonesia: `> **Relevansi Indonesia:** [1-2 kalimat konteks lokal]`

---

## 6. Quality Gates

Sebelum menandai pekerjaan sebagai "selesai", cek semua item:

### Decision Analyst Gate

- [ ] Ada rekomendasi bisnis eksplisit (bukan hanya deskripsi hasil)
- [ ] Business impact dikuantifikasi (Rp / % / unit)
- [ ] Ada prioritasi (mana yang dikerjakan pertama, kenapa)

### Analytics Translator Gate

- [ ] Setiap temuan teknis punya plain-language translation
- [ ] Ada konteks pasar Indonesia (referensi Tokopedia/Shopee/Telkomsel/JNE jika relevan)
- [ ] Markdown cell bisa dibaca tanpa menjalankan kode

### Prompt Architect Gate

- [ ] Jika ada string template untuk teks: pertimbangkan apakah Claude API lebih tepat
- [ ] Narrative/insight generation: gunakan prompt terstruktur (role, context, output format)
- [ ] Prompt templates disimpan dan terdokumentasi di `notebooks/prompts/`

### Statistical Data Scientist Gate

- [ ] Asumsi test statistik dicek sebelum test dijalankan
- [ ] Confidence interval dilaporkan (bukan hanya p-value)
- [ ] Effect size dilaporkan
- [ ] Random seed di-set
- [ ] Minimal 2 model dibandingkan di notebook ML

---

## 7. Indonesian Market Context Guidelines

Setiap proyek harus memiliki koneksi ke pasar Indonesia. Gunakan referensi ini:

| Domain | Referensi Indonesia |
|---|---|
| E-commerce | Tokopedia, Shopee, Lazada, TikTok Shop; Harbolnas 11.11/12.12 |
| Payments | GoPay, OVO, ShopeePay, DANA, QRIS, transfer bank |
| Logistics | JNE, J&T Express, SiCepat, AnterAja, Grab/GoSend |
| Telco | Telkomsel, XL Axiata, Indosat Ooredoo; prepaid dominan |
| Retail/FMCG | Indomaret, Alfamart, Wings Group, Unilever Indonesia |
| Regional | DKI Jakarta + Jabar = ~45-50% e-commerce GMV; Sumatera + Kalimantan = growth market |

**Rule:** Jika dataset adalah Brazilian/US/global: selalu sertakan paragraf mapping ke konteks
Indonesia di README (heading "Konteks Pasar Indonesia") dan blockquote di exec summary notebook.

---

## 8. SWOT Portfolio

### Strengths (pertahankan)

- 5 proyek lengkap end-to-end, dataset nyata, code bersih
- Konsistensi visual dan struktur antar proyek (warna, layout, footer)
- Framing bisnis dengan konteks Indonesia di setiap proyek
- Statistical rigor: bootstrap, power analysis, multiple models, effect size
- viz_helpers.py sebagai reusable library yang mengurangi duplikasi code

### Weaknesses (perbaiki di P2-P3)

- Dashboard statis (PNG) — tidak interaktif, tidak bisa di-filter oleh viewer
- Belum ada deployed demo (tidak ada URL yang bisa dibagikan)
- LLM integration belum ada — peran "Prompt Architect" belum terdemonstrasikan
- Dataset 2 proyek masih perlu didownload (ab-testing, supply-chain)
- Belum ada root README sebagai entry point portfolio di GitHub

### Opportunities (kejar di P3-P4)

- Streamlit deployment: 1 proyek live -> recruiter bisa demo tanpa install apapun
- Claude API narrative: auto-generated insight dari dashboard metrics
- SHAP explainability: model churn + supply chain lebih explainable untuk klien
- Indonesian dataset: 1 proyek dengan data lokal (BPS, Satu Data Indonesia)
- GitHub proper setup: portfolio visible dengan README yang menarik

### Threats (mitigasi)

- Portofolio kompetitor sudah deploy Streamlit/Tableau dengan live URL
- Tanpa demo URL, recruiter sulit verifikasi tanpa clone repo sendiri
- Dataset besar (CSV) bisa ter-commit ke git jika .gitignore tidak ada

---

## 9. Improvement Roadmap

### P2 — Foundation (dikerjakan 2026-05-15)

- [x] CLAUDE.md ini — comprehensive operating manual
- [x] `.gitignore` — ignore data/raw/, *.parquet, __pycache__, .ipynb_checkpoints
- [x] `environment.yml` — single env untuk semua 5 proyek
- [x] `README.md` root — portfolio overview, skill matrix, link ke 5 proyek

### P3 — Differentiation (sesi berikutnya)

- [ ] **Streamlit app**: sales-dashboard -> interactive web app (filter by state/category/period)
- [ ] **Claude API integration**: auto-narrative dari dashboard JSON metrics menggunakan Anthropic SDK
- [ ] **SHAP**: tambah explainability layer ke churn + supply chain model (notebook terpisah)
- [ ] **GitHub Actions**: smoke test — validate notebook dapat diimport tanpa error

### P4 — Advanced (masa depan)

- [ ] 1 proyek dengan dataset Indonesia (BPS, Satu Data Indonesia, atau open data publik)
- [ ] Portfolio website (GitHub Pages atau Netlify) dengan embedded dashboard screenshots
- [ ] Model monitoring dashboard (MLflow atau custom logging)

---

## 10. Do's and Don'ts

### Do

- Tulis kode yang bisa dibaca ulang 6 bulan kemudian tanpa konteks tambahan
- Gunakan `viz_helpers.py` — jangan reinvent color constants atau KPI card
- Ikuti pola notebook yang sudah ada (structure, naming, output)
- Tambahkan Indonesian context ke setiap analisis baru
- Commit kecil dengan pesan yang jelas ("add SHAP to churn notebook 03")

### Don't

- Jangan commit file di `data/raw/` (terlalu besar, ada di .gitignore)
- Jangan commit `*.parquet` output (regenerable dari notebook)
- Jangan hardcode path absolut (`C:\Users\Lenovo\...`) — gunakan `Path('../output')`
- Jangan tambahkan feature di luar roadmap tanpa diskusi terlebih dahulu
- Jangan skip quality gates di Section 6

---

*Last updated: 2026-05-15 | Maintained by Ray*
