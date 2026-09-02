# Learning Module: Crowd Management During Events

Discover how data science and artificial intelligence can improve crowd management during large-scale public events. Based on the AiMTT (AI for Mobility and Transport Transition) crowd management use case developed around the SAIL Amsterdam 2025 event, this repository provides hands-on Python notebooks and reference materials designed to accompany the video learning module.

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

## Practical Notebooks and Dataset Summary

Each practical folder includes both an **Assignment** notebook with guided exercises and an **Assignment-Solution** notebook with reference implementations.

| Folder | Module Topic | Primary Datasets | Open in Colab Badge |
| :--- | :--- | :--- | :--- |
| [2.2 LOS](./2.2%20LOS) | Level of Service (LOS) Deep Dive | `LOS_deepdive_data.geojson`<br>`LOS_archive_data.geojson`<br>`los_alerts_deepdive_data.geojson` | [Open Starter](https://colab.research.google.com/github/AiMTT-project/use-case-1/blob/main/2.2%20LOS/Assignment/los.ipynb) |
| [2.3 Visualisatie](./2.3%20Visualisatie) | Crowd Data Visualisation | `visualisation_deepdive_data.geojson` | [Open Starter](https://colab.research.google.com/github/AiMTT-project/use-case-1/blob/main/2.3%20Visualisatie/Assignment/visualisation_deepdive.ipynb) |
| [3.2 Alerting](./3.2%20Alerting) | Alert-Based Monitoring | `los_alerts_deepdive_data.geojson`<br>`visualisation_deepdive_data.geojson`<br>`tomtom_alerts_deepdive_data.geojson`<br>`vaarwegen_alerts_deepdive_data.geojson` | [Open Starter](https://colab.research.google.com/github/AiMTT-project/use-case-1/blob/main/3.2%20Alerting/Assignment/alerts_deepdive.ipynb) |
| [3.3 Crowd forecasting](./3.3%20Crowd%20forecasting) | Crowd Flow Forecasting (Starter & Advanced) | `SAIL2025_LVMA_data_3min_20August-25August2025_flow.csv` | [Open Starter](https://colab.research.google.com/github/AiMTT-project/use-case-1/blob/main/3.3%20Crowd%20forecasting/Assignment/01_crowd_forecasting_starter_exercises.ipynb) |
| [3.4 Evaluation during the event](./3.4%20Evaluation%20during%20the%20event) | Operational Data Archiving | `LOS_archive_data.geojson` (from 2.2 LOS) | [Open Starter](https://colab.research.google.com/github/AiMTT-project/use-case-1/blob/main/3.4%20Evaluation%20during%20the%20event/Assignment/archiving_deepdive.ipynb) |

---

## Running in Google Colab & Dataset Access

When you launch any notebook using the **Open in Colab** badge, the notebook runs in a fresh cloud virtual machine. The datasets are configured for immediate accessibility through three flexible options:

### 1. Automatic In-Notebook Download (Default)
Each notebook contains built-in path resolution logic. If a dataset is not detected in your local environment, the notebook automatically downloads the file from the GitHub repository (`https://raw.githubusercontent.com/AiMTT-project/use-case-1/main/`) into the `sample_data/` directory.

### 2. Fast Download via Shell Command (Colab / Linux)
You can also download any required dataset directly in a Colab code cell using `wget` or `curl`:

```bash
# Create target directory
!mkdir -p sample_data

# Example: Download Chapter 2.2 Level of Service dataset
!wget -q https://raw.githubusercontent.com/AiMTT-project/use-case-1/main/2.2%20LOS/LOS_deepdive_data.geojson -O sample_data/LOS_deepdive_data.geojson

# Example: Download Chapter 3.3 Visitor Flow time series dataset
!wget -q https://raw.githubusercontent.com/AiMTT-project/use-case-1/main/3.3%20Crowd%20forecasting/SAIL2025_LVMA_data_3min_20August-25August2025_flow.csv -O sample_data/SAIL2025_LVMA_data_3min_20August-25August2025_flow.csv
```

### 3. Manual Upload
Download the data file from the corresponding folder on GitHub and drag it into the `sample_data` folder in the Google Colab file sidebar.

---

## Local Environment Setup

### Prerequisites
Python 3.10 or higher is recommended.

### Installation

Clone the repository:

```bash
git clone https://github.com/AiMTT-project/use-case-1.git
cd use-case-1
```

Install the required Python packages:

```bash
pip install pandas numpy matplotlib geopandas contextily lightgbm scikit-learn plotly pyarrow fastparquet imageio
```

---

## Contributing and Partners

This learning module was created as part of the AiMTT project by:
- **TU Delft** (Delft University of Technology)
- **Analyze**
- **uCrowds**
