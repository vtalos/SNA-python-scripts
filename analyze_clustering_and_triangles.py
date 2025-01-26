import pandas as pd
import matplotlib.pyplot as plt

# Read the nodes.csv file
file_path = "nodes.csv"
data = pd.read_csv(file_path)

# Calculate average clustering coefficient
average_clustering_coefficient = data['clustering'].mean()

# Calculate the total number of triangles
total_triangles = data['triangles'].sum()

# Create a histogram for the clustering coefficient distribution
plt.figure(figsize=(10, 6))
plt.hist(data['clustering'], bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel("Clustering Coefficient", fontsize=16)
plt.ylabel("Frequency", fontsize=16)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Check for the triadic closure phenomenon
triadic_closure_nodes = data[data['clustering'] > 0]  # Nodes with non-zero clustering
num_triadic_closure_nodes = len(triadic_closure_nodes)

# Summarize clustering effects
print("\nClustering Effects Summary:")
print(f"- Average Clustering Coefficient: {average_clustering_coefficient}")
print(f"- Total Number of Triangles: {total_triangles}")
print(f"- Number of Nodes Exhibiting Triadic Closure: {num_triadic_closure_nodes}")
print(f"- Percentage of nodes exhibiting triadic closure: {num_triadic_closure_nodes / len(data) * 100:.2f}%")