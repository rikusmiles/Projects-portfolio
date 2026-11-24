# Autonomous Network Intrusion & SOC Flow Triage Engine (CTU-13)
### Applied Data & Digital Innovation Lab (LATAM) — Living Stones Foundation

![Copyright](https://img.shields.io/badge/License-All%20Rights%20Reserved-red.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)
![Frontend](https://img.shields.io/badge/Frontend-HTML5%20%7C%20TailwindCSS%20%7C%20Chart.js-sky.svg)
![Model](https://img.shields.io/badge/Model-Random%20Forest%20(AUC%200.9999)-emerald.svg)

> **PROPRIETARY & CONFIDENTIAL NOTICE:**  
> Copyright © 2026 Anushka Sinha & Living Stones Foundation. **All Rights Reserved.**  
> Unauthorized copying, cloning, distribution, modification, or commercial/academic reuse of this codebase, machine learning architecture, telemetry data, or dashboard interface, via any medium, is strictly prohibited without prior written permission from the author.

---

## 1. Executive Summary & Objective
The **Autonomous Network Intrusion & SOC Flow Triage Engine** is an end-to-end cybersecurity analytics and Security Operations Center (SOC) triage platform developed within the **Living Stones Foundation Applied Data & Digital Innovation Lab (LATAM)**.

Using the **CTU-13 NetFlow Capture** (`92,212` total network flows across `58` statistical features), this pipeline transforms raw packet telemetry into actionable threat intelligence:
* **Behavioral Threat Profiling:** Establishes baseline network patterns, uncovering a **3.37x higher SYN flag rate**, **9.4x longer median flow duration** (`397ms` vs. `42ms`), and unilateral **0-byte return payload asymmetry** in botnet and scanning traffic.
* **Zero-Leakage ML Pipeline:** Extracts a curated **12-feature subset** scaled via `RobustScaler` (Median/IQR) to handle extreme network throughput skews without data leakage.
* **High-Precision Detection:** Achieves **99.68% accuracy** and **0.9999 ROC-AUC** on an unseen `23,053`-flow holdout validation set.
* **Interactive SOC Triage Console (`index.html`):** Operationalizes model probabilities into calibrated **0–100 Threat Severity Scores** mapped to the **MITRE ATT&CK** framework.

---

## 2. Repository Contents

| File Name | Description |
| :--- | :--- |
| `index.html` | Standalone, responsive SOC Triage Dashboard (HTML5, Tailwind CSS, Chart.js). |
| `CTU13_EDA_Livingston.ipynb` | Master Google Colab notebook containing EDA, feature selection, modeling, and dashboard compilation. |
| `ctu13_eda_livingston.py` | Clean, standalone Python script export of the end-to-end analytical pipeline. |
| `model_evaluation_metrics.png` | Confusion Matrix (`13,301 TN`, `9,678 TP`, `28 FP`, `46 FN`) and ROC-AUC performance curves. |
| `SOC_CTU13_Triage_Telemetry.csv` | Exported SOC triage log containing scored flow telemetry and MITRE ATT&CK mappings. |
| `CTU13_Exploratory_Data_Analysis_Summary.xlsx` | 4-tab statistical summary workbook (Executive Overview, TCP Flags, Timing/Volume, Top Correlations). |
| `CTU13_Model_Training_Evaluation_Summary.xlsx` | 4-tab model benchmark workbook (Classifier Metrics, Confusion Matrix, Feature Architecture). |

---

## 3. Model Validation & SOC Operational Architecture
To adhere to Business Intelligence and SOC engineering best practices, the dashboard explicitly separates offline model evaluation from raw dataset context and live operations:

### A. Raw Dataset Context (`92,212` Total Captured Flows)
* **Benign Flows (`Label = 0`):** `53,314` (`57.82%`)
* **Attacks in Dataset (`Label = 1`):** `38,898` (`42.18%`)

### B. Offline Model Validation (`23,053` Holdout Test Set — 25% Split)
| Metric | Random Forest (Primary) | HistGradientBoosting | Isolation Forest (Unsupervised) |
| :--- | :---: | :---: | :---: |
| **Test Accuracy** | **99.68%** | 99.67% | 68.88% |
| **Attack Precision** | **99.71%** | 99.67% | 82.38% |
| **Intercepted Attacks (Recall / TP)** | **9,678 / 9,724 (99.53%)** | 99.54% | 33.37% |
| **Missed Attacks (False Negatives)** | **46 / 9,724 (0.47%)** | 45 (0.46%) | 6,479 (66.63%) |
| **False Alarms (False Positives)** | **28 / 13,329 (0.21%)** | 32 (0.24%) | 694 (5.21%) |
| **ROC-AUC Score** | **0.9999** | 0.9999 | N/A |

### C. Curated 12-Feature Subset
`Flow IAT Min`, `Init Bwd Win Byts`, `Pkt Len Std`, `Pkt Len Mean`, `SYN Flag Cnt`, `FIN Flag Cnt`, `Bwd IAT Min`, `TotLen Bwd Pkts`, `Tot Bwd Pkts`, `Flow Duration`, `Flow Byts/s`, `Active Min`.

---

## 4. Quickstart & Deployment

### View the Interactive Dashboard
* **Browser Preview:** Open `index.html` directly in any modern web browser (zero build steps or server dependencies required).
* **cPanel / Shared Hosting:** Upload `index.html` into your `public_html/` directory (`644` file permissions).

### Run the Python Pipeline
```bash
# Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl

# Execute the pipeline script
python ctu13_eda_livingston.py
