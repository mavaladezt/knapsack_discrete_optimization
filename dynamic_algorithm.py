

def knapsack(capacity, values, weights):
    '''
    Function uses dynamic programming to solve knapsack problem. Iterates for each integer value from 1 to capacity.
    Problem gets exponentially more complicated with the amount of options/variables (len(values))
    Input:
        capacity: capacity of knapsack (integer)
        values: values of each option to be considered for knapsack (list same size as weights)
        weights: weights of each item (list same size as values)
    Output:
        total: total value of optimal knapsack
        output_data: list with 1 or 0. 1 if item is selected, 0 if its not. Same order as values/weights
    '''

    n = len(values)
    W=capacity

    import time 
    start=time.time()

    bag = [0]*(W+1)
    for i in range(W+1): 
        bag[i]=[0]*(n+1)

    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                bag[w][i] = 0
            elif weights[i-1] <= w:
                bag[w][i] = max(values[i-1] + bag[w-weights[i-1]][i-1],  bag[w][i-1])
            else:
                bag[w][i] = bag[w][i-1]

    total = bag[len(bag)-1][len(bag[0])-1]

    last_row=len(bag)
    last_col=len(bag[0])
    result=[0]*(last_col-1)

    col=last_col-1
    row=last_row-1

    while col>=1:
        if bag[row][col]!=bag[row][col-1]:
            result[col-1]=1
            row-=weights[col-1]
        col-=1

    output_data=str(total) + ' ' + str(0) + '\n'
    print('Total value: ',total)
    print(result)

    end=time.time()
    print('Time total:',end-start)
    return total, output_data

#=========================================================================

import numpy as np

values = list(np.random.rand(300))
weights = list(np.random.randint(0,1000,300))
capacity = int(np.sum(weights)*.8)

knapsack(capacity,values,weights)


