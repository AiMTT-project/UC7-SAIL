# Chapter 2.3: Crowd Data Visualisation Deep Dive

This module provides the practical deep-dive notebook accompanying **Video 2.3: Visualisation**, presented by **Kevin Otjes (Analyze)** as part of Chapter 2 (Preparation Phase).

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

---

## Notebook Walkthrough

The notebook is divided into four practical assignments:

1. **Capacity Over Time**: Plot the percentage utilization across all monitored event zones in a unified time-series chart.
2. **Actionable Threshold Mapping**: Categorize area utilization into defined capacity bands (below 50%, 50% to 80%, above 80%) with intuitive alert colors.
3. **Map-Based Situation Picture**: Produce snapshot spatial visualisations of the Crowdscan dataset for critical moments during the event.
4. **Web GIS Styling Implementation**:
   - Write SLD styling rules using property filters and color fills.
   - Configure GeoStyler JSON definitions with custom classification rules.
   - Build Mapbox vector styling expressions for web deployment.

---

## Required Python Libraries

To run the notebooks in this folder, install the following dependencies:

```bash
pip install geopandas pandas matplotlib contextily numpy
```
