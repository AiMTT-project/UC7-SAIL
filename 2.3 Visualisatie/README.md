# Chapter 2.3: Crowd Data Visualisation Deep Dive

This module provides the practical deep-dive notebooks accompanying **Video 2.3: Visualisation**, presented by **Kevin Otjes (Analyze)** as part of Chapter 2 (Preparation Phase).

---

## Interactive Notebooks

Open the notebooks directly in Google Colab:

- **Starter Exercises**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AiMTT-project/UC7-SAIL/blob/main/2.3%20Visualisatie/Assignment/visualisation_deepdive.ipynb)
- **Reference Solutions**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AiMTT-project/UC7-SAIL/blob/main/2.3%20Visualisatie/Assignment-Solution/visualisation_deepdive_answers.ipynb)

---

## Overview

During major public events, crowd managers must interpret hundreds of data streams rapidly under high pressure. The design of a data visualisation directly determines how quickly and accurately operators perceive risks and take action.

A good visualisation system establishes visual consistency across all dashboards:
- Consistent color palettes and threshold definitions (green for normal, yellow for elevated, red for critical).
- Clear distinctions between real-time monitoring, simulations, and forecasts.
- Standardized styling layers compatible with web GIS viewers and control-room dashboards.

In this deep dive, you will work with crowd sensor data from SAIL 2025 to create clear capacity charts, develop map-based status layers, and write web GIS styling rules across three major industry standards: SLD, GeoStyler, and Mapbox Style Specification.

---

## Learning Objectives

By completing this module, you will be able to:

1. **Design Actionable Visualisations**: Create clear time-series charts illustrating area capacity and visitor load over the course of an event day.
2. **Apply Consistent Thresholds**: Map quantitative metrics to intuitive visual categories that immediately communicate status without clutter.
3. **Render Spatial Data**: Plot polygon areas, sensor counts, and capacity percentages on OpenStreetMap basemaps.
4. **Implement Web GIS Styling Standards**: Translate visualisation rules into industry-standard styling formats:
   - **SLD (Styled Layer Descriptor)**: XML-based standard used by OGC-compliant servers like GeoServer.
   - **GeoStyler**: A modern, vendor-agnostic JavaScript styling specification.
   - **Mapbox Style Specification**: JSON-based styling widely used in modern interactive map dashboards.

---

## Folder Contents

```
2.3 Visualisatie/
│
├── Assignment/
│   └── visualisation_deepdive.ipynb        # Student exercise notebook with styling tasks
│
├── Assignment-Solution/
│   └── visualisation_deepdive_answers.ipynb# Complete reference solution notebook
│
└── visualisation_deepdive_data.geojson     # Spatial crowd density and capacity tracking dataset
```

GitHub Directory: [AiMTT-project/UC7-SAIL/tree/main/2.3%20Visualisatie](https://github.com/AiMTT-project/UC7-SAIL/tree/main/2.3%20Visualisatie)

---

## Dataset Access in Google Colab

When running the notebook in Google Colab, you can obtain the dataset using any of the following methods:

### Option 1: Automatic Download (Default)
The notebook includes an automated loader that downloads `visualisation_deepdive_data.geojson` directly from GitHub into the `sample_data/` folder if it is not found locally.

### Option 2: Download via wget in Colab
Run the following shell commands in a Colab cell:

```bash
!mkdir -p sample_data
!wget -q https://raw.githubusercontent.com/AiMTT-project/UC7-SAIL/main/2.3%20Visualisatie/visualisation_deepdive_data.geojson -O sample_data/visualisation_deepdive_data.geojson
```

### Option 3: Manual Upload
1. Download `visualisation_deepdive_data.geojson` from the [2.3 Visualisatie GitHub folder](https://github.com/AiMTT-project/UC7-SAIL/tree/main/2.3%20Visualisatie).
2. Upload the file into the `sample_data` folder in the Colab file browser.

---

## Required Python Libraries

To run the notebooks locally or in Colab, install the following dependencies:

```bash
pip install geopandas pandas matplotlib contextily numpy
```
