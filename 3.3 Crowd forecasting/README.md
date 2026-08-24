# Chapter 3.3: Crowd Flow Forecasting (Starter & Advanced)

This module provides the practical deep-dive notebooks accompanying **Videos 3.3.1, 3.3.2, and 3.3.3: Crowd Forecasting**, presented by **Theivaprakasham Hari (TU Delft)** as part of Chapter 3 (Live Event Operations).

---

## Overview

Real-time sensor monitoring shows what is happening right now, but proactive crowd management requires knowing what will happen in 30, 60, or 240 minutes. Forecasting provides crowd managers with the crucial **lead time** needed to execute preventative interventions (such as opening overflow routes, dispatching stewards, or adjusting public transit frequency) before severe overcrowding occurs.

This module contains two complete learning tracks based on high-resolution 3-minute visitor flow sensor data from SAIL Amsterdam 2025:

1. **Starter Track (`01_crowd_forecasting_starter`)**: Focuses on the core machine learning workflow, feature engineering, baseline models, LightGBM regression, quantile loss for uncertainty estimation, and multi-step forecasting up to 4 hours.
2. **Advanced Track (`02_crowd_forecasting_advanced`)**: Covers production architecture, automated multi-sensor model training, real-time online Kalman filter bias correction, probabilistic interval evaluation, weather sensitivity analysis, and interactive Plotly control room visualisations.

---

## Learning Objectives

### Starter Notebook (Foundations to Machine Learning)
1. **Explore Event Time Series**: Analyze 3-minute visitor flow data across sensor gates, identifying diurnal rhythms, event peak periods, and sudden crowd surges.
2. **Engineer Time Series Features**:
   - Construct short and long lag features (3 min, 6 min, 15 min, 30 min, 60 min).
   - Calculate rolling statistics (moving averages, rolling standard deviations, min/max bounds).
   - Encode calendar and cyclical temporal components (hour of day, day of week, sine/cosine encodings).
   - Integrate weather features (temperature, precipitation, wind speed).
3. **Benchmark Predictive Models**:
   - Implement naive persistence and seasonal naive baselines.
   - Train regularized Linear Regression models.
   - Train non-linear Gradient-Boosted Decision Trees using LightGBM.
4. **Quantify Uncertainty with Quantile Regression**:
   - Train dedicated models targeting the 10th percentile (P10), 50th percentile (P50 / Median), and 90th percentile (P90).
   - Evaluate probabilistic prediction intervals using Pinball Loss and the Winkler Score.
5. **Generate Multi-Step Forecasts**: Build direct multi-step forecasting models covering operational horizons from 15 minutes up to 4 hours.

### Advanced Notebook (Production Pipeline & Online Filtering)
1. **Build Modular Production Pipelines**: Implement reusable feature transformers and training harnesses across all network sensors.
2. **Automate Multi-Sensor Training**: Train and persist independent probabilistic models tailored to the distinct behavioural dynamics of each sensor location.
3. **Implement Online Kalman Filter Correction**:
   - Update forecast predictions dynamically using live streaming residuals.
   - Mitigate model drift caused by unexpected program changes or local crowd diversions.
4. **Conduct Probabilistic Evaluation**:
   - Benchmark point metrics (MAE, RMSE, MAPE) alongside interval metrics (empirical coverage percentage, mean prediction interval width).
5. **Analyze Weather Sensitivity**: Quantify the impact of rainfall and temperature anomalies on gate-level arrival volumes.
6. **Build Interactive Dashboards**: Create responsive Plotly visualizations showing live observations, median forecasts, and 80% confidence bands.

---

## Folder Contents

```
3.3 Crowd forecasting/
│
├── Assignment/
│   ├── 01_crowd_forecasting_starter_exercises.ipynb   # Starter exercises notebook
│   └── 02_crowd_forecasting_advanced_exercises.ipynb  # Advanced pipeline exercises notebook
│
├── Assignment-Solution/
│   ├── 01_crowd_forecasting_starter_solutions.ipynb   # Complete starter solutions notebook
│   └── 02_crowd_forecasting_advanced_solutions.ipynb  # Complete advanced pipeline solutions notebook
│
└── SAIL2025_LVMA_data_3min_20August-25August2025_flow.csv # High-resolution 3-minute sensor flow dataset
```

---

## Dataset Overview

The dataset `SAIL2025_LVMA_data_3min_20August-25August2025_flow.csv` contains continuous visitor flow counts collected between August 20 and August 25, 2025.

Key columns:
- `timestamp`: Date and time at 3-minute intervals.
- `sensor_id`: Unique identifier for each pedestrian tracking gate.
- `location_name`: Human-readable location description (for example, Piet Heinkade, Stationsplein, Java-eiland).
- `flow`: Total number of pedestrians passing through the gate during the 3-minute window.
- `temperature`, `precipitation`, `wind_speed`: Local meteorological observations.

---

## Required Python Libraries

To run the notebooks in this folder, install the following dependencies:

```bash
pip install pandas numpy matplotlib lightgbm scikit-learn plotly
```
