Model 1: Supervisor Narcissism and Gossip about Supervisor
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                     BO   R-squared:                       0.069
Model:                            OLS   Adj. R-squared:                  0.045
Method:                 Least Squares   F-statistic:                     2.880
Date:                Sun, 02 Jun 2024   Prob (F-statistic):             0.0389
Time:                        11:51:29   Log-Likelihood:                -190.14
No. Observations:                 121   AIC:                             388.3
Df Residuals:                     117   BIC:                             399.5
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                         1.4098      1.180      1.195      0.235      -0.927       3.746
snarc                         0.2820      0.302      0.935      0.352      -0.315       0.879
gossip_supervisor             0.2748      0.380      0.723      0.471      -0.478       1.028
snarc_x_gossip_supervisor    -0.0286      0.092     -0.310      0.757      -0.211       0.154
==============================================================================
Omnibus:                        7.589   Durbin-Watson:                   1.799
Prob(Omnibus):                  0.022   Jarque-Bera (JB):                7.721
Skew:                           0.619   Prob(JB):                       0.0211
Kurtosis:                       3.016   Cond. No.                         162.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

Model 2: Supervisor Narcissism and Gossip about Peers
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                     BO   R-squared:                       0.111
Model:                            OLS   Adj. R-squared:                  0.089
Method:                 Least Squares   F-statistic:                     4.890
Date:                Sun, 02 Jun 2024   Prob (F-statistic):            0.00307
Time:                        11:51:29   Log-Likelihood:                -187.30
No. Observations:                 121   AIC:                             382.6
Df Residuals:                     117   BIC:                             393.8
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
=======================================================================================
                          coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------
const                   1.7669      1.223      1.445      0.151      -0.655       4.189
snarc                   0.1124      0.314      0.358      0.721      -0.509       0.734
gossip_peer             0.1248      0.375      0.333      0.740      -0.617       0.867
snarc_x_gossip_peer     0.0332      0.094      0.355      0.724      -0.152       0.219
==============================================================================
Omnibus:                        8.997   Durbin-Watson:                   1.756
Prob(Omnibus):                  0.011   Jarque-Bera (JB):                9.183
Skew:                           0.671   Prob(JB):                       0.0101
Kurtosis:                       3.141   Cond. No.                         172.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

Model 3: Supervisor Narcissism and Gossip Ratio
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                     BO   R-squared:                       0.060
Model:                            OLS   Adj. R-squared:                  0.036
Method:                 Least Squares   F-statistic:                     2.498
Date:                Sun, 02 Jun 2024   Prob (F-statistic):             0.0631
Time:                        11:51:29   Log-Likelihood:                -190.69
No. Observations:                 121   AIC:                             389.4
Df Residuals:                     117   BIC:                             400.6
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
const                    0.8834      1.182      0.747      0.456      -1.457       3.224
snarc                    0.6045      0.303      1.995      0.048       0.004       1.204
gossip_ratio             0.8824      1.028      0.858      0.393      -1.154       2.919
snarc_x_gossip_ratio    -0.2947      0.259     -1.140      0.257      -0.807       0.217
==============================================================================
Omnibus:                       10.780   Durbin-Watson:                   1.874
Prob(Omnibus):                  0.005   Jarque-Bera (JB):               11.586
Skew:                           0.757   Prob(JB):                      0.00305
Kurtosis:                       3.059   Cond. No.                         89.1
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

VIF for Model 1:
                     feature         VIF
0                      const  120.072368
1                      snarc    4.841586
2          gossip_supervisor   27.332088
3  snarc_x_gossip_supervisor   36.101183

VIF for Model 2:
               feature         VIF
0                const  135.196463
1                snarc    5.495248
2          gossip_peer   22.767816
3  snarc_x_gossip_peer   30.093560

VIF for Model 3:
                feature         VIF
0                 const  119.406142
1                 snarc    4.842090
2          gossip_ratio   31.709589
3  snarc_x_gossip_ratio   37.783320