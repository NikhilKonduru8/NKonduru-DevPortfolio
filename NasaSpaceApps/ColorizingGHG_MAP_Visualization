# COLORIZING THE MAP: NIKHIL KONDURU

# Colorizing Greenhouse Gas Emissions for Nasa Space Apps Hackathon Map Visualization

import rasterio
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

tiff = '/content/MiCASA_v1_ATMC_x3600_y1800_daily_20010101.tif'


with rasterio.open(tiff) as src:
    emissions_data = src.read(1)

colors = ['white','green','green','green','green','green','green','green','green','green','green',
          'yellow','yellow','yellow','yellow','yellow','yellow','yellow',
          'orange','orange','orange','orange','orange','orange','orange','orange','orange','orange','orange','orange',
          'orange','orange',
           'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']

my_cmap = LinearSegmentedColormap.from_list('my_colormap', colors)

plt.figure(figsize=(10, 10))
plt.imshow(emissions_data, cmap=my_cmap)  # Use the custom colormap
plt.title('GHG Emissions Visualization')
plt.axis('off')  # Hide the axis
plt.colorbar(label='GHG Emissions: CO2')  # Optional: Add a colorbar for reference
plt.show()
