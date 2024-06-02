import pandas as pd
from scipy.stats import pearsonr
import statsmodels.stats.power as smp

# Load the isolated CSV file
csv_file_path = '../survey_data/isolated_output_cleaned.csv'
df = pd.read_csv(csv_file_path)

# Define the columns for each category of interest
bo_columns = ['BO1', 'BO2', 'BO3', 'BO4', 'BO5', 'BO6']
snarc_columns = ['snarc1', 'snarc2', 'snarc3', 'snarc4', 'snarc5', 'snarc6', 'snarc7', 'snarc8', 'snarc9', 'snarc10', 'snarc11', 'snarc12', 'snarc13']
gossip_leader_columns = ['gossip2', 'gossip4']

# Calculate the average scores for BO and snarc
df['BO'] = df[bo_columns].mean(axis=1)
df['snarc'] = df[snarc_columns].mean(axis=1)

# Remove rows with any NaN values
df = df.dropna()

# Extract the relevant columns for correlation
snarc = df['snarc']
BO = df['BO']

# Calculate Pearson correlation for the entire dataset
correlation, p_value = pearsonr(snarc, BO)

# Print the correlation and p-value for the entire dataset
print(f"Overall Pearson correlation coefficient: {correlation}")
print(f"Overall P-value: {p_value}")

# Calculate the power of the analysis for the entire dataset
# Required inputs: effect size (correlation), alpha level, and sample size
effect_size = correlation
alpha = 0.05
sample_size = len(df)

# Calculate power for the entire dataset
analysis = smp.FTestAnovaPower()
power = analysis.solve_power(effect_size=effect_size, nobs=sample_size, alpha=alpha)

# Print the power of the analysis for the entire dataset
print(f"Overall Power of the analysis: {power}")

# Calculate the 75th percentile for snarc
snarc_75th_percentile = df['snarc'].quantile(0.75)

# Filter the dataset for the top quartile of snarc
top_quartile_df = df[df['snarc'] >= snarc_75th_percentile]

# Extract the relevant columns for correlation in the top quartile
snarc_top_quartile = top_quartile_df['snarc']
BO_top_quartile = top_quartile_df['BO']

# Calculate Pearson correlation for the top quartile of snarc
top_quartile_correlation, top_quartile_p_value = pearsonr(snarc_top_quartile, BO_top_quartile)

# Print the correlation and p-value for the top quartile
print(f"Top Quartile Pearson correlation coefficient: {top_quartile_correlation}")
print(f"Top Quartile P-value: {top_quartile_p_value}")

# Calculate the power of the analysis for the top quartile
# Required inputs: effect size (correlation), alpha level, and sample size
top_quartile_effect_size = top_quartile_correlation
top_quartile_sample_size = len(top_quartile_df)

# Calculate power for the top quartile
top_quartile_analysis = smp.FTestAnovaPower()
top_quartile_power = top_quartile_analysis.solve_power(effect_size=top_quartile_effect_size, nobs=top_quartile_sample_size, alpha=alpha)

# Print the power of the analysis for the top quartile
print(f"Top Quartile Power of the analysis: {top_quartile_power}")
