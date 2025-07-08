# Import required libraries 
from scipy.stats import ttest_rel
from itertools import combinations
import pandas as pd

# Define function logic to perfor test over multiple variables
def paired_t_test(df, pairs, alpha=0.05): 
    results = []
    for param, (before_col, after_col) in pairs.items():
        if before_col in df.columns and after_col in df.columns:
            before_data = df[before_col].dropna()
            after_data = df[after_col].dropna()
            min_length = min(len(before_data), len(after_data))
            before_data = before_data[:min_length]
            after_data = after_data[:min_length]
            
            #t_stat, p_value = stats.ttest_rel(before_data, after_data)
            t_stat, p_value = ttest_rel(before_data, after_data)
            conclusion = "Significant Difference" if p_value < alpha else "No Significant Difference"
            
            results.append({
                "Parameter": param,
                "Before Mean": before_data.mean(),
                "After Mean": after_data.mean(),
                "T-Statistic": t_stat,
                "P-Value": p_value,
                "Alpha": alpha,
                "Conclusion": conclusion
            })
    
    return pd.DataFrame(results)