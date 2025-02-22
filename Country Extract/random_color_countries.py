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

# Create a directory to save the output files
output_dir = "random_color_countries"
os.makedirs(output_dir, exist_ok=True)


# Function to generate a random color (RGB)
def random_color():
    return (
        random.random(),
        random.random(),
        random.random(),
    )  # Returns a tuple of (R, G, B) values between 0 and 1


# Create a dictionary to store colors for each country (to ensure consistency if needed)
country_colors = {}

# Assign a random color to each country
for index, country in world.iterrows():
    country_name = country[
        "NAME"
    ]  # Adjust 'NAME' to match your shapefile column for country names
    if country_name not in country_colors:
        country_colors[country_name] = random_color()

# Create a figure for the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))

# Plot each country with its random color
for country_name, color in country_colors.items():
    country_data = world[world["NAME"] == country_name]
    country_data.plot(ax=ax, color=color, edgecolor="black", linewidth=0.5)

# Customize the map
plt.title("World Map with Random Colors for Each Country")
plt.axis("off")

# Save the map as PNG
output_path = os.path.join(output_dir, "random_color_world_map.png")
plt.savefig(output_path, dpi=300, bbox_inches="tight", pad_inches=0)
plt.close()

print(f"Saved world map with random colors as {output_path}")

# Optional: Print the colors assigned to each country
print("\nColors assigned to countries:")
for country_name, color in country_colors.items():
    print(f"{country_name}: RGB({color[0]:.2f}, {color[1]:.2f}, {color[2]:.2f})")
