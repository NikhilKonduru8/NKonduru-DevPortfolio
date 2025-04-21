
# Scatterplot of Greenhouse Gas Emissions in the United States from 1990 - 2012


import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Greenhouse Gas Emissions worldwide.csv'
df = pd.read_csv(file_path, header=None, names=['Country', 'Year', 'Emissions', 'Unknown1', 'Unknown2', 'Unknown3', 'Unknown4', 'Unknown5'])

us_data = df[df['Country'] == 'United States of America']

us_data['Year'] = pd.to_datetime(us_data['Year'], format='%Y')
us_data['Emissions'] = us_data['Emissions'].astype(float)

us_data = us_data.sort_values('Year')

plt.figure(figsize=(12, 6))
plt.plot(us_data['Year'], us_data['Emissions'], marker='o')

plt.title('Greenhouse Gas Emissions in the United States (1990-2012)')
plt.xlabel('Year')
plt.ylabel('Emissions (kt)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.tight_layout()
plt.show()
