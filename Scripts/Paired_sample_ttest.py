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


# Implementations 
data = {
    "Soil_pH_Before": [6.4, 6.3, 6.5, 6.2, 6.1], "Soil_pH_After": [6.7, 6.6, 6.8, 6.5, 6.4], 
    "Nitrogen_(%)_Before": [6.4, 3.3, 6.5, 5.2, 4.1], "Nitrogen_(%)_After": [8.7, 9.6, 6.9, 9.5, 6.4],
    "Phosphorous (%)_Before": [6.4, 6.3, 6.5, 6.2, 6.1], "Phosphorous (%)_After": [6.7, 6.6, 6.8, 6.5, 6.4],
    "CEC (Meq/100g)_Before": [9.4, 6.3, 8.5, 6.2, 5.1], "CEC (Meq/100g)_After": [6.7, 8.6, 9.8, 6.5, 7.4]  
    }

data = pd.DataFrame(data)
parameter_pairs = {
    "Soil pH": ("Soil_pH_Before", "Soil_pH_After"),
    "Nitrogen (%)": ("Nitrogen_(%)_Before", "Nitrogen_(%)_After"), 
    "Phosphorous (%)": ("Phosphorous (%)_Before", "Phosphorous (%)_After"), 
    "CEC (Meq/100g)": ("CEC (Meq/100g)_Before", "CEC (Meq/100g)_After"),
    }


results_df = paired_t_test(data, parameter_pairs)
display(results_df)