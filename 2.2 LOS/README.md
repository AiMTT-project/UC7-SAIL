# Chapter 2.2: Level of Service (LOS) Deep Dive

This module provides the practical deep-dive notebook accompanying **Video 2.2: Level-of-Service concept**, presented by **Winnie Daamen (TU Delft)** as part of Chapter 2 (Preparation Phase).

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

---

## Notebook Walkthrough

The notebook is divided into five guided sections:

1. **Data Exploration**: Load the GeoJSON dataset, inspect timestamp granularity (1.5 to 2 minute intervals), and plot sensor locations over OpenStreetMap basemaps.
2. **Density and Flow Calculation**: Complete the metric calculation formulas for area density and line flow.
3. **Unidirectional LOS Classification**: Filter the data during the peak SAIL IN arrival period (13:30 to 14:00) and classify crowd conditions using Fruin thresholds.
4. **Bidirectional LOS Matrix**: Construct a custom classification matrix combining density and flow ratings for bidirectional areas.
5. **Spatial Animation**: Render time-stepped maps and combine them into an animated MP4 file using `contextily` and `imageio`.

---

## Required Python Libraries

To run the notebooks in this folder, install the following dependencies:

```bash
pip install geopandas pandas matplotlib contextily numpy imageio
```
