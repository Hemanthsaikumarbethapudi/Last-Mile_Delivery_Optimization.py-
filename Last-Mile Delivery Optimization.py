import numpy as np
import networkx as nx
import heapq

# Constants
NUM_HUBS = 10
AVG_DEMAND = 500
DEMAND_STD_DEV = 50
MIN_DEMAND = 400
MAX_DEMAND = 600
SCOOTER_CAPACITY = 10
SCOOTERS_PER_HUB = 10
TRIPS_PER_SCOOTER = 5
DELIVERY_TIME_BASE = 20  # minutes per package
TRAFFIC_VARIABILITY = (0, 0.5)  # Uniform distribution
ON_TIME_GOAL = 0.90    
COST_PER_DELIVERY = 2.0  # Current cost
TARGET_COST = 1.6  # Desired cost

# Simulating daily demand at each hub
def generate_demand():
    demand = np.random.normal(AVG_DEMAND, DEMAND_STD_DEV, NUM_HUBS)
    return np.clip(demand, MIN_DEMAND, MAX_DEMAND).astype(int)

# Simulating traffic impact
def adjust_delivery_time():
    return DELIVERY_TIME_BASE * (1 + np.random.uniform(*TRAFFIC_VARIABILITY))

# Delivery Scheduling Optimization
def schedule_deliveries(demand):
    total_deliveries = sum(demand)
    total_scooters = NUM_HUBS * SCOOTERS_PER_HUB
    max_trips = total_scooters * TRIPS_PER_SCOOTER
    required_trips = np.ceil(total_deliveries / SCOOTER_CAPACITY)
    
    # Check feasibility
    if required_trips > max_trips:
        print("Warning: Insufficient capacity! Consider increasing fleet or optimizing routes.")
    
    return required_trips, total_deliveries / required_trips  # Trips required, avg deliveries per trip

# Route Optimization using Dijkstra
def shortest_path(graph, start, end):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances[end]

# Simulating a city road network (graph-based)
def create_city_graph():
    G = {
        'Hub1': {'Hub2': 5, 'Hub3': 10},
        'Hub2': {'Hub1': 5, 'Hub4': 7},
        'Hub3': {'Hub1': 10, 'Hub5': 8},
        'Hub4': {'Hub2': 7, 'Hub6': 6},
        'Hub5': {'Hub3': 8, 'Hub6': 9},
        'Hub6': {'Hub4': 6, 'Hub5': 9}
    }
    return G

# Calculate Cost Optimization
def calculate_cost_optimization(trips):
    new_cost = COST_PER_DELIVERY * (trips / (NUM_HUBS * SCOOTERS_PER_HUB * TRIPS_PER_SCOOTER))
    return new_cost

# Run Simulation
demand = generate_demand()
required_trips, avg_deliveries_per_trip = schedule_deliveries(demand)
city_graph = create_city_graph()
optimized_cost = calculate_cost_optimization(required_trips)

print(f"Total Demand: {sum(demand)} packages")
print(f"Required Trips: {required_trips}, Avg Deliveries per Trip: {avg_deliveries_per_trip:.2f}")
print(f"Optimized Cost per Delivery: ${optimized_cost:.2f} (Target: <=$1.60)")
print(f"Shortest Route from Hub1 to Hub6: {shortest_path(city_graph, 'Hub1', 'Hub6')} minutes")
