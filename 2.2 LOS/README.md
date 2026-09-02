# Chapter 2.2: Level of Service (LOS) Deep Dive

This module provides the practical deep-dive notebooks accompanying **Video 2.2: Level-of-Service concept**, presented by **Winnie Daamen (TU Delft)** as part of Chapter 2 (Preparation Phase).

---

## Interactive Notebooks

Open the notebooks directly in Google Colab:

- **Starter Exercises**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AiMTT-project/use-case-1/blob/main/2.2%20LOS/Assignment/los.ipynb)
- **Reference Solutions**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AiMTT-project/use-case-1/blob/main/2.2%20LOS/Assignment-Solution/los_answers.ipynb)

---

## Overview

Level of Service (LOS) is a foundational framework used in crowd management and pedestrian engineering to describe the operational quality of pedestrian infrastructure. It categorizes crowd states on a scale from **LoS A (free flow)** to **LoS F (congested or breakdown conditions)** based on key variables such as density, flow rate, and walking speed.

The classical reference standard developed by John J. Fruin (1971) is based on unidirectional movement along corridors and walkways. During large-scale public events like SAIL Amsterdam 2025, pedestrian movement is predominantly bidirectional or multidirectional. Counter-flows introduce friction, lane formation, and speed reductions.

In this deep dive, you will explore real pedestrian sensor counts collected around Amsterdam Central Station during the SAIL IN event on August 20, 2025. You will calculate fundamental crowd metrics, apply unidirectional standards, design realistic bidirectional thresholds, and create animated spatial visualisations.

---

## Learning Objectives

By completing this module, you will be able to:

1. **Calculate Density and Flow**: Compute density (people per square meter) and flow (people per meter width per minute) from raw area counts and line-crossing counts.
2. **Apply Fruin Unidirectional Standards**: Classify crowd states using classical pedestrian LOS ranges.
3. **Design Bidirectional LOS Frameworks**: Establish tailored density and flow thresholds that account for opposing pedestrian streams and reduced capacity.
4. **Implement Area-Specific Profiles**: Customize LOS thresholds for distinct spatial categories, such as bridges, bottlenecks, and open station plazas.
5. **Generate Animated Geo-Visualisations**: Export time-stamped map animations (MP4) to inspect crowd dynamics over the course of an event day.

---

## Folder Contents

```
2.2 LOS/
│
├── Assignment/
│   └── los.ipynb                 # Student exercise notebook with guided tasks
│
├── Assignment-Solution/
│   └── los_answers.ipynb         # Complete reference solutions with plots
│
├── LOS_deepdive_data.geojson     # Pedestrian counts and spatial geometries for SAIL IN (August 20, 2025)
├── los_alerts_deepdive_data.geojson # Annotated Level of Service alert geometry dataset
└── LOS_archive_data.geojson      # Multi-location time-series dataset for archival analysis
```

GitHub Directory: [AiMTT-project/use-case-1/tree/main/2.2%20LOS](https://github.com/AiMTT-project/use-case-1/tree/main/2.2%20LOS)

---

## Dataset Access in Google Colab

When running the notebook in Google Colab, you can obtain the datasets using any of the following methods:

### Option 1: Automatic Download (Default)
The notebook includes an automated loader that retrieves `LOS_deepdive_data.geojson` directly from GitHub into the `sample_data/` folder if it is not present locally.

### Option 2: Download via wget in Colab
Execute the following shell commands in a Colab code cell:

```bash
!mkdir -p sample_data
!wget -q https://raw.githubusercontent.com/AiMTT-project/use-case-1/main/2.2%20LOS/LOS_deepdive_data.geojson -O sample_data/LOS_deepdive_data.geojson
```

### Option 3: Manual Upload
1. Download `LOS_deepdive_data.geojson` from the [2.2 LOS GitHub folder](https://github.com/AiMTT-project/use-case-1/tree/main/2.2%20LOS).
2. Drag and drop the file into the `sample_data` folder in the Colab file browser sidebar.

---

## Required Python Libraries

To run the notebooks locally or in Colab, install the following dependencies:

```bash
pip install geopandas pandas matplotlib contextily numpy imageio
```
