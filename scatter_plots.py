import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
file_path = 'nodes.csv'
data = pd.read_csv(file_path)

# List of centrality measures to plot
centrality_measures = [
    'Degree', 'indegree', 'outdegree', 
    'closnesscentrality', 'betweenesscentrality', 'eigencentrality',
    'pageranks', 'bridgingcoefficient', 'bridgingcentrality'
]

# List of labels for the measures
centrality_labels = [
    'Degree', 'In-degree', 'Out-degree', 
    'Closeness Centrality', 'Betweenness Centrality', 'Eigenvector Centrality',
    'PageRank', 'Bridging Coefficient', 'Bridging Centrality'
]

# Create scatter plots for each measure
for measure, label in zip(centrality_measures, centrality_labels):
    # Calculate the frequency of each unique value in the measure
    value_counts = data[measure].value_counts().sort_index()
    
    # Plot the scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(value_counts.index, value_counts.values, alpha=0.6, edgecolor='k')
    plt.xlabel(label, fontsize=14)
    plt.ylabel('Number of Nodes', fontsize=14)
    plt.grid(alpha=0.3)

    # Fix axes to display numbers in readable format
    plt.ticklabel_format(style='plain', axis='both')  # Disable scientific notation

    # Adjust layout and save/show the plot
    plt.tight_layout()
    plt.savefig(f'scatter_{measure}.png')  # Save each plot as an image
    plt.show()