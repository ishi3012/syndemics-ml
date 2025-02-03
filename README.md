# Syndemics Analysis using Machine Learning and Network Analysis

## Overview

This project explores disease interactions through a syndemics framework, leveraging **machine learning clustering techniques** and **network analysis** to identify co-occurring diseases influenced by **social, environmental, and psychological factors**. Using a dataset of **95,000 patients from Chicago**, this project aims to help **physicians better understand and treat patients** by identifying disease clusters and their socio-economic drivers.


## Deep Dive Alert! 🚀

Want to understand the brains behind this project? 🤖💡 Check out my blog:

[Unlocking the Syndemics Approach: How Machine Learning Reveals Disease Interactions](https://ishi3012.github.io/the-code-diary/Syndemics/syndemics_intro.html)

## Features

- **Clustering Analysis**: Implements **K-Means** and **K-Modes** to identify patient clusters based on disease prevalence.
- **Observed-to-Expected Ratio (OER)**: Measures co-occurrence of diseases beyond expected random association.
- **Network Analysis**: Visual representation of disease interactions to uncover hidden patterns.
- **Data Preprocessing**: Includes **race discretization, primary care visit categorization, and missing data handling**.
- **Disease Correlations**: Identification of syndemic relationships such as **Endometrial Cancer & Lung Cancer (OER = 8.4)** and **Asthma & Pneumonia (OER = 4.3)**.

## Data Source

- **Chicago Area Patient-Centered Outcomes Research Network (CAPriCORN)**
- Electronic Health Records (EHR) from **Rush System (2016-2022)**
- **Dataset**: ~93,994 patients, 30 disease attributes, and 6 socio-economic indicators (e.g., race, insurance, age)

## Methodology

### 1. Machine Learning Clustering
- **Algorithms Used**:
  - **K-Means & K-Modes** for patient clustering
  - Optimal **k = 16** clusters determined using elbow plots and **Adjusted Rand Index (ARI)**.
- **Validation Metrics**:
  - **Silhouette Scores** (Best clusters: **K-Modes Cluster_4 & K-Means Cluster_7**)
  - **ARI scores**: Best clustering performance at **k = 16**.

### 2. Observed-to-Expected Ratio (OER)
- Measures how frequently diseases co-occur compared to their expected occurrence.
<!-- - **Formula**:  
  ```math
  OER = \frac{Observed Coexistence(i, j)}{Expected Coexistence(i, j)}
```math -->

### 3. Network Analysis for Disease Interactions
- Graph-based representation of disease interactions.
- Identifies highly connected disease nodes, revealing underlying syndemic relationships.

## Key Findings
| OER  | Disease 1            | Disease 2                  |
|------|----------------------|----------------------------|
| 8.4  | Endometrial Cancer   | Lung Cancer               |
| 5.0  | Endometrial Cancer   | Non-Alzheimer’s Dementia  |
| 4.3  | Asthma               | Pneumonia                 |
| 2.9  | Asthma               | Endometrial Cancer        |
| 2.7  | Asthma               | Hypothyroidism            |

- Outliers (25+ primary care visits over 7 years) were predominantly Black patients, suggesting social determinants play a critical role in healthcare access and outcomes.
- High disease clustering among certain demographics supports the hypothesis that social factors influence disease progression.

## Future Work
- Incorporate genetic, environmental, and lifestyle factors (e.g., BMI, smoking, Social Vulnerability Index).
- Develop predictive models to forecast patient outcomes based on identified disease clusters.
- Implement integrated treatment strategies for physicians to improve patient management.

## Installation & Usage
```bash
# Clone the repository
git clone https://github.com/ishi3012/syndemics-ml.git

# Install dependencies
pip install -r requirements.txt

# Run the analysis
python main.py

```

## References
- Singer, M., Bulled, N., Ostrach, B., & Mendenhall, E. (2017). Syndemics and the biosocial conception of health. Lancet, 389(10072), 941-950.
- Lee, H. A., & Park, H. (2021). Comorbidity network analysis related to obesity in middle-aged and older adults. Epidemiol Health.
- Huang, Z. (1997). Clustering large data sets with mixed numeric and categorical values. Pacific Asia Knowledge Discovery and Data Mining Conference.

