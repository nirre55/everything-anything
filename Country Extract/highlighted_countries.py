import geopandas as gpd
import matplotlib.pyplot as plt
import os
import random

# Set the path to your Natural Earth shapefile
shapefile_path = "C:\\Users\\Oulmi\\Downloads\\ne_10m_admin_0_countries\\ne_10m_admin_0_countries.shp"  # Update this path to where your shapefile is stored

# Load the shapefile
world = gpd.read_file(shapefile_path)

# Ensure the data is in a projected coordinate system for better visualization (e.g., WGS84)
world = world.to_crs(epsg=4326)  # WGS84 (latitude/longitude)

# Define the countries you want to highlight (with random colors)
highlight_countries = [
    "United States of America",
    "Canada",
    "France",
]  # Adjust names to match your shapefile (e.g., "United States" might work instead of "United States of America")

# Create a directory to save the output files
output_dir = "highlighted_countries"
os.makedirs(output_dir, exist_ok=True)


# Function to generate a random color (RGB)
def random_color():
    return (
        random.random(),
        random.random(),
        random.random(),
    )  # Returns a tuple of (R, G, B) values between 0 and 1


# Generate a random color for each highlighted country (to ensure consistency for each country)
highlight_colors = {country: random_color() for country in highlight_countries}

# Create a figure for the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))

# Plot highlighted countries with random colors
highlighted = world[
    world["NAME"].isin(highlight_countries)
]  # Adjust 'NAME' to match your shapefile column for country names
for country_name in highlight_countries:
    country_data = highlighted[highlighted["NAME"] == country_name]
    country_data.plot(
        ax=ax, color=highlight_colors[country_name], edgecolor="black", linewidth=0.5
    )

# Plot other countries in gray
other_countries = world[~world["NAME"].isin(highlight_countries)]
other_countries.plot(ax=ax, color="lightgray", edgecolor="black", linewidth=0.5)

# Customize the map
plt.title("Highlighted Countries (Random Colors: USA, Canada, France; Gray: Others)")
plt.axis("off")

# Save the map as PNG
output_path = os.path.join(output_dir, "highlighted_random_color_world_map.png")
plt.savefig(output_path, dpi=300, bbox_inches="tight", pad_inches=0)
plt.close()

print(f"Saved highlighted world map with random colors as {output_path}")

# Optional: List the countries processed and their colors
print("\nHighlighted countries and their random colors:")
for country, color in highlight_colors.items():
    print(f"{country}: RGB({color[0]:.2f}, {color[1]:.2f}, {color[2]:.2f})")
print("\nOther countries are shown in gray.")
