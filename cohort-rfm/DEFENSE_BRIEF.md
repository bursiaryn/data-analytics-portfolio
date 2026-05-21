# Project Defense Brief — Cohort + RFM Analysis

> **Tujuan:** Catatan teknis & fundamental untuk dipertanggungjawabkan di interview.
> Isi dengan **bahasa sendiri**. Yang gagal dijelaskan = yang perlu dipelajari ulang.

---

## 1. Fact Sheet

| Item | Detail |
|------|--------|
| Dataset | Reuses Olist (`sales-dashboard/output/df_master.parquet`) |
| Domain | Customer lifecycle / retention analytics |
| Cohort horizon | 13 bulan (cohort by first purchase month) |
| RFM scoring | 5-quintile (1-5 per R, F, M → score 555 = best) |
| Segments | 8 segments (Champions, Loyal, Potential Loyalists, At Risk, dll) |
| CLV calculation | Per-segment average × estimated lifespan |

---

## 2. Defense Questions

### 2.1 Apa yang dilakukan? (1 paragraf executive)
> *Apa itu cohort, apa itu RFM, kenapa keduanya digabung?*



### 2.2 Apa beda cohort analysis vs segmentation biasa?
> *Cohort = group dengan shared experience (mis. first purchase di bulan X). Segmentation = group by attribute (mis. age, location). Kenapa cohort lebih powerful untuk retention?*



### 2.3 Kenapa RFM 5-quintile (bukan 3 atau 10)?
> *Trade-off granularity vs sample size per segment. Quintile = balanced karena split by percentile.*



### 2.4 Definisi cohort di proyek ini — by first purchase month, kenapa bukan first visit / first sign-up?
> *Data Olist hanya punya purchase data. Untuk dataset lain (mis. SaaS), first sign-up lebih relevan.*



### 2.5 Bagaimana cara handle cohort dengan sample size kecil (mis. < 100 customers)?
> *Risiko overinterpret. Pertimbangan: aggregate dengan cohort lain, atau exclude dari analisis.*



### 2.6 CLV formula — break down per komponen
> *CLV = avg_order_value × purchase_frequency × estimated_lifespan_months. Asumsi konstan over time?*



### 2.7 Asumsi yang dicek
> *Distribusi monetary skewed → median lebih representatif daripada mean? Recency calculation date — pakai max date dataset atau today?*



### 2.8 Limitasi
> *Tidak ada cost data → CLV bukan profit. Tidak ada survival analysis → lifespan estimation rough. Cohort hanya 13 bulan, kurang panjang untuk multi-year retention.*



### 2.9 Business interpretation
> *Segment "Champions" — apa yang dilakukan ke mereka? Segment "At Risk" — campaign retention apa?*



---

## 3. Likely Interview Questions

1. **"Apa itu RFM?"** — Recency (kapan terakhir beli), Frequency (berapa kali beli), Monetary (berapa total spending).
2. **"Heatmap cohort retention — sumbu X dan Y itu apa? Warna gelap = apa?"** — X: month since first purchase, Y: cohort (first purchase month), warna: % retention.
3. **"Kenapa retention bulan ke-1 selalu 100%?"** — By definition cohort di-anchor di bulan 0.
4. **"Apa itu CLV (Customer Lifetime Value)?"** — Estimasi total revenue dari satu pelanggan selama hidup hubungannya dengan bisnis.
5. **"Bedakan CLV dengan ARPU."** — ARPU = average revenue per user per period (mis. bulanan). CLV = totalnya seumur pelanggan.
6. **"Kalau Champions = 8% pelanggan tapi generate 35% revenue, apa implikasinya?"** — Pareto principle on customer level; prioritas retention budget.
7. **"Apa beda recency rendah vs frequency tinggi?"** — Recency rendah = baru beli (good). Frequency tinggi = sering beli (good). Combination matters.
8. **"Kalau dataset hanya 6 bulan, apakah RFM masih valid?"** — Recency window terbatas, monetary mungkin underestimate; perlu disclose limitation.
9. **"Bagaimana scoring 5-quintile dilakukan? Bagaimana tie-breaking?"** — `pd.qcut` atau ranking; tie biasanya assigned ke quintile lebih rendah (atau random).

---

## 4. AI Usage — Honest Framing

> *"Konsep RFM dan cohort analysis saya pelajari dari blog Optimove dan paper akademik retention analytics — bukan dari AI. AI bantu implementasi `pd.qcut` dan annotation heatmap. Pemilihan 5-quintile dan definisi 8 segmen ikut framework standar industri (RFM Decoder), bukan AI yang menentukan."*

---

## 5. Glossary Konsep Kunci

| Konsep | Definisi singkat | Lokasi belajar |
|--------|------------------|----------------|
| Cohort analysis | | Mode Analytics blog |
| RFM scoring | | Optimove blog / Putler |
| CLV (Customer Lifetime Value) | | HBR article |
| Retention rate | | |
| Churn complement | | |
| Quintile vs decile | | |
| pd.qcut() | | pandas docs |
| Heatmap cohort | | seaborn docs |

---

## 6. Self-Assessment Checklist

- [ ] Saya bisa baca heatmap cohort dan jelaskan trend dalam 30 detik
- [ ] Saya bisa explain RFM scoring step-by-step
- [ ] Saya bisa argue kenapa 5-quintile bukan 4 atau 10
- [ ] Saya bisa interpret CLV dan tau limitasinya (no profit, no cost data)
- [ ] Saya tau 1 segment yang akan saya prioritize dan kenapa
