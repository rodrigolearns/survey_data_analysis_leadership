import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import pearsonr

# Load the isolated CSV file
csv_file_path = '../survey_data/isolated_output_cleaned.csv'
df = pd.read_csv(csv_file_path)

# Define the columns for each category of interest
bo_columns = ['BO1', 'BO2', 'BO3', 'BO4', 'BO5', 'BO6']
snarc_columns = ['snarc1', 'snarc2', 'snarc3', 'snarc4', 'snarc5', 'snarc6', 'snarc7', 'snarc8', 'snarc9', 'snarc10', 'snarc11', 'snarc12', 'snarc13']
gossip_supervisor_columns = ['gossip2', 'gossip4']
gossip_peer_columns = ['gossip1', 'gossip3', 'gossip5']

# Calculate the average scores for BO, snarc, gossip towards the supervisor, and gossip about peers
df['BO'] = df[bo_columns].mean(axis=1)
df['snarc'] = df[snarc_columns].mean(axis=1)
df['gossip_supervisor'] = df[gossip_supervisor_columns].mean(axis=1)
df['gossip_peer'] = df[gossip_peer_columns].mean(axis=1)

# Calculate the ratio of gossip about the supervisor to gossip about peers
df['gossip_ratio'] = df['gossip_supervisor'] / df['gossip_peer']

# Remove rows with any NaN values
df = df.dropna()

# Add interaction terms
df['snarc_x_gossip_supervisor'] = df['snarc'] * df['gossip_supervisor']
df['snarc_x_gossip_peer'] = df['snarc'] * df['gossip_peer']
df['snarc_x_gossip_ratio'] = df['snarc'] * df['gossip_ratio']

# Model 1: Supervisor Narcissism and Gossip about Supervisor
X1 = df[['snarc', 'gossip_supervisor', 'snarc_x_gossip_supervisor']]
y = df['BO']
X1 = sm.add_constant(X1)
model1 = sm.OLS(y, X1).fit()

# Model 2: Supervisor Narcissism and Gossip about Peers
X2 = df[['snarc', 'gossip_peer', 'snarc_x_gossip_peer']]
y = df['BO']
X2 = sm.add_constant(X2)
model2 = sm.OLS(y, X2).fit()

# Model 3: Supervisor Narcissism and Gossip Ratio
X3 = df[['snarc', 'gossip_ratio', 'snarc_x_gossip_ratio']]
y = df['BO']
X3 = sm.add_constant(X3)
model3 = sm.OLS(y, X3).fit()

# Print the summaries of the regression analyses
print("Model 1: Supervisor Narcissism and Gossip about Supervisor")
print(model1.summary())
print("\nModel 2: Supervisor Narcissism and Gossip about Peers")
print(model2.summary())
print("\nModel 3: Supervisor Narcissism and Gossip Ratio")
print(model3.summary())

# Calculate Variance Inflation Factor (VIF) for each model to check for multicollinearity
vif_data1 = pd.DataFrame()
vif_data1["feature"] = X1.columns
vif_data1["VIF"] = [variance_inflation_factor(X1.values, i) for i in range(len(X1.columns))]

vif_data2 = pd.DataFrame()
vif_data2["feature"] = X2.columns
vif_data2["VIF"] = [variance_inflation_factor(X2.values, i) for i in range(len(X2.columns))]

vif_data3 = pd.DataFrame()
vif_data3["feature"] = X3.columns
vif_data3["VIF"] = [variance_inflation_factor(X3.values, i) for i in range(len(X3.columns))]

# Print VIFs
print("\nVIF for Model 1:")
print(vif_data1)
print("\nVIF for Model 2:")
print(vif_data2)
print("\nVIF for Model 3:")
print(vif_data3)

# Plotting

# Scatter plot with regression line for snarc vs BO with statistical details
correlation, p_value = pearsonr(df['snarc'], df['BO'])
plt.figure(figsize=(7, 6))
sns.regplot(x='snarc', y='BO', data=df, scatter_kws={'s': 50}, line_kws={'color': 'red'})
plt.title('Scatter Plot with Regression Line\nSupervisor Narcissism vs Worker Burnout')
plt.xlabel('Supervisor Narcissism (snarc)')
plt.ylabel('Worker Burnout (BO)')
plt.text(0.05, 0.95, f'Pearson r: {correlation:.2f}\nP-value: {p_value:.3f}', 
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))
plt.show()

# Interaction Plot for Model 1 (Gossip about Supervisor)
plt.figure(figsize=(7, 6))
sns.scatterplot(x='snarc', y='BO', hue='gossip_supervisor', palette='RdYlGn_r', data=df, edgecolor=None)
sns.regplot(x='snarc', y='BO', data=df, scatter=False, color='red', line_kws={'label': 'Regression Line'})
plt.title('Interaction Plot\nSupervisor Narcissism vs Worker Burnout with Gossip about Supervisor')
plt.xlabel('Supervisor Narcissism (snarc)')
plt.ylabel('Worker Burnout (BO)')
plt.legend()
plt.show()

# Interaction Plot for Model 2 (Gossip about Peers)
plt.figure(figsize=(7, 6))
sns.scatterplot(x='snarc', y='BO', hue='gossip_peer', palette='RdYlGn_r', data=df, edgecolor=None)
sns.regplot(x='snarc', y='BO', data=df, scatter=False, color='red', line_kws={'label': 'Regression Line'})
plt.title('Interaction Plot\nSupervisor Narcissism vs Worker Burnout with Gossip about Peers')
plt.xlabel('Supervisor Narcissism (snarc)')
plt.ylabel('Worker Burnout (BO)')
plt.legend()
plt.show()

# Interaction Plot for Model 3 (Gossip Ratio)
plt.figure(figsize=(7, 6))
sns.scatterplot(x='snarc', y='BO', hue='gossip_ratio', palette='coolwarm', data=df, edgecolor=None)
sns.regplot(x='snarc', y='BO', data=df, scatter=False, color='red', line_kws={'label': 'Regression Line'})
plt.title('Interaction Plot\nSupervisor Narcissism vs Worker Burnout with Gossip Ratio')
plt.xlabel('Supervisor Narcissism (snarc)')
plt.ylabel('Worker Burnout (BO)')
plt.legend()
plt.show()

# Distribution of Gossip Ratio
plt.figure(figsize=(7, 6))
sns.histplot(df['gossip_ratio'], bins=20, kde=True)
plt.title('Distribution of Gossip Ratio')
plt.xlabel('Gossip Ratio')
plt.ylabel('Frequency')
plt.show()

# 3D Scatter Plot for Worker Burnout, Supervisor Narcissism, and Gossip about the Supervisor
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(df['snarc'], df['gossip_supervisor'], df['BO'], c=df['gossip_supervisor'], cmap='RdYlGn_r', edgecolor=None)

# Fit plane of best fit
X = df[['snarc', 'gossip_supervisor']]
X = sm.add_constant(X)
model = sm.OLS(df['BO'], X).fit()
b0, b1, b2 = model.params

# Create a meshgrid for plotting the plane
snarc_range = np.linspace(df['snarc'].min(), df['snarc'].max(), 10)
gossip_supervisor_range = np.linspace(df['gossip_supervisor'].min(), df['gossip_supervisor'].max(), 10)
snarc_grid, gossip_supervisor_grid = np.meshgrid(snarc_range, gossip_supervisor_range)
BO_plane = b0 + b1 * snarc_grid + b2 * gossip_supervisor_grid

ax.plot_surface(snarc_grid, gossip_supervisor_grid, BO_plane, alpha=0.3, color='blue', edgecolor='none')

ax.set_xlabel('Supervisor Narcissism (snarc)')
ax.set_ylabel('Gossip about Supervisor')
ax.set_zlabel('Worker Burnout (BO)')
ax.set_title('3D Scatter Plot\nWorker Burnout, Supervisor Narcissism, and Gossip about Supervisor')

# Adding a color bar to the plot
cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label('Gossip about Supervisor')

plt.show()
