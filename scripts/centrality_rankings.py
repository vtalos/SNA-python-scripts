import pandas as pd

# Load data
nodes_file = "data/nodes.csv"
edges_file = "data/edges.csv"

nodes_df = pd.read_csv(nodes_file)
edges_df = pd.read_csv(edges_file)

# Helper function to get top nodes by a metric
def get_top_nodes(df, column, top_n=30):
    return df.nlargest(top_n, column)[["Label", column]]

# Get top nodes for each metric
top_degree = get_top_nodes(nodes_df, "Degree")
top_indegree = get_top_nodes(nodes_df, "indegree")
top_outdegree = get_top_nodes(nodes_df, "outdegree")
top_betweenness = get_top_nodes(nodes_df, "betweenesscentrality")
top_closeness = get_top_nodes(nodes_df, "closnesscentrality")
top_eigenvector = get_top_nodes(nodes_df, "eigencentrality")
top_pagerank = get_top_nodes(nodes_df, "pageranks")

# Print results
print("Top Nodes by Degree Centrality:")
print(top_degree)
print("\nTop Nodes by In-Degree Centrality:")
print(top_indegree)
print("\nTop Nodes by Out-Degree Centrality:")
print(top_outdegree)
print("\nTop Nodes by Betweenness Centrality:")
print(top_betweenness)
print("\nTop Nodes by Closeness Centrality:")
print(top_closeness)
print("\nTop Nodes by Eigenvector Centrality:")
print(top_eigenvector)
print("\nTop Nodes by PageRank:")
print(top_pagerank)