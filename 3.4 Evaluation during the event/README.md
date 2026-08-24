# Chapter 3.4: Evaluation and Operational Data Archiving Deep Dive

This module provides the practical deep-dive notebook accompanying **Video 3.4: Evaluation during the event**, presented by **Kevin Otjes (Analyze)** as part of Chapter 3 (Live Event Operations).

---

## Overview

Real-time situational dashboards and predictive models are vital during live operations, but the data flowing through these systems is equally valuable for:
- Mid-event management reporting and daily shift briefings.
- Post-incident forensic evaluations and debriefings with municipal authorities.
- Training machine learning models and calibrating simulation parameters for future editions.

Streaming IoT feeds, pedestrian sensor logs, and municipal data services generate millions of individual JSON or GeoJSON records. Storing raw message streams directly into traditional text files causes massive disk consumption and slow query performance.

In this deep dive, you will simulate a live event datastream based on SAIL 2025 sensor records. You will build an efficient archival pipeline using compressed columnar **Parquet** storage and implement **hierarchical time-based partitioning** (by date and hour) to enable rapid analytics.

---

## Learning Objectives

By completing this module, you will be able to:

1. **Simulate Streaming Data Ingestion**: Emulate message-by-message data arrival from sensor networks in a Python environment.
2. **Implement Columnar Storage with Parquet**:
   - Convert row-oriented spatial records into columnar Parquet files.
   - Apply Snappy compression to drastically reduce disk storage footprints while preserving schema types and coordinate references.
3. **Design Time-Based Partitioning Schemes**:
   - Structure archive directories by date and hour (for example, `year=2025/month=08/day=20/hour=15/`).
   - Understand how partition pruning accelerates analytical queries by reading only relevant time slices.
4. **Inspect and Verify Archives**: Validate archive directory structures, file counts, and read performance compared to flat GeoJSON and CSV formats.

---

## Folder Contents

```
3.4 Evaluation during the event/
│
├── Assignment/
│   └── archiving_deepdive.ipynb            # Student exercise notebook with archiving tasks
│
└── Assignment-Solution/
    └── archiving_deepdive_answers.ipynb    # Complete reference solution notebook
```

---

## Dataset Reference

This module utilizes the `LOS_archive_data.geojson` dataset located in the [`2.2 LOS`](../2.2%20LOS) directory of this repository.

The dataset contains pedestrian sensor counts, line crossings, area densities, and spatial polygon geometries across key Amsterdam locations during SAIL 2025.

---

## Notebook Walkthrough

The notebook covers two practical assignments:

1. **Streaming Ingestion and Parquet Compression**:
   - Stream individual sensor records into a simulated buffer.
   - Write out batches as Snappy-compressed Parquet files.
   - Compare file sizes between raw GeoJSON records and compressed Parquet output.
2. **Hourly Partitioned Archival**:
   - Parse ISO timestamp strings into temporal components (year, month, day, hour).
   - Write streaming batches into structured subdirectory trees.
   - Inspect the generated archive tree structure and query specific hourly subsets efficiently.

---

## Required Python Libraries

To run the notebooks in this folder, install the following dependencies:

```bash
pip install geopandas pandas pyarrow fastparquet
```
