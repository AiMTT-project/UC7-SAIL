# Learning Module: Crowd Management During Events

Discover how data science and artificial intelligence can improve crowd management during large-scale public events. Based on the AIM-TT (AI for Mobility and Transport Transition) crowd management use case developed around the SAIL Amsterdam 2025 event, this repository provides hands-on Python notebooks and reference materials designed to accompany the video learning module.

The learning series walks through the entire event lifecycle step by step, covering data sharing architectures, crowd simulation, Level of Service assessments, real-time monitoring, threshold alerting, probabilistic crowd forecasting, and operational data archiving.

---

## Target Audience

This learning module bridges the gap between data science and operational safety management:

- **Data Scientists**: Learn how to build production-grade feature pipelines, train probabilistic gradient-boosted time series models, apply online Kalman filters for sensor correction, and design spatial map visualisations and GIS styles.
- **Crowd Managers and Safety Professionals**: Understand how sensor networks, Level of Service thresholds, early alerting mechanisms, and predictive models translate into timely crowd management interventions.

---

## Curriculum and Video Mapping

The learning module consists of 19 video lectures organised into four sequential chapters. The table below outlines the full syllabus, the partner organisations, the authors, and links to the practical deep-dive notebooks in this repository.

### Chapter 1: Introduction (Inleiding)

| Unit | Title | Author / Speaker | Organisation | Format and Duration | Practical Material |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1.1** | Introduction: SAIL | Roland Geraerts | uCrowds | Video (7:16) | Practical context and FOOV goals |
| **1.2** | Introduction: Crowd Management | Winnie Daamen | TU Delft | Video (10-15 min) | Theory and background |
| **1.3** | Introduction: Data Sharing | Kevin Otjes | Analyze | Video (10-15 min) | Data requirements and DPIA |
| **1.4** | Introduction: Scenarios | Roland Geraerts | uCrowds | Video (15:41) | Scenario development |

### Chapter 2: Preparation Phase (Koude en Lauwe Fase)

| Unit | Title | Author / Speaker | Organisation | Format and Duration | Practical Material |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2.1** | Working with Stakeholders | Kevin Otjes | Analyze | Video (10-15 min) | Multi-disciplinary collaboration |
| **2.2** | Level-of-Service Concept | Winnie Daamen | TU Delft | Video (15 min) + 1h Deep Dive | [2.2 LOS Notebooks](./2.2%20LOS) |
| **2.3** | Visualisation | Kevin Otjes | Analyze | Video (10 min) + 1.5h Deep Dive | [2.3 Visualisatie Notebooks](./2.3%20Visualisatie) |
| **2.4** | Data Architecture for Data Sharing | Kevin Otjes | Analyze | Video (10-15 min) | Data Sharing House (DSH) usage |
| **2.5.1** | Crowd Simulation: Overview | Roland Geraerts | uCrowds | Video (30:06) | Simulation setup and parameters |
| **2.5.2** | Crowd Simulation: Theory | Roland Geraerts | uCrowds | Video (28:37) | Core principles of crowd models |
| **2.5.3** | Crowd Simulation Deep Dive | Roland Geraerts | uCrowds | Video (26:24) | Hands-on with SimCrowds |
| **2.5.4** | Crowd Simulation: Large Language Models | Roland Geraerts | uCrowds | Video (27:28) | LLMs for scenario generation |

### Chapter 3: Live Event Operations (Warme Fase)

| Unit | Title | Author / Speaker | Organisation | Format and Duration | Practical Material |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3.1** | Monitoring | Winnie Daamen | TU Delft | Video (10-15 min) | Multi-sensor monitoring in practice |
| **3.2** | Alerting | Kevin Otjes | Analyze | Video (10-15 min) + 2h Deep Dive | [3.2 Alerting Notebooks](./3.2%20Alerting) |
| **3.3.1** | Crowd Forecasting: Theory | Theivaprakasham Hari | TU Delft | Video (15-20 min) | Predictive modeling foundations |
| **3.3.2** | Introduction to Time Series Forecasting | Theivaprakasham Hari | TU Delft | Video (20-30 min) + 1-2h Deep Dive | [3.3 Starter Notebook](./3.3%20Crowd%20forecasting) |
| **3.3.3** | Advanced Time Series Forecasting | Theivaprakasham Hari | TU Delft | Video (30 min) + 2-4h Deep Dive | [3.3 Advanced Notebook](./3.3%20Crowd%20forecasting) |
| **3.4** | Evaluation During the Event | Kevin Otjes | Analyze | Video (10 min) + 1h Deep Dive | [3.4 Evaluation Notebooks](./3.4%20Evaluation%20during%20the%20event) |

### Chapter 4: Post-Event Evaluation (Evaluatie en Leren)

| Unit | Title | Author / Speaker | Organisation | Format and Duration | Practical Material |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4** | Evaluation of Crowd Management | Winnie Daamen | TU Delft | Video (10 min) | Post-event analysis and learning |

---

## Practical Notebooks Overview

Each practical unit contains both an **Assignment** notebook with exercises and an **Assignment-Solution** notebook with reference code and explanations.

| Folder | Module Topic | Key Concepts | Notebooks Included |
| :--- | :--- | :--- | :--- |
| [2.2 LOS](./2.2%20LOS) | Level of Service (LOS) Deep Dive | Fruin unidirectional standard, bidirectional flow thresholds, area-specific LOS, animated spatial output | `los.ipynb`<br>`los_answers.ipynb` |
| [2.3 Visualisatie](./2.3%20Visualisatie) | Crowd Data Visualisation | Capacity line charts, threshold styling, map rendering, web GIS styling (SLD, GeoStyler, Mapbox) | `visualisation_deepdive.ipynb`<br>`visualisation_deepdive_answers.ipynb` |
| [3.2 Alerting](./3.2%20Alerting) | Alert-Based Monitoring | Noise reduction, multi-source signal fusion (pedestrians, roads, waterways), moving averages, persistence filters | `alerts_deepdive.ipynb`<br>`alerts_deepdive_answers.ipynb` |
| [3.3 Crowd forecasting](./3.3%20Crowd%20forecasting) | Crowd Flow Forecasting (Starter & Advanced) | 3-minute sensor flow, feature engineering, LightGBM, quantile regression (P10/P50/P90), multi-step direct output, online Kalman filter, Plotly dashboards | `01_crowd_forecasting_starter_exercises.ipynb`<br>`02_crowd_forecasting_advanced_exercises.ipynb`<br>`01_crowd_forecasting_starter_solutions.ipynb`<br>`02_crowd_forecasting_advanced_solutions.ipynb` |
| [3.4 Evaluation during the event](./3.4%20Evaluation%20during%20the%20event) | Operational Data Archiving | Streaming data ingestion, format comparison (GeoJSON/CSV vs Parquet), temporal hourly partitioning for fast query performance | `archiving_deepdive.ipynb`<br>`archiving_deepdive_answers.ipynb` |

---

## Getting Started

### Prerequisites

To run the notebooks locally, you need Python 3.10 or higher. You can also run the notebooks in Google Colab or JupyterLab.

### Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-org/aimtt-crowd-management-notebooks.git
cd aimtt-crowd-management-notebooks
```

Install the core Python packages:

```bash
pip install pandas numpy matplotlib geopandas contextily lightgbm scikit-learn plotly pyarrow fastparquet imageio
```

### Running the Notebooks

1. Open your preferred environment (Jupyter Notebook, JupyterLab, VS Code, or Google Colab).
2. Navigate to the desired module folder.
3. Open the notebook inside the `Assignment` folder to work on the exercises, or refer to `Assignment-Solution` for the complete implementation.

---

## Contributing and Partners

This learning module was created as part of the AIM-TT project by:
- **TU Delft** (Delft University of Technology)
- **Analyze**
- **uCrowds**
