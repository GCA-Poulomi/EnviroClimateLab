import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for environmental indicators
# Replace this with actual data
eco_indicators = {
    'ProductA': {'GlobalWarming': 100, 'OzoneDepletion': 0.05, 'AirPollution': 40, 'WaterUsage': 300},
    'ProductB': {'GlobalWarming': 80, 'OzoneDepletion': 0.03, 'AirPollution': 30, 'WaterUsage': 250},
    'ProductC': {'GlobalWarming': 90, 'OzoneDepletion': 0.04, 'AirPollution': 35, 'WaterUsage': 280},
    # Add more products or categories
}

# Convert to DataFrame for easier handling
eco_df = pd.DataFrame(eco_indicators).T

# Visualizing the environmental indicators
plt.figure(figsize=(12, 6))
sns.heatmap(eco_df, annot=True, cmap='coolwarm')
plt.title('Environmental Indicators Assessment')
plt.ylabel('Product/Category')
plt.xlabel('Indicator')
plt.show()
