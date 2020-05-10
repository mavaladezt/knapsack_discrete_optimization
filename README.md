# Knapsack Optimization

### Knapsack is a resource allocation problem very common in supply chain and production planning.

According to wikipedia: "Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. It derives its name from the problem faced by someone who is constrained by a fixed-size knapsack and must fill it with the most valuable items".<p>

For this knapsack optimization, I will be applying a dynamic programming algorithm programmed by myself and will compare it to Google's pywrapknapsack_solver which solves this kind of problems.<p>

Dynamic Algorithm:<br/>
  Time: 169.0 seconds<br/>
  Solution: 124172<p>

Google's pywrapknapsack_solver:<br/>
  Time: 0.002 seconds<br/>
  Solution: 124172<br/>
  
__Same optimal solution but Google's version is np.inf faster than mine.__

