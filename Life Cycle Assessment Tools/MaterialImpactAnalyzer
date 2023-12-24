import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data structure for environmental impact factors of materials
# Replace this with your actual data
impact_data = {
    'Steel': {'GHG_Emissions': 1.8, 'Water_Usage': 3.0, 'Toxicity': 0.5},
    'Plastic': {'GHG_Emissions': 1.5, 'Water_Usage': 1.2, 'Toxicity': 0.7},
    'Aluminum': {'GHG_Emissions': 2.3, 'Water_Usage': 2.5, 'Toxicity': 0.4},
    # ... add more materials
}

# Convert to DataFrame
impact_df = pd.DataFrame(impact_data).T

# Function to calculate statistics
def calculate_statistics(df):
    stats = pd.DataFrame()
    stats['Mean'] = df.mean()
    stats['Median'] = df.median()
    stats['Standard Deviation'] = df.std()
    return stats

# Calculate statistics for each impact category
stats = calculate_statistics(impact_df)

# Print statistics
print(stats)

# Visualizing the impact of each material
plt.figure(figsize=(12, 6))
sns.heatmap(impact_df, annot=True, cmap='viridis')
plt.title('Environmental Impact of Materials')
plt.ylabel('Material')
plt.xlabel('Impact Category')
plt.show()
