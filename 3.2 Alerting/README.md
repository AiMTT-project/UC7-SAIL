# Chapter 3.2: Alert-Based Monitoring Deep Dive

This module provides the practical deep-dive notebooks accompanying **Video 3.2: Alerting**, presented by **Kevin Otjes (Analyze)** as part of Chapter 3 (Live Event Operations).

---

## Interactive Notebooks

Open the notebooks directly in Google Colab:

- **Starter Exercises**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AiMTT-project/UC7-SAIL/blob/main/3.2%20Alerting/Assignment/alerts_deepdive.ipynb)
- **Reference Solutions**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AiMTT-project/UC7-SAIL/blob/main/3.2%20Alerting/Assignment-Solution/alerts_deepdive_answers.ipynb)

---

## Overview

Live control rooms receive massive streams of sensor readings during large-scale public events. Displaying every raw measurement on an operational dashboard quickly creates **information overload**, obscuring genuine safety hazards and leading to **alert fatigue**.

Effective alert design requires transforming noisy, instantaneous sensor spikes into dependable operational signals:
- Using **moving averages** and **rolling statistics** instead of single-point threshold evaluations.
- Requiring **temporal persistence** (for example, demanding that a critical Level of Service F state persists over consecutive evaluation windows before triggering an alarm).
- Fusing multiple operational data sources, including pedestrian sensors, road traffic congestion, and waterway vessel movements.

In this deep dive, you will examine real multimodal datasets from SAIL 2025, diagnose information overload, build noise-filtering alert algorithms, and visualize coordinated operational alerts across land and water.

---

## Learning Objectives

By completing this module, you will be able to:

1. **Diagnose Information Overload**: Evaluate how uncurated raw sensor feeds degrade situational awareness in high-tempo control environments.
2. **Fuse Multi-Source Signals**: Ingest and align three distinct operational data streams:
   - Pedestrian Level of Service sensor counts.
   - TomTom urban traffic flow and delay reports.
   - Waterway (vaarwegen) nautical vessel monitoring records.
3. **Build Noise-Resistant Alert Rules**:
   - Implement rolling window moving averages to smooth out temporary measurement anomalies.
   - Apply moving minimum persistence filters to ensure only sustained safety breaches trigger active notifications.
4. **Develop Spatial Alert Dashboards**: Render filtered alert icons and status boundaries onto synchronized map visualisations and animated MP4 video reports.

---

## Folder Contents

```
3.2 Alerting/
│
├── Assignment/
│   └── alerts_deepdive.ipynb               # Student exercise notebook with guided tasks
│
├── Assignment-Solution/
│   └── alerts_deepdive_answers.ipynb       # Complete reference solution notebook
│
├── alerts_deepdive_data.geojson            # Pedestrian Level of Service dataset
├── tomtom_alerts_deepdive_data.geojson      # Road traffic speed and congestion alert dataset
└── vaarwegen_alerts_deepdive_data.geojson   # Nautical waterway sensor and traffic dataset
```

GitHub Directory: [AiMTT-project/UC7-SAIL/tree/main/3.2%20Alerting](https://github.com/AiMTT-project/UC7-SAIL/tree/main/3.2%20Alerting)

---

## Dataset Access in Google Colab

The notebook automatically checks your local folders and downloads the required files from GitHub into `sample_data/` if needed.

You can also pre-fetch all multi-modal datasets using `wget` in a Colab code cell:

```bash
!mkdir -p sample_data

# Pedestrian Level of Service alerts dataset (from Chapter 2.2)
!wget -q https://raw.githubusercontent.com/AiMTT-project/UC7-SAIL/main/2.2%20LOS/los_alerts_deepdive_data.geojson -O sample_data/los_alerts_deepdive_data.geojson

# Crowdscan capacity dataset (from Chapter 2.3)
!wget -q https://raw.githubusercontent.com/AiMTT-project/UC7-SAIL/main/2.3%20Visualisatie/visualisation_deepdive_data.geojson -O sample_data/visualisation_deepdive_data.geojson

# TomTom traffic flow dataset
!wget -q https://raw.githubusercontent.com/AiMTT-project/UC7-SAIL/main/3.2%20Alerting/tomtom_alerts_deepdive_data.geojson -O sample_data/tomtom_alerts_deepdive_data.geojson

# Waterway vessel monitoring dataset
!wget -q https://raw.githubusercontent.com/AiMTT-project/UC7-SAIL/main/3.2%20Alerting/vaarwegen_alerts_deepdive_data.geojson -O sample_data/vaarwegen_alerts_deepdive_data.geojson
```

---

## Required Python Libraries

To run the notebooks locally or in Colab, install the following dependencies:

```bash
pip install geopandas pandas matplotlib contextily numpy imageio pyproj pillow
```
