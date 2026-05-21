# Project Defense Brief — A/B Testing & Experimentation

> **Tujuan:** Catatan teknis & fundamental untuk dipertanggungjawabkan di interview.
> Isi dengan **bahasa sendiri**. Yang gagal dijelaskan = yang perlu dipelajari ulang.

---

## 1. Fact Sheet

| Item | Detail |
|------|--------|
| Dataset | ab_data.csv (Kaggle), ~290k users |
| Domain | Product/marketing experimentation |
| Test design | 21-day test, 50/50 split control vs treatment |
| Conversion test | Z-test for proportions |
| Revenue test | Welch's t-test (unequal variance) + bootstrap CI (10k iter) |
| Power analysis | MDE table, alpha=0.05, power=0.80 |
| Verdict | NO-GO (no significant difference) |
| AI Layer (notebook 06) | OpenRouter `openai/gpt-oss-120b:free` auto-narrative |

---

## 2. Defense Questions

### 2.1 Apa yang dilakukan? (1 paragraf executive)
> *Apa pertanyaan bisnisnya, gimana test designed, hasilnya apa, rekomendasinya apa.*



### 2.2 Kenapa z-test untuk conversion (proporsi), bukan chi-square?
> *Z-test untuk 2 proporsi: equivalent dengan chi-square untuk 2×2 contingency table. Z lebih natural untuk arah (1-tailed vs 2-tailed). Kapan chi-square lebih cocok? (>2 groups).*



### 2.3 Kenapa Welch's t-test untuk revenue, bukan Student's t-test?
> *Welch's tidak asumsikan equal variance (heteroskedastisitas). Revenue per user biasanya skewed dengan variance berbeda antar grup. Student's = subset case dari Welch.*



### 2.4 Bootstrap CI — kenapa 10,000 iterasi? Kenapa CI bukan p-value?
> *Bootstrap = resampling untuk estimasi distribusi statistik. 10k = balance antara stability dan compute time. CI memberikan range, p-value hanya binary signal — CI lebih informatif untuk business decision.*



### 2.5 Power analysis — apa itu MDE? Kenapa alpha=0.05 dan power=0.80?
> *MDE = Minimum Detectable Effect. Alpha 0.05 = Type I error rate (false positive). Power 0.80 = 1 - Type II error (true positive rate). Ini convention industri, BUKAN aturan keras.*



### 2.6 Asumsi yang dicek
> *Random assignment (cek balance dengan SRM test)? Independence (tidak ada user duplikat)? Distribusi revenue (skewness)? Sample ratio mismatch?*



### 2.7 Verdict NO-GO — kenapa ini valid result, bukan failure?
> *Industri rata-rata: 70% A/B test tidak beat baseline. NO-GO menghindari ship feature yang tidak improve metric. Lebih bahaya: false positive yang ship feature buruk.*



### 2.8 Limitasi
> *Test 21 hari mungkin kurang lama (novelty effect masih ada di 2 minggu pertama). Tidak ada segmentasi per device/region. Tidak account untuk seasonality.*



### 2.9 Business interpretation
> *Marketing tim minta lift 5% — actual -1.31%. Apa next step? Re-test dengan variasi lain? Investigasi kenapa tidak work? Atau accept dan move on?*



---

## 3. Likely Interview Questions

1. **"Apa itu A/B testing?"** — Controlled experiment dengan random assignment untuk causal inference.
2. **"Bedakan Type I dan Type II error."** — Type I = false positive (alpha), Type II = false negative (beta). Trade-off: turunkan alpha, naikkan beta.
3. **"P-value 0.19 — apa artinya?"** — Probability of observing this result (or more extreme) jika null hypothesis benar. BUKAN probability that null hypothesis is true.
4. **"Apa beda confidence interval dengan p-value?"** — CI = range of plausible values. P-value = single number. CI lebih kaya informasi.
5. **"Cohen's d -0.003 — apa artinya?"** — Effect size sangat kecil; bahkan kalau significant, business impact negligible.
6. **"Sample size 290k — kenapa masih tidak significant?"** — Karena effect size kecil. Statistical significance ∝ effect_size × sqrt(n). Kalau effect mendekati 0, n besar pun tidak save.
7. **"Apa itu Simpson's paradox? Bagaimana cara cek di A/B test?"** — Aggregated result bisa berlawanan dengan disaggregated. Cek dengan segmentasi.
8. **"Sequential testing — kenapa berbahaya?"** — Multiple peeking inflate Type I error. Solusi: pre-register test duration atau pakai sequential testing methods (mSPRT).
9. **"Novelty effect — apa itu?"** — Treatment unggul awalnya karena user excited; effect menghilang setelah beberapa minggu.
10. **"Network effects — kapan A/B testing tidak valid?"** — Kalau treatment satu user pengaruhi user lain (social, marketplace), random assignment broken.

---

## 4. AI Usage — Honest Framing

> *"Pemilihan z-test untuk proporsi, Welch's untuk revenue, dan bootstrap untuk CI — itu keputusan saya berdasarkan statistical inference textbook (Wasserman 'All of Statistics', Kohavi 'Trustworthy Online Controlled Experiments'). AI membantu generate scipy boilerplate dan format MDE table. Untuk AI narrative layer (notebook 06), saya design system prompt dengan STATISTICAL SAFEGUARDS supaya LLM tidak hallucinate interpretasi p-value — itu sengaja dilakukan karena LLM rentan salah interpretasi statistik frequentist."*

---

## 5. Glossary Konsep Kunci

| Konsep | Definisi singkat (30 detik) | Lokasi belajar |
|--------|----------------------------|----------------|
| Null hypothesis (H0) | | StatQuest |
| Alpha / Type I error | | |
| Beta / Type II error | | |
| Power (1-beta) | | |
| Effect size (Cohen's d) | | |
| Bootstrap | | "All of Statistics" Ch.8 |
| Welch's t-test | | Wikipedia |
| Z-test for proportions | | |
| MDE (Minimum Detectable Effect) | | |
| Confidence interval | | |
| P-value (correct interpretation) | | "Mindless Statistics" Gigerenzer |
| Sample Ratio Mismatch (SRM) | | Kohavi blog |
| Novelty effect | | Kohavi 2020 book |

---

## 6. Self-Assessment Checklist

- [ ] Saya bisa explain p-value correctly (bukan "probability H0 benar")
- [ ] Saya bisa derive sample size formula minimal untuk z-test
- [ ] Saya tau kapan pakai 1-tailed vs 2-tailed test
- [ ] Saya bisa explain kenapa NO-GO bukan failure
- [ ] Saya tau 3 reason A/B test bisa misleading (Simpson's, novelty, network effect)
- [ ] Saya bisa bedakan statistical significance vs practical significance
