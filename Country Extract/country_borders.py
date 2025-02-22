import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import os

# Set the path to your Natural Earth shapefile
shapefile_path = "C:\\Users\\Oulmi\\Downloads\\ne_10m_admin_0_countries\\ne_10m_admin_0_countries.shp"  # Update this path to where your shapefile is stored

# Load the shapefile
world = gpd.read_file(shapefile_path)

# Ensure the data is in a projected coordinate system for better visualization (e.g., WGS84)
world = world.to_crs(epsg=4326)  # WGS84 (latitude/longitude)

# Create a directory to save the output files
output_dir = "country_borders"
os.makedirs(output_dir, exist_ok=True)

# Extract and save borders for each country
for index, country in world.iterrows():
    country_name = country[
        "NAME"
    ]  # Adjust 'NAME' to match the column name in your shapefile for country names
    geometry = country["geometry"]

    # Create a GeoDataFrame for the single country
    country_gdf = gpd.GeoDataFrame([country], geometry="geometry")

    # Save as SVG (vector format)
    svg_path = os.path.join(output_dir, f"{country_name}_borders.svg")
    country_gdf.boundary.plot(figsize=(5, 5), edgecolor="black", facecolor="none")
    plt.title(country_name)
    plt.axis("off")
    plt.savefig(svg_path, format="svg", bbox_inches="tight", pad_inches=0)
    plt.close()

    print(f"Saved borders for {country_name} as {svg_path}")

# Optional: Create and save a single world map with all country borders color-coded
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.plot(ax=ax, edgecolor="black", facecolor="none", linewidth=0.5)
plt.title("World Country Borders")
plt.axis("off")

# Save the world map as PNG
world_map_path = os.path.join(output_dir, "world_borders.png")
plt.savefig(world_map_path, dpi=300, bbox_inches="tight", pad_inches=0)
plt.close()

print(f"Saved world map with all borders as {world_map_path}")

# Optional: Print a list of all countries processed
print("\nCountries processed:")
for country_name in world["NAME"].unique():
    print(country_name)
