# Chapter 3.4: Evaluation and Operational Data Archiving Deep Dive

This module provides the practical deep-dive notebooks accompanying **Video 3.4: Evaluation during the event**, presented by **Kevin Otjes (Analyze)** as part of Chapter 3 (Live Event Operations).

---

## Interactive Notebooks

Open the notebooks directly in Google Colab:

- **Starter Exercises**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AiMTT-project/UC7-SAIL/blob/main/3.4%20Evaluation%20during%20the%20event/Assignment/archiving_deepdive.ipynb)
- **Reference Solutions**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AiMTT-project/UC7-SAIL/blob/main/3.4%20Evaluation%20during%20the%20event/Assignment-Solution/archiving_deepdive_answers.ipynb)

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

GitHub Directory: [AiMTT-project/UC7-SAIL/tree/main/3.4%20Evaluation%20during%20the%20event](https://github.com/AiMTT-project/UC7-SAIL/tree/main/3.4%20Evaluation%20during%20the%20event)

---

## Dataset Reference and Colab Access

This module uses `LOS_archive_data.geojson`, which is stored in the [`2.2 LOS`](https://github.com/AiMTT-project/UC7-SAIL/tree/main/2.2%20LOS) folder of this repository.

The dataset contains pedestrian sensor counts, line crossings, area densities, and spatial polygon geometries across key Amsterdam locations during SAIL 2025.

### Automatic In-Notebook Download (Default)
When executed in Google Colab, the notebook automatically downloads `LOS_archive_data.geojson` from the GitHub repository into `sample_data/`.

### Download via wget in Colab
You can also download the dataset manually using `wget`:

```bash
!mkdir -p sample_data
!wget -q https://raw.githubusercontent.com/AiMTT-project/UC7-SAIL/main/2.2%20LOS/LOS_archive_data.geojson -O sample_data/LOS_archive_data.geojson
```

---

## Required Python Libraries

To run the notebooks locally or in Colab, install the following dependencies:

```bash
pip install geopandas pandas pyarrow fastparquet
```
