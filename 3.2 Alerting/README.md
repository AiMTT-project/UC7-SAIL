# Chapter 3.2: Alert-Based Monitoring Deep Dive

This module provides the practical deep-dive notebook accompanying **Video 3.2: Alerting**, presented by **Kevin Otjes (Analyze)** as part of Chapter 3 (Live Event Operations).

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

---

## Notebook Walkthrough

The notebook covers three progressive exercises:

1. **Unfiltered Data Ingestion and Overload Analysis**: Load pedestrian, road traffic, and waterway feeds simultaneously, inspecting the resulting visual chaos when all raw signals are plotted together.
2. **Targeted State Filtering**: Isolate a specific operational moment (such as August 21 at 18:34) and filter the pedestrian dataset to display distinct visual alert markers only when conditions reach critical LoS F.
3. **Moving Window Alert Logic**:
   - Implement a moving average filter over a 30-minute evaluation window (18:15 to 18:45) to detect sustained high-density trends.
   - Implement a moving minimum filter requiring all timestamps within a moving window to remain at LoS F before firing an escalation alert.
   - Export the resulting alert sequence to an animated MP4 file.

---

## Required Python Libraries

To run the notebooks in this folder, install the following dependencies:

```bash
pip install geopandas pandas matplotlib contextily numpy imageio
```
