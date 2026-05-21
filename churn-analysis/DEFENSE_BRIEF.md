# Project Defense Brief — Customer Churn Prediction

> **Tujuan:** Catatan teknis & fundamental untuk dipertanggungjawabkan di interview.
> Isi dengan **bahasa sendiri**. Yang gagal dijelaskan = yang perlu dipelajari ulang.

---

## 1. Fact Sheet

| Item | Detail |
|------|--------|
| Dataset | IBM Telco Customer Churn, 7,043 pelanggan |
| Domain | Telco retention / customer lifetime |
| Churn rate | ~26.5% (class imbalance moderate) |
| Models | Logistic Regression (baseline) + Random Forest (candidate) |
| Performance | AUC 0.83, recall churn 78% |
| Explainability | SHAP TreeExplainer (notebook 05) |
| MLflow | 4 runs logged (LR baseline/tuned, RF baseline/tuned) di notebook 06 |

---

## 2. Defense Questions

### 2.1 Apa yang dilakukan? (1 paragraf executive)
> *Elevator pitch — apa masalah bisnisnya, gimana solve-nya, hasilnya apa.*



### 2.2 Kenapa Logistic Regression + Random Forest (2 model, bukan 1)?
> *Standar baseline → candidate. Apa fungsi tiap model? Apa yang dibandingkan?*



### 2.3 Kenapa `class_weight='balanced'` (bukan SMOTE atau undersampling)?
> *Pertimbangan: data tidak tambah, recall meningkat, tapi precision turun. Kapan SMOTE lebih cocok?*



### 2.4 AUC 0.83 — itu bagus atau jelek?
> *Benchmark: random = 0.5, sempurna = 1.0. Industri telco churn biasanya 0.75-0.85. Konteks kenapa 0.83 layak deploy.*



### 2.5 Recall churn 78% — kenapa fokus ke recall, bukan accuracy?
> *Hint: cost of false negative (pelanggan churn tidak terdeteksi) >> cost of false positive (pelanggan loyal di-retain padahal tidak perlu).*



### 2.6 Asumsi apa yang dicek?
> *Multikolinearitas (VIF)? Distribusi feature? Stratified split untuk class imbalance? Random seed?*



### 2.7 SHAP — apa beda global vs local explanation?
> *Global = feature importance over dataset. Local = kenapa pelanggan X diprediksi churn. Mana yang lebih berguna untuk stakeholder?*



### 2.8 Limitasi
> *Dataset statis (snapshot), tidak ada time-series. Tidak ada cost-sensitive learning. Threshold default 0.5 belum dioptimize.*



### 2.9 Business interpretation
> *Kalau model bilang 200 pelanggan akan churn bulan depan — apa yang dilakukan bisnis? Berapa budget retention yang reasonable?*



---

## 3. Likely Interview Questions

1. **"Apa beda Logistic Regression dengan Random Forest secara intuisi?"** — Garis pemisah vs forest of decision trees.
2. **"Kalau AUC LR = 0.82 dan RF = 0.83, beda 0.01 — apakah RF significantly better?"** — Statistical significance vs practical significance.
3. **"Kenapa stratified split, bukan random split?"** — Untuk class imbalance, supaya proporsi churn sama di train/test.
4. **"Apa itu confusion matrix? Bedakan precision, recall, F1."** — Wajib hafal definisi dan kapan pakai yang mana.
5. **"SHAP itu apa? Beda dengan feature importance Random Forest?"** — Shapley value dari game theory; SHAP additive dan konsisten.
6. **"Bagaimana cara deploy model ini ke production?"** — Pickle/joblib + API endpoint atau batch scoring; monitoring drift.
7. **"Kalau dataset baru datang, model perlu retrain kapan?"** — Concept drift detection (perubahan distribusi feature atau target).
8. **"Apa itu MLflow yang kamu pakai? Kenapa perlu?"** — Experiment tracking; tanpa itu sulit reproducible.
9. **"Pelanggan dengan AUC tinggi seharusnya churn, tapi ternyata loyal — kenapa bisa salah?"** — Edge cases, missing features (kompetitor pricing, customer service incident).

---

## 4. AI Usage — Honest Framing

> *"Pemilihan LR + RF, metrik recall sebagai primary, dan SHAP untuk explainability — itu keputusan saya berdasarkan literatur churn analytics. AI membantu generate scikit-learn boilerplate dan debug code. Untuk SHAP, saya validasi dengan baca paper Lundberg & Lee 2017 supaya paham basis matematisnya, bukan sekadar copy-paste output."*

---

## 5. Glossary Konsep Kunci

| Konsep | Definisi singkat (30 detik) | Lokasi belajar |
|--------|----------------------------|----------------|
| Logistic Regression | | StatQuest YouTube |
| Random Forest | | StatQuest YouTube |
| AUC / ROC | | StatQuest YouTube |
| Precision vs Recall | | Wikipedia |
| Class imbalance | | imbalanced-learn docs |
| SHAP value | | Lundberg & Lee 2017 paper |
| Stratified sampling | | sklearn docs |
| TreeExplainer | | SHAP docs |
| Confusion matrix | | |
| Cross-validation | | |

---

## 6. Self-Assessment Checklist

- [ ] Saya bisa jelaskan project ini dalam 60 detik tanpa catatan
- [ ] Saya bisa derive formula AUC tanpa lihat (intuisi cukup, tidak perlu kalkulus)
- [ ] Saya bisa interpret SHAP plot tanpa baca catatan
- [ ] Saya tau kenapa F1 ≠ accuracy ≠ recall
- [ ] Saya bisa argumentasi kenapa RF tuned > LR baseline dari MLflow runs
