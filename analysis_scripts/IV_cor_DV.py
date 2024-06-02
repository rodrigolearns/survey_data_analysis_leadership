import pandas as pd
from scipy.stats import pearsonr
import statsmodels.stats.power as smp

# Load the isolated CSV file
csv_file_path = 'isolated_output_cleaned.csv'
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

# Calculate Pearson correlation
correlation, p_value = pearsonr(snarc, BO)

# Print the correlation and p-value
print(f"Pearson correlation coefficient: {correlation}")
print(f"P-value: {p_value}")

# Calculate the power of the analysis
# Required inputs: effect size (correlation), alpha level, and sample size
effect_size = correlation
alpha = 0.05
sample_size = len(df)

# Calculate power
analysis = smp.FTestAnovaPower()
power = analysis.solve_power(effect_size=effect_size, nobs=sample_size, alpha=alpha)

# Print the power of the analysis
print(f"Power of the analysis: {power}")
