import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data for water usage (in cubic meters per unit)
# Replace this with actual data
water_usage_data = {
    'Cotton': 10,     # Water usage per kg
    'Polyester': 5,   # Water usage per kg
    'Wheat': 1.2,     # Water usage per kg
    'Beef': 15.5,     # Water usage per kg
    # ... add more materials or products
}

# Convert to DataFrame for easier handling
water_usage_df = pd.DataFrame(list(water_usage_data.items()), columns=['Material', 'Water_Usage'])

# Function to calculate statistics
def calculate_statistics(df, column):
    stats = df[column].describe()
    return stats

# Calculate statistics for water usage
stats = calculate_statistics(water_usage_df, 'Water_Usage')

# Print statistics
print("Water Usage Statistics:")
print(stats)

# Visualizing the water usage of each material/product
plt.figure(figsize=(10, 6))
sns.barplot(x='Water_Usage', y='Material', data=water_usage_df, palette='cool')
plt.title('Water Usage Assessment per Material/Product')
plt.xlabel('Water Usage (cubic meters per kg)')
plt.ylabel('Material/Product')
plt.show()
