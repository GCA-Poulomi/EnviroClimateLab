import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for lifecycle costs (in USD)
# Replace this with actual data
lifecycle_costs = {
    'Production': 5000,      # Cost of production
    'Operation': 2000,       # Annual operation cost
    'Maintenance': 300,      # Annual maintenance cost
    'Disposal': 100,         # Cost of disposal
    'LifeSpan': 10           # Lifespan in years
}

# Function to calculate total lifecycle cost
def calculate_total_lifecycle_cost(costs):
    total_cost = costs['Production'] + (costs['Operation'] + costs['Maintenance']) * costs['LifeSpan'] + costs['Disposal']
    return total_cost

# Calculate total lifecycle cost
total_cost = calculate_total_lifecycle_cost(lifecycle_costs)

# Print total lifecycle cost
print(f"Total Lifecycle Cost: ${total_cost} USD")

# Prepare data for visualization
costs_for_visualization = {k: v for k, v in lifecycle_costs.items() if k != 'LifeSpan'}
costs_for_visualization['Total'] = total_cost

# Convert to DataFrame for easier handling
costs_df = pd.DataFrame(list(costs_for_visualization.items()), columns=['Cost Type', 'Amount'])

# Visualizing the lifecycle costs
plt.figure(figsize=(10, 6))
sns.barplot(x='Amount', y='Cost Type', data=costs_df, palette='autumn')
plt.title('Breakdown of Lifecycle Costs')
plt.xlabel('Cost (USD)')
plt.ylabel('Cost Type')
plt.show()
