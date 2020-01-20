from pulp import *
import pandas as pd


def energyOptimization(nuclear, solar, wind, hydroelectric, gas, biofuel, neighbour, dem):

    available = [nuclear, solar, wind, hydroelectric, gas, biofuel, neighbour]
    demand = dem

    emissions = [0,0,0,0,0,0,0]
    costs = [0,0,0,0,0,0,0]

    idx = [0, 1, 2, 3, 4, 5, 6]
    d = {'PowerType': pd.Series(['Nuclear', 'Solar', 'Wind', 'Hydroelectric', 'Gas', 'Biofuel', 'Neighbour'], index=idx),
        'SourceAvailable': pd.Series(available, index=idx),
        'Cost': pd.Series([0.068, 0.481, 0.133, 0.057, 0.140, 0.131, 0.160], index=idx),
        'Emissions': pd.Series([0.006, 0.105, 0.013, 0.004, 0.909, 0.058, 0.258], index=idx)}
    df = pd.DataFrame(d)

    SourceUse = pulp.LpVariable.dicts("SourceUse", df.index, lowBound=0)
    model = pulp.LpProblem("Reduction", pulp.LpMinimize)

    for idx in df.index:
        emissions[idx] = SourceUse[idx] * df['Emissions'][idx]

    for idx in df.index:
        costs[idx] = SourceUse[idx] * df['Cost'][idx]

    valueToMinimize = (sum([emissions[idx] for idx in df.index]) - sum([costs[idx] for idx in df.index]))


    #objective
    model += valueToMinimize


    #Bound constraints                                                                                                
    for idx in df.index:
        model += SourceUse[idx] <= df['SourceAvailable'][idx]

    # Total SourceUse value should be equal to demand                                                                      
    model += sum([SourceUse[idx] for idx in df.index]) == demand

    # Solve                                                                                                            
    model.solve()


    output = []
    # Output solution                                                                                                            
    for idx in df.index:
        output.append(SourceUse[idx].value())
        #print(df['PowerType'][idx], SourceUse[idx].value())
    output.append(sum([emissions[idx].value() for idx in df.index]))
    output.append(sum([costs[idx].value() for idx in df.index]))
    return output
    #print("Total Emissions: ", sum([emissions[idx].value() for idx in df.index]))
    #print("Total Costs: ", sum([costs[idx].value() for idx in df.index]))



#available = [10781, 0, 623, 4548, 5000, 26, 2371]
#demand = 20000

#output array order = [nuclear, solar, wind, hydroelectric, gas, biofuel, neighbour, total emissions, total cost]
#print(energyOptimization(10781, 0, 623, 4548, 5000, 26, 2371, 20000))