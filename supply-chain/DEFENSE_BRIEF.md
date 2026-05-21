# Project Defense Brief — Supply Chain Optimization

> **Tujuan:** Catatan teknis & fundamental untuk dipertanggungjawabkan di interview.
> Isi dengan **bahasa sendiri**. Yang gagal dijelaskan = yang perlu dipelajari ulang.

---

## 1. Fact Sheet

| Item | Detail |
|------|--------|
| Dataset | DataCo Supply Chain, ~180k transaksi, `encoding='latin-1'` |
| Domain | Operations / logistics analytics |
| ABC analysis | Pareto 80/20 inventory classification (A/B/C tier) |
| Reorder Point | ROP = (avg_daily_demand × lead_time) + safety_stock |
| Safety stock | Z=1.645 (95% service level) |
| Late delivery model | Logistic Regression + Random Forest, AUC 0.90+ |
| Explainability | SHAP TreeExplainer (notebook 07), `max_depth=10` untuk avoid 39-min runtime |

---

## 2. Defense Questions

### 2.1 Apa yang dilakukan? (1 paragraf executive)
> *Multi-faceted: inventory classification, reorder optimization, prediksi keterlambatan. Apa benang merahnya?*



### 2.2 Apa itu ABC analysis? Kenapa Pareto 80/20?
> *A = top 20% items contribute 80% revenue; B = next 30% contribute 15%; C = remaining 50% contribute 5%. Implikasi: prioritas inventory management berbeda per tier.*



### 2.3 Reorder Point formula — break down per komponen
> *ROP = lead_time_demand + safety_stock. Lead time demand = avg_daily_demand × lead_time. Safety stock = Z × std_dev × sqrt(lead_time).*



### 2.4 Kenapa Z=1.645 (bukan 1.96 atau 2.33)?
> *Z=1.645 → 95% service level (single-tail). Z=1.96 → 95% confidence interval (two-tail). Z=2.33 → 99% service level. Trade-off: higher Z = more safety stock = more holding cost.*



### 2.5 Service level — apa artinya 95%?
> *Probability stock tidak habis selama lead time. Bukan accuracy prediction model. Trade-off: 95% lebih murah dari 99%, tapi lebih sering stockout.*



### 2.6 Late delivery model — kenapa LR + RF, dan kenapa RF menang?
> *LR baseline untuk interpretability. RF untuk capture non-linear interaction (mis. shipping mode × region × season). AUC 0.90+ menunjukkan RF lebih kuat untuk task ini.*



### 2.7 SHAP `max_depth=10` — kenapa harus shallow?
> *TreeExplainer complexity scales dengan tree depth. Default unlimited depth bikin SHAP 39+ menit. max_depth=10 cut ke <1 menit, plus reduce overfit. Lesson: explainability butuh model lebih sederhana dari production model.*



### 2.8 Asumsi yang dicek
> *Lead time distribusi normal? Daily demand stationary? Outlier handling (extreme late delivery)? Train-test split temporal atau random?*



### 2.9 Limitasi
> *Lead time assumed normal — kalau bimodal (mis. air vs sea shipping mixed), Z formula tidak tepat. Tidak ada cost optimization (only quantity). Tidak account untuk supplier reliability.*



### 2.10 Business interpretation
> *Item A dengan lead time 14 hari, demand 100/hari, std 20 — berapa ROP? Apa artinya untuk procurement team?*



---

## 3. Likely Interview Questions

1. **"Apa itu Pareto principle?"** — 80/20 distribution; vital few drive most outcomes.
2. **"Bedakan ABC dengan XYZ analysis."** — ABC = by revenue/volume. XYZ = by demand variability. Kombinasi (A-X, A-Y...) → 9 strategies.
3. **"Apa itu safety stock? Kenapa perlu?"** — Buffer untuk variability demand & lead time. Tanpa itu, stockout sering kalau ada lonjakan.
4. **"Kalau lead time bertambah 50%, ROP berubah berapa?"** — Linear di lead_time_demand, sqrt di safety stock. Total > 50% naik.
5. **"AUC 0.90 — itu suspicious atau bagus?"** — Konteks: kalau late delivery rate 30%, AUC 0.90 plausibel. Cek apakah ada data leakage (feature yang tidak available saat prediksi).
6. **"SHAP — gimana cara baca summary plot?"** — Y axis: features sorted by importance. X axis: SHAP value. Warna: feature value (red=high, blue=low).
7. **"Kalau saya CEO supply chain, apa 1 hal yang harus saya prioritize berdasarkan analisis ini?"** — Latihan: pilih SATU rekomendasi dan defend.
8. **"Bagaimana cara monitor model late delivery di production?"** — Drift detection: feature distribution monitoring, performance drop alert, periodic retraining.
9. **"Apa itu bullwhip effect?"** — Demand variability amplifies upstream supply chain. Bonus poin kalau tau.

---

## 4. AI Usage — Honest Framing

> *"Konsep ABC analysis dan ROP formula dari textbook operations management (Chopra & Meindl 'Supply Chain Management'). AI bantu implement Python code dan SHAP integration. Lesson penting yang saya temukan sendiri: default RF dengan unlimited depth bikin TreeExplainer 39+ menit — saya yang debug dan kasih solusi `max_depth=10`. Itu real engineering insight, bukan dari AI."*

---

## 5. Glossary Konsep Kunci

| Konsep | Definisi singkat (30 detik) | Lokasi belajar |
|--------|----------------------------|----------------|
| Pareto principle (80/20) | | Wikipedia |
| ABC analysis | | Chopra & Meindl textbook |
| Reorder Point (ROP) | | |
| Safety stock | | |
| Service level | | Inventory management blog |
| Lead time | | |
| Lead time variability | | |
| Z-score (1.645 = 95% one-tail) | | Stats textbook |
| Bullwhip effect | | Lee, Padmanabhan, Whang 1997 |
| TreeExplainer complexity | | SHAP docs |
| AUC ROC | | StatQuest |
| Data leakage | | |

---

## 6. Self-Assessment Checklist

- [ ] Saya bisa derive ROP formula tanpa lihat catatan
- [ ] Saya bisa explain Z=1.645 vs 1.96 vs 2.33 (one-tail vs two-tail)
- [ ] Saya bisa baca SHAP summary plot dan interpret 3 feature teratas
- [ ] Saya tau kenapa AUC 0.90+ untuk late delivery plausible (kalau tidak ada leakage)
- [ ] Saya bisa argumentasi 1 business recommendation top dari proyek ini
- [ ] Saya tau apa itu bullwhip effect (bonus untuk supply chain expertise signal)
