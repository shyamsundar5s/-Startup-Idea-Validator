import matplotlib.pyplot as plt

def generate_trend_graph(trends, output_file):
    plt.figure(figsize=(10, 5))
    plt.plot(trends['dates'], trends['values'], marker='o')
    plt.title('Market Demand Trends')
    plt.xlabel('Date')
    plt.ylabel('Search Interest')
    plt.grid(True)
    plt.savefig(output_file)

# Example usage:
# trends = {'dates': ['2025-01', '2025-02', '2025-03'], 'values': [50, 75, 90]}
# generate_trend_graph(trends, 'trend_graph.png')
