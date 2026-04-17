# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
        docid:
        name:
        description: >
        version: 0.0.0.0.0.0
        authority: filesystem
        security: seclvl2
        <(WT)>: -32
"""

# -*- coding: utf-8 -*
# ======================================Standard Library Modules======================================================||
from os.path import abspath, dirname, join
import datetime as dt

# ======================================3rd Party Library Modules=====================================================||

# ======================================Solutions Brewer Library Modules==============================================||
from kahndor import kahndor
from kahndor.logma import Logma

# ====================================================================================================================||
here = join(dirname(__file__), "")  # ||
log = True
logma = Logma(__name__)

# ====================================================================================================================||
pxcfg = join(here, "_data_", ".yaml")

import pandas as pd
import geopandas as gpd
import plotly.express as px
import requests
from io import StringIO
import warnings

warnings.filterwarnings("ignore")

# =====================================================
# Step 1: Download global mining operations dataset
# Source: S&P Global (formerly SNL) via public World Bank / USGS-derived dataset
# This is one of the most comprehensive open datasets of mines with coordinates
# =====================================================

print("Downloading global mineral mines dataset (~50k locations)...")

# Direct link to a cleaned, public version of the dataset (updated regularly)
url = "https://raw.githubusercontent.com/development-data-lab/mining-data/master/data/mines.csv"

# Alternative reliable source (USGS Mineral Resources Data System - MRDS)
# url = "https://mrdata.usgs.gov/mrds/mrds.csv"  # Very large, may be slow

try:
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    data = StringIO(response.text)
    df = pd.read_csv(data)
    print(f"✅ Successfully loaded {len(df):,} mining sites")
except Exception as e:
    print("❌ Failed to download from primary source. Trying backup...")
    # Backup: Smaller but reliable dataset from Our World in Data / USGS
    url_backup = "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Major%20mineral%20deposits%20of%20the%20world%20(USGS)/Major%20mineral%20deposits%20of%20the%20world%20(USGS)-data.csv"
    df = pd.read_csv(url_backup)
    df = df[df["year"] == 2005]  # Most complete year
    print(f"✅ Loaded backup dataset: {len(df):,} sites")

# =====================================================
# Step 2: Clean and filter the data
# =====================================================

print("Cleaning and filtering data...")

# Standardize column names (depends on source)
if "latitude" in df.columns and "longitude" in df.columns:
    lat_col, lon_col = "latitude", "longitude"
elif "Latitude" in df.columns and "Longitude" in df.columns:
    lat_col, lon_col = "Latitude", "Longitude"
    df.rename(columns={"Latitude": "latitude", "Longitude": "longitude"}, inplace=True)
elif "lat" in df.columns.str.lower().values:
    lat_col = [col for col in df.columns if "lat" in col.lower()][0]
    lon_col = [col for col in df.columns if "lon" in col.lower()][0]
    df.rename(columns={lat_col: "latitude", lon_col: "longitude"}, inplace=True)
else:
    print("Could not find latitude/longitude columns")
    print("Available columns:", list(df.columns))
    exit()

# Drop rows without coordinates
df = df.dropna(subset=["latitude", "longitude"])

# Filter reasonable coordinate ranges
df = df[(df["latitude"].between(-90, 90)) & (df["longitude"].between(-180, 180))]

# Try to find commodity / mineral type
commodity_col = None
possible_names = [
    "commodity",
    "Commodity",
    "primary_commodity",
    "mineral",
    "deposit_type",
    "metal",
    "name",
]
for name in possible_names:
    if any(name in col.lower() for col in df.columns):
        commodity_col = [col for col in df.columns if name in col.lower()][0]
        break

if commodity_col:
    df["commodity"] = df[commodity_col].astype(str)
else:
    df["commodity"] = "Unknown"

# Optional: Top commodities for better visualization
top_commodities = df["commodity"].value_counts().head(15).index
df["display_commodity"] = df["commodity"].where(
    df["commodity"].isin(top_commodities), "Other"
)

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs="EPSG:4326"
)

print(f"Final dataset: {len(gdf):,} mines with coordinates")

# =====================================================
# Step 3: Plot interactive world map
# =====================================================

print("Generating interactive map...")

fig = px.scatter_mapbox(
    gdf,
    lat="latitude",
    lon="longitude",
    color="display_commodity" if "display_commodity" in gdf.columns else "commodity",
    hover_name=commodity_col if commodity_col else "commodity",
    hover_data={
        "latitude": False,
        "longitude": False,
        "commodity": True,
    },
    zoom=1,
    height=800,
    title="🌍 Global Mineral Mining Operations (Active & Known Deposits)",
    color_discrete_sequence=px.colors.qualitative.Bold,
    category_orders=(
        {"display_commodity": sorted(gdf["display_commodity"].unique())}
        if "display_commodity" in gdf.columns
        else None
    ),
)

fig.update_layout(
    mapbox_style="open-street-map",  # Free, no token needed
    legend_title_text="Primary Commodity",
    margin={"r": 0, "t": 50, "l": 0, "b": 0},
)

fig.update_traces(marker=dict(size=6, opacity=0.7))

# Show and save
fig.show()

# Save as HTML file
fig.write_html("world_mining_operations_map.html")
print("✅ Map saved as 'world_mining_operations_map.html'")

# Optional: Save cleaned dataset
gdf[["latitude", "longitude", "commodity", "geometry"]].to_file(
    "mining_sites.geojson", driver="GeoJSON"
)
print("✅ Cleaned data saved as 'mining_sites.geojson'")

# ====================================================================================================================||

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
