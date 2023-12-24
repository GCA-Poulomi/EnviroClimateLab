import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data structure for emission factors (in kg CO2e per unit)
# You would replace this with real data
emission_factors = {
    'Electricity': 0.5,  # kg CO2e per kWh
    'Gasoline': 2.3,     # kg CO2e per liter
    'Diesel': 2.7,       # kg CO2e per liter
    'NaturalGas': 2.0,   # kg CO2e per cubic meter
    'Steel': 1.8,        # kg CO2e per kg
    'Plastic': 1.5       # kg CO2e per kg
}

# Function to calculate carbon footprint
def calculate_carbon_footprint(data, emission_factors):
    total_footprint = 0
    details = {}

    for item in data:
        material, amount = item['material'], item['amount']
        footprint = amount * emission_factors.get(material, 0)
        total_footprint += footprint
        details[material] = details.get(material, 0) + footprint

    return total_footprint, details

# Sample usage data
usage_data = [
    {'material': 'Electricity', 'amount': 320},  # kWh
    {'material': 'Gasoline', 'amount': 50},     # liters
    {'material': 'Steel', 'amount': 20},        # kg
    {'material': 'Plastic', 'amount': 10}       # kg
]

# Calculate the carbon footprint
total_footprint, details = calculate_carbon_footprint(usage_data, emission_factors)

# Print total carbon footprint
print(f"Total Carbon Footprint: {total_footprint} kg CO2e")

# Visualizing the details
details_df = pd.DataFrame(list(details.items()), columns=['Material', 'Footprint'])
sns.barplot(x='Footprint', y='Material', data=details_df)
plt.title('Carbon Footprint by Material')
plt.xlabel('kg CO2e')
plt.ylabel('')
plt.show()
