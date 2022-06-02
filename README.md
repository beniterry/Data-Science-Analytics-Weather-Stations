# Data-Science-Analytics-Wheather-Stations
Pandas dataframe analysis on weather stations automated sensors - scrubs, filters, and runs data analysis tests.


# Output From Application TerryB_a5.py - Developed by Ben Terry



Initiating scrubbing for part A...

######## Scrubbing has been completed! ########

Size before scrubbing: 109982
Size after scrubbing: 2083<br /><br />

Testing for skewness and kurtosis...

P-values:
Skewness - 0.946 
Kurtosis - 0.090
Parametric techniques are indicated.<br /><br />

Applying variance checking between the groups...

Bartlett() test results:

Test statistic: 3.53 
P-value = 0.171

Results are non-significant which confirm homogeneity.<br /><br />

Performing ANOVA test...

F-statistic: 14.05 
P-value = 0.000

Test Results:

Mean Air Temperature at 63rd Street: 22.09
Mean Air Temperature at Oak: 22.39
Mean Air Temperature at Foster Street: 21.74

The air temperatures differed between the 3 weather stations.<br /><br />


Initiating scrubbing for part B...

######## Scrubbing has been completed! ########

Size before scrubbing: 109982
Size after scrubbing: 109907

Performing quick check...

The distribution is normal.

Kurtosis:  -0.392 
Skewness:  -0.356

Z-scores:
Skewness - -46.779 
Kurtosis - -33.273

Non-normality is indicated for skewness.
Non-normality is detected for kurtosis.
Therefore non-parametric techniques will be used.<br /><br />

Applying variance checking between the groups...

Levene() test results:

Test statistic: 4.70 
P-value = 0.009

Results are non-significant which confirm homogeneity.<br /><br />

Performing Kruskal-Wallis H test...

H-statistic: 3004.21 
P-value = 0.000

Test Results:

Median Humidity at 63rd Street: 75.00 %
Median Humidity at Oak: 68.00 %
Median Humidity at Foster Street: 71.00 %

The median humidity differed between the 3 weather stations.
See boxplot for a visual.<br /><br />
![img](https://www.linkpicture.com/q/Figure-2022-06-02-010410.png)

############### End of Application ###############
