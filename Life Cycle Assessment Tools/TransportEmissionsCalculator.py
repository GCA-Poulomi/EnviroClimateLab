import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for emission factors (in kg CO2e per km)
# Replace this with actual data
emission_factors = {
    'Car': 0.12,      # Gasoline car
    'Truck': 0.6,     # Diesel truck
    'Train': 0.03,    # Electric train
    'Airplane': 0.25, # Average airplane
}

# Function to calculate transport emissions
def calculate_transport_emissions(distance, mode, emission_factors):
    emissions = distance * emission_factors.get(mode, 0)
    return emissions

# Sample transport data (Replace with actual data)
transports = [
    {'mode': 'Car', 'distance': 100},  # km
    {'mode': 'Truck', 'distance': 300},
    {'mode': 'Train', 'distance': 400},
    {'mode': 'Airplane', 'distance': 1000},
]

# Calculating emissions for each transport
results = []
for transport in transports:
    emissions = calculate_transport_emissions(transport['distance'], transport['mode'], emission_factors)
    results.append({'Mode': transport['mode'], 'Distance': transport['distance'], 'Emissions': emissions})

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Visualizing the emissions of each transport mode
plt.figure(figsize=(10, 6))
sns.barplot(x='Emissions', y='Mode', data=results_df, palette='Set2')
plt.title('Transport Emissions by Mode')
plt.xlabel('Emissions (kg CO2e)')
plt.ylabel('Mode of Transportation')
plt.show()
