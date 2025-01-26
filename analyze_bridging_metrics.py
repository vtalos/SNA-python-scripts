import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
nodes_df = pd.read_csv('nodes.csv')

# Summary statistics for bridging coefficient and centrality
print("\nSummary Statistics:")
print(nodes_df[['bridgingcoefficient', 'bridgingcentrality']].describe())

# Identify nodes with high bridging centrality and coefficient
high_bridging_centrality = nodes_df[nodes_df['bridgingcentrality'] > nodes_df['bridgingcentrality'].mean()]
high_bridging_coefficient = nodes_df[nodes_df['bridgingcoefficient'] > nodes_df['bridgingcoefficient'].mean()]

print(f"\nNumber of nodes with high bridging centrality: {len(high_bridging_centrality)}")
print(f"Number of nodes with high bridging coefficient: {len(high_bridging_coefficient)}")

# Visualize bridging centrality distribution
plt.figure(figsize=(10, 6))
plt.hist(nodes_df['bridgingcentrality'], bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.title("Distribution of Bridging Centrality", fontsize=16)
plt.xlabel("Bridging Centrality", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualize bridging coefficient distribution
plt.figure(figsize=(10, 6))
plt.hist(nodes_df['bridgingcoefficient'], bins=30, color='green', edgecolor='black', alpha=0.7)
plt.title("Distribution of Bridging Coefficient", fontsize=16)
plt.xlabel("Bridging Coefficient", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Highlight important nodes
top_bridging_nodes = nodes_df.sort_values(by='bridgingcentrality', ascending=False).head(10)
print("\nTop 10 Nodes by Bridging Centrality:")
print(top_bridging_nodes[['Label', 'bridgingcentrality', 'bridgingcoefficient']])