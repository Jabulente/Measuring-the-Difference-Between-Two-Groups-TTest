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


# Generating Demostration datasets
def dataset_generation(sample_size=1000):
    np.random.seed(42)
    Plot = np.random.choice(['Plot 1', 'Plot 2', 'Plot 3', 'Plot 4'], size=sample_size)
    Nitrogen = np.random.normal(5, 10, size=sample_size)
    Phosphorous = np.random.normal(7, 2, size=sample_size) 
    Calicium = np.random.normal(5, 8, size=sample_size)
    Zinc = np.random.normal(2, 5, size=sample_size)
    Magnesium = np.random.normal(5, 10, size=sample_size)
    Sulphur = np.random.normal(3, 9, size=sample_size)
    
    data = pd.DataFrame({
        "Plot": Plot,
        'Nitrogens': Nitrogen,
        'Phosphorous': Phosphorous,
        'Calicium': Calicium,
        'Zinc': Zinc,
        'Magnesium': Magnesium,
        'Sulphur': Sulphur
        
    })
    return data

pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_columns', 10)
df = dataset_generation(sample_size=1000)
display(df)


population_means = {"Nitrogens": 2.5, "Phosphorous": 3, "Calicium":4, "Zinc":6, "Magnesium":5.7, "Sulphur":3 }
results_df = one_sample_t_test(df, df.columns, population_means)
display(results_df)
