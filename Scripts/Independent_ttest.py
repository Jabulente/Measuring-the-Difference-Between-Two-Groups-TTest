import pandas as pd
from scipy.stats import ttest_ind
from itertools import combinations

def independent_ttest(df, group_cols, variables):
    results = []
    for category in group_cols:
        unique_groups = df[category].unique()
        group_combinations = list(combinations(unique_groups, 2))
        
        for column in variables:
            for group1, group2 in group_combinations:
                group1_data = df[df[category] == group1][column].dropna()
                group2_data = df[df[category] == group2][column].dropna()
                
                if len(group1_data) > 1 and len(group2_data) > 1:  # Ensure enough samples
                    t_stat, p_value = ttest_ind(group1_data, group2_data, equal_var=False)
                    
                    results.append({
                        'Group Category': category,
                        'Variable': column,
                        'Group 1': group1,
                        'Group 2': group2,
                        'Group 1 Mean': group1_data.mean(),
                        'Group 2 Mean': group2_data.mean(),
                        'Mean Diff.': group1_data.mean() - group2_data.mean(),
                        'T-Statistic': t_stat,
                        'P-Value': p_value,
                        'Significant (α=0.05)': p_value < 0.05
                    })
    
    return pd.DataFrame(results)

# Sample dataset simulation (replace with your actual data loading)
data = {
    'Fertilizer': ['Organic']*20 + ['Inorganic']*20 + ['Control']*20,
    'Light Exposure': ['Low']*10 + ['High']*10 + ['Low']*10 + ['High']*10 + ['Low']*10 + ['High']*10,
    'Plant Height (cm)': list(np.random.normal(30, 5, 20)) + list(np.random.normal(35, 5, 20)) + list(np.random.normal(32, 5, 20)),
    'Leaf Area (cm²)': list(np.random.normal(150, 30, 20)) + list(np.random.normal(170, 30, 20)) + list(np.random.normal(160, 30, 20)),
    'Chlorophyll Content (SPAD units)': list(np.random.normal(40, 5, 20)) + list(np.random.normal(45, 5, 20)) + list(np.random.normal(42, 5, 20))
}
df = pd.DataFrame(data)

# Execute analysis
group_cols = ['Fertilizer', 'Light Exposure']
variables = ['Plant Height (cm)', 'Leaf Area (cm²)', 'Chlorophyll Content (SPAD units)']
results = independent_ttest(df, group_cols=group_cols, variables=variables)

# Display formatted results
pd.set_option('display.float_format', '{:.4f}'.format)
display(results.style.format({
    'Group 1 Mean': '{:.2f}',
    'Group 2 Mean': '{:.2f}',
    'T-Statistic': '{:.3f}',
    'P-Value': '{:.5f}'
}).background_gradient(subset=['P-Value'], cmap='YlOrRd'))
