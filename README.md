# Last-Mile_Delivery_Optimization.py-
This project implements an AI-powered last-mile delivery optimization system using Python. It leverages graph-based route optimization, demand prediction, and cost analysis to improve delivery efficiency in urban areas.
## Key Features
1. Demand Forecasting: Uses a normal distribution to simulate daily delivery demand at multiple hubs.

2. Route Optimization: Implements Dijkstra’s algorithm to determine the shortest delivery paths.

3. Fleet Utilization Analysis: Evaluates delivery schedules based on available scooters and trip capacity.

4. Traffic Impact Simulation: Models delivery time fluctuations due to variable traffic conditions.

5. Cost Optimization: Estimates cost per delivery and compares it against a predefined target.

## Technologies Used
1.Python

2. NumPy – For demand generation and statistical modeling

3. NetworkX – For graph-based routing and shortest path calculations

4. Heapq (Priority Queue) – For efficient pathfinding using Dijkstra’s algorithm

## How It Works
1. Simulate Demand: Randomly generates delivery demand at hubs based on historical data.

2. Optimize Routing: Uses Dijkstra’s algorithm to compute the most efficient delivery paths.

3. Schedule Deliveries: Calculates the required number of trips and fleet utilization.

4. Analyze Traffic Impact: Adjusts delivery time dynamically based on traffic conditions.

5. Evaluate Cost Efficiency: Estimates cost per delivery and assesses feasibility.

## Future Enhancements
1. Implement real-time traffic data integration.

2. Expand the model to include different vehicle types (e.g., drones, electric bikes).

3. Use machine learning for demand prediction based on historical patterns.
