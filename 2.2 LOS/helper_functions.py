import pandas as pd
import numpy as np
import os
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import contextily as ctx
import geopandas as gpd


def in_range(
    value: float,
    min_val: float = None,
    max_val: float = None,
    include_min: bool = False,
    include_max: bool = True,
) -> bool:
    if pd.isna(value):
        return False

    lower_ok = (
        True
        if min_val is None
        else (value >= min_val if include_min else value > min_val)
    )
    upper_ok = (
        True
        if max_val is None
        else (value <= max_val if include_max else value < max_val)
    )

    return lower_ok and upper_ok


def classify_metric(value: float, thresholds: dict, metric: str) -> str:
    for los, bounds in thresholds.items():
        min_val = bounds[metric].get("min")
        max_val = bounds[metric].get("max")

        if in_range(value, min_val=min_val, max_val=max_val):
            return los

    return np.nan


def combine_los(los_density: str, los_flow: str) -> str:
    los_rank = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
    }

    if pd.isna(los_density) and pd.isna(los_flow):
        return np.nan
    if pd.isna(los_density):
        return los_flow
    if pd.isna(los_flow):
        return los_density

    if los_density in los_rank and los_flow in los_rank:
        return max([los_density, los_flow], key=lambda x: los_rank[x])

    if los_density in los_rank:
        return los_density
    if los_flow in los_rank:
        return los_flow

    return np.nan


def save_gdf_as_mp4(gdf: gpd.GeoDataFrame):

    # --- Settings ---
    los_order = ["LoS A", "LoS B", "LoS C", "LoS D", "LoS E", "LoS F"]

    los_colors = {
        "LoS A": "#002CCF",
        "LoS B": "#58AA2A",
        "LoS C": "#F8EC39",
        "LoS D": "#F1C73A",
        "LoS E": "#E56F2F",
        "LoS F": "#8A3817",
    }

    # --- Prepare data ---
    gdf_day = gdf.copy()
    gdf_day["time"] = pd.to_datetime(gdf_day["time"])
    gdf_day["time_10min"] = gdf_day["time"].dt.floor("10min")
    gdf_day["LoS"] = pd.Categorical(gdf_day["LoS"], categories=los_order, ordered=True)
    gdf_day["color"] = gdf_day["LoS"].map(los_colors)

    # Optional: keep only one day
    gdf_day = gdf_day[
        gdf_day["time"].dt.date == pd.Timestamp("2025-08-20").date()
    ].copy()

    # Reproject once
    gdf_day = gdf_day.to_crs(epsg=3857)

    # Fixed extent
    xmin, ymin, xmax, ymax = gdf_day.total_bounds

    # Ordered timestamps
    time_steps = sorted(gdf_day["time_10min"].dropna().unique())

    # Legend
    legend_patches = [
        mpatches.Patch(color=los_colors[los], label=los) for los in los_order
    ]

    # Output folder
    frame_dir = "los_frames"
    os.makedirs(frame_dir, exist_ok=True)

    frame_paths = []

    # --- Save each frame as PNG ---
    for i, current_time in enumerate(time_steps):
        gdf_step = gdf_day[gdf_day["time_10min"] == current_time].copy()

        fig, ax = plt.subplots(figsize=(10, 10))

        if not gdf_step.empty:
            gdf_step.plot(
                ax=ax,
                color=gdf_step["color"],
                alpha=0.7,
                edgecolor="black",
                linewidth=0.8,
            )

        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)

        # Add basemap after setting extent
        ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)

        ax.legend(handles=legend_patches, title="Level of Service", loc="upper right")
        ax.set_title(
            f"Level of Service at {pd.Timestamp(current_time).strftime('%Y-%m-%d %H:%M')}"
        )
        ax.set_axis_off()

        frame_path = os.path.join(frame_dir, f"frame_{i:03d}.png")
        plt.savefig(frame_path, dpi=150, bbox_inches="tight")
        plt.close(fig)

        frame_paths.append(frame_path)

    # --- Combine PNGs into MP4 ---
    with imageio.get_writer("los_animation.mp4", fps=2) as writer:
        for frame_path in frame_paths:
            writer.append_data(imageio.imread(frame_path))

    print("Saved: los_animation.mp4")
