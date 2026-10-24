# Rezumat — IDS cu ML pe Raspberry Pi (PLoS One, 2025)

> **Titlu:** *A cost effective machine learning based network intrusion detection system using
> Raspberry Pi for real time analysis*
> **Autori:** R.W.K.S. Wijethilaka, Kanishka Yapa, Deemantha Siriwardena
> (Sri Lanka Institute of Information Technology)
> **Publicație:** PLoS One, 20(12):e0331123 · **An:** 2025 (primit 2024-10-24, acceptat 2025-08-11)
> **DOI:** 10.1371/journal.pone.0331123 · **Link:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12747338/ (PMC, acces liber)
>
> *Rezumat realizat din lectura articolului. Verifică cifrele exacte direct în articol înainte de a le
> cita în lucrare (vezi §„Citire critică").*

---

## TL;DR (3 fraze)

Autorii construiesc un IDS ieftin bazat pe ML, care rulează pe un **Raspberry Pi 4** și clasifică
traficul de rețea în timp real, alertând prin **email + LED/buzzer**. Compară mai multe modele și
aleg **Random Forest** (acuratețe raportată **96.5%**), antrenat pe dataset-ul **NF-UQ-NIDS**.
Sistemul **doar alertează** (nu blochează traficul), iar evaluarea e făcută într-un lab controlat, nu
pe o rețea reală.

---

## 1. Obiectiv & motivație
IDS accesibil pentru **IMM-uri** (SMB). Argumentele: sistemele bazate pe semnături ratează
amenințările noi/zero-day, iar majoritatea IDS-urilor ML cer hardware scump. Soluția lor analizează
trafic inbound/outbound, clasifică atacul și trimite alerte.

## 2. Hardware
- **Raspberry Pi 4** (varianta de RAM nu e precizată în articol).
- **Fără accelerator AI** (Tabelul 5: „No dedicated AI acceleration").
- Periferice: Ethernet, microSD, breadboard cu LED verde (normal), LED roșu + buzzer (atac), GPIO.

## 3. Dataset & clase de atac
- **Dataset:** NF-UQ-NIDS. Articolul **nu** raportează numărul total de eșantioane / pe clasă.
- **Tipuri de atac menționate:** DoS, SQL Injection, Port Scanning, Malware, Exploits,
  Reconnaissance, MITM „și altele" (numărul total de clase nu e precizat).
- Atacurile sunt mapate la **OWASP Top 10** și **MITRE ATT&CK** (ex. T1498 = DoS, T1046 = port scan).

## 4. Preprocesare & features
- Curățare (valori lipsă, duplicate, inconsistențe).
- Scalare **Min-Max** (0–1) + **Z-score** pentru features gaussiene; **one-hot** pentru categorice (ex. protocol).
- Reducere de dimensionalitate: **PCA** + **RFE** (Recursive Feature Elimination).
- Features temporale: inter-arrival time între pachete, durata flow-ului.
- Dezechilibru de clase tratat cu **SMOTE**.
- Split **70/30 stratificat** + **10-fold cross-validation**.
- Tuning: **Grid Search** + **Randomized Search** (`n_estimators`, `max_depth`, min. samples/split).

## 5. Modele comparate
Random Forest, XGBoost, Naïve Bayes, LSTM, ANN, SVM. **Random Forest = modelul ales** pentru deployment.

## 6. Analiză în timp real
- Captură cu **pyshark** + **tcpdump** pe interfața de rețea.
- Extragere features + clasificare **pe Pi**, cu model pre-antrenat.
- Unelte auxiliare: Wireshark (inspecție), pandas/NumPy (date), Splunk (monitorizare în teste).
- **Alerte:** LED roșu + buzzer la detecție; **smtplib** trimite email cu IP sursă/destinație,
  timestamp și sumar de pachet.

## 7. Rezultate

**Random Forest (Tabelul 3):**

| Metrică | Valoare |
|---|---|
| Accuracy | **96.5%** |
| Precision | 94.1% |
| Recall | 95.5% |
| F1 | 94.8% |

**Alte modele (Tabelul 3):** Naïve Bayes acc. 85.7% / F1 83.1% · XGBoost acc. 92.3% / F1 82.7% ·
SVM acc. 90.6% / F1 89.4% · LSTM acc. 88.4% / F1 87.5%.

**Latență / resurse:** abstractul menționează un „average response time of **50 ms**", **fără**
metodologie de măsurare. **Nu** se raportează consum CPU/RAM și nici timp de inferență pe Pi.

**Comparație cu alte IDS/firewall (Tabelul 4):** Snort 89.2%, Suricata 91.5%, Palo Alto 98.3%,
Cisco Firepower 97.6%. Costul hardware al soluției lor: **$50–$100**.

**Simulări de atac (doar calitativ):** DoS/DDoS (Hping3), recon (Nmap), SQLi (SQLMap), MITM (Ettercap),
XSS, brute force (Hydra), ransomware-like, exploits/fuzzing, data theft — „aliniate cu rezultatele
așteptate", dar **fără metrici per-atac**.

## 8. Răspuns / mitigare
Doar **alertare** (LED, buzzer, email). Sistemul **nu blochează** traficul și **nu** descrie mitigare automată.

## 9. Limitări (recunoscute de autori)
- Nu au testat Pi-ul sub **trafic mare**.
- Testare doar în **lab controlat**, nu pe rețea reală de IMM.
- Nu au analizat evaziunea adversarială, malware polimorf, resource exhaustion.
- Impactul SMOTE asupra ratelor de fals-pozitiv/negativ „nu e analizat complet".
- Comparația cu alte edge devices (Jetson Nano, Odroid) e doar la nivel de specificații (Tabelul 5).

## 10. Concluzii & work viitor
Concluzie: soluție **cost-effective**, ușor de folosit, pentru IMM-uri. Viitor: deployment real +
colectare de date reale, testbed-uri virtualizate (GNS3/Mininet/CloudLab), stress-testing (latență,
packet drop, overhead pe Pi vs. alte edge devices), antrenare adversarială, filtrare/rate-limiting,
detecție nesupervizată de anomalii.

---

## Citire critică (observații, de verificat în articol)

Lectura a semnalat câteva **neconcordanțe interne** — utile de menționat ca analiză critică:

- **Tabelul 2 vs. Tabelul 3** dau acurateți diferite pentru aceleași modele (ex. XGBoost 95.8% vs.
  92.3%, LSTM 94.2% vs. 88.4%, Naïve Bayes 89.5% vs. 85.7%); Tabelul 2 include și ANN (93.7%), absent în Tabelul 3.
- **F1 XGBoost (82.7%)** e mai mic decât ar rezulta din precision/recall (~90.6% ca medie armonică).
- Acuratețea „previous research" pentru RF (95.96%) e atribuită unei referințe despre *infrastructure
  asset management* (posibil citare greșită).
- Abstractul scrie „96.5 detection accuracy" **fără** semnul `%`.
- **Fără** confusion matrix numeric (doar figuri) și **fără** măsurători reale de CPU/RAM/inferență pe Pi.

---

## Relevanță pentru Aurora (de ce contează pentru lucrarea mea)

| Aspect | Articolul PLoS One | Aurora (proiectul meu) |
|---|---|---|
| Hardware | Pi 4 (RAM nespecificat) | Pi 4 **2 GB** (constrângere explicită, documentată) |
| Dataset | NF-UQ-NIDS | **CICIDS2017 re-etichetat** + **date proprii** din lab |
| Model | Random Forest | Random Forest (confirmă alegerea) + detector ARP dedicat |
| Timp real | pyshark + tcpdump pe Pi | senzor flow-based pe Pi (scapy/tshark), schema unică de features |
| Răspuns | **doar alertă** (email/LED) | **răspuns automat** (iptables + alertă) → *aici depășesc articolul* |
| Latență/resurse | „50 ms", fără metodologie | **măsor explicit** latența + CPU/RAM pe Pi (psutil) → *contribuție* |
| Contribuție extra | — | clasa nouă **`SPOOFING`** (ARP), absentă din benchmark-uri |

**Idei de preluat la susținere:**
1. Articolul **validează direcția** (RF ieftin pe Pi 4 pentru IDS real-time), deci e o referință bună
   pentru „state of the art".
2. **Lacunele lui sunt oportunitățile mele:** nu măsoară resurse/latență riguros, răspunde doar prin
   alertă, nu acoperă spoofing L2 → eu adaug exact aceste lucruri (măsurători pe 2 GB, răspuns automat,
   clasa `SPOOFING`).
3. Maparea lor la **MITRE ATT&CK / OWASP** e un model bun de urmat pentru taxonomia mea.
