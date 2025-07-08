# Import required libraries
from scipy.stats import ttest_ind
from itertools import combinations
import pandas as pd

# Defined function logic to automate test over multiple variables
def Independent_ttest(df, group_column, Variables):
    unique_groups = df[group_column].unique()
    group_combinations = list(combinations(unique_groups, 2))
    results = []
    for column in Variables:
        for group1, group2 in group_combinations:
            group1_data = df[df[group_column] == group1][column]
            group2_data = df[df[group_column] == group2][column]
            t_stat, p_value = ttest_ind(group1_data, group2_data, equal_var=False)
            
            results.append({
                'Parameter': column,
                'Group 1': group1,
                'Group 2': group2,
                'T-Statistic': t_stat,
                'P-Value': p_value,
                'Interpretation': 'Significant' if p_value < 0.05 else 'Not Significant'
            })
        
    results_df = pd.DataFrame(results)
    return results_df