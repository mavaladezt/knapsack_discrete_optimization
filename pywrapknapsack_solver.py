


import time
import numpy as np
from ortools.algorithms import pywrapknapsack_solver

#==DATA========================================

np.random.seed(1)
values = np.random.randint(1,500,500).tolist()
#values = [values]
weights = np.random.randint(1,1000,500).tolist()
weights = [weights]
capacity = np.sum(weights)*.95
capacity = [int(capacity)]

#==ALGORITHM===================================

solver = pywrapknapsack_solver.KnapsackSolver(
    pywrapknapsack_solver.KnapsackSolver.
    KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

#==SOLUTION===================================

start=time.time()

solver.Init(values, weights, capacity)
computed_value = solver.Solve()

packed_items = []
packed_weights = []
total_weight = 0
print('Total value =', computed_value)
for i in range(len(values)):
    if solver.BestSolutionContains(i):
        packed_items.append(i)
        packed_weights.append(weights[0][i])
        total_weight += weights[0][i]
print('Total weight:', total_weight)
print('Packed items:', packed_items)
print('Packed_weights:', packed_weights)
end=time.time()
print('Time total:',end-start)

#Time total: 0.002 seconds
#Solution: 124172
