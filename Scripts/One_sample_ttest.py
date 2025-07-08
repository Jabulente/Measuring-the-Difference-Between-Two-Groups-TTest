# Import required libraries
from scipy.stats import ttest_1samp
from itertools import combinations
import pandas as pd
import numpy as np

# Defined function logic to automate test over multiple variables
def one_sample_t_test(df, columns, population_means, alpha=0.05): 
    results = []
    for col in columns:
        if col in df.columns and col in population_means:
            sample_data = df[col].dropna()  # Remove NaN values
            pop_mean = population_means[col]
            
            t_stat, p_value = stats.ttest_1samp(sample_data, pop_mean)
            Interpretation = "Significant Difference" if p_value < alpha else "No Significant Difference"
            
            results.append({
                "Parameter": col,
                "Sample Mean": sample_data.mean(),
                "Hypothesized Mean": pop_mean,
                "T-Statistic": t_stat,
                "P-Value": p_value,
                "Alpha": alpha,
                "Conclusion": Interpretation
            })
    
    return pd.DataFrame(results)