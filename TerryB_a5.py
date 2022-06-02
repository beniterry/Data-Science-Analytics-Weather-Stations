from scipy import stats
from scipy.stats import skewtest, kurtosistest
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean
from statistics import median
plt.close('all')


######################################################################
# Ben Terry
# Data Science & Analytics
######################################################################

###### VARIABLES ######
alpha = .05

################ PART A ################
print('\n'*25)
print("##################################")
print('Output from application TerryB_a5.py')
print('Developed by Ben Terry')
print("##################################\n")

# Read the data file and assign Series object
print('\nInitiating scrubbing for part A...')
datfile='C:\\Users\\ben_i\\Documents\\Beach_Weather_Stations_-_Automated_Sensors.csv'

frame = pd.read_csv(datfile)

count = len(frame) # ROW COUNT

# 1. Drop unwanted columns
frame.drop(columns = ['Barometric Pressure', 'Wet Bulb Temperature', 'Rain Intensity', 'Interval Rain',
                      'Total Rain', 'Precipitation Type', 'Wind Direction', 'Wind Speed',
                      'Maximum Wind Speed', 'Solar Radiation', 'Heading', 'Battery Life',
                      'Measurement Timestamp Label', 'Measurement ID'], axis = 1, inplace = True)

# 2/3. Discard reading <30 and >40
    # Check for only main stations
stationCheck = frame['Station Name'].tolist()

for i in range(0, len(frame)):
    if stationCheck[i] != '63rd Street Weather Station' or stationCheck != 'Oak Street Weather Station' or stationCheck[i] != 'Foster Weather Station':
        stationCheck[i] = None
        
        # Filter incorrect readings
aTemp = frame['Air Temperature'].tolist()

for i in range(0, len(frame)):
    if aTemp[i] < -30 or aTemp[i] > 40:
        aTemp[i] = None

sr = pd.Series(data = aTemp) # Pull the scrubbed list back into Series object
frame['Air Temperature'] = sr # Update scrubbed column to frame



# 4. Isolate the senser entries that were logged during the RQ period of interest (August, 2017)
d = frame['Measurement Timestamp'].str.split().str[0]  # Get first element of Measurement Timestamp date
frame['Date'] = d # Create column of full date: nn/nn/nn

m = d.str.split("/").str[0]  # Split Date by "/" and get first element(month)
frame['Month'] = m # Create column of just the month

y = d.str.split("/").str[2]  # Split Date by "/" and get third element(year)
frame['Year'] = y # Create column of just the year

        # Sort for only August 2017
monthList = frame['Month'].tolist()
yearList = frame['Year'].tolist()
        
        # Month
for i in range(0, len(monthList)):
    if monthList[i] != '08':
        monthList[i] = None

        # Update frame
sr2 = pd.Series(data = monthList)
frame['Month'] = sr2

        # Year
for j in range(0, len(yearList)):
    if yearList[j] != '2017':
        yearList[j] = None

        # Update frame
sr3 = pd.Series(data = yearList)
frame['Year'] = sr3

    # Drop Date column
frame.drop(columns = ['Date'], axis = 1, inplace = True)



# 5/6. only the date-specific rows that will be analyzed as per the Part A RQ
frame.dropna(subset = ['Air Temperature', 'Month', 'Year'], inplace = True) # DROP ALL NAN ROWS

count2 = len(frame)
print('\n######## Scrubbing has been completed! ########\n')
print('Size before scrubbing:', count)
print('Size after scrubbing:', count2)

############### Part A analysis ##############
print('\nTesting for skewness and kurtosis...')

skewResult = skewtest(frame['Air Temperature'], nan_policy = 'omit')
kurtResult = kurtosistest(frame['Air Temperature'], nan_policy = 'omit')

print('\nP-values:\n', 'Skewness -', format(skewResult[1], '.3f'), '\n Kurtosis -', format(kurtResult[1], '.3f'))

print("Parametric techniques are indicated.")

# Varience check
print('\nApplying variance checking between the groups...')

    # Get air temps reading for each station of interest, and put them in lists
stations = frame['Station Name'].tolist()
aTemps = frame['Air Temperature'].tolist()

street = []
oak = []
foster =[]

for i in range(0, len(frame)):
    if stations[i] == '63rd Street Weather Station':
        street.append(aTemps[i])
    if stations[i] == 'Oak Street Weather Station':
        oak.append(aTemps[i])
    else:
        foster.append(aTemps[i])
        

# Bartlett() test
bartlett = stats.bartlett(street, oak, foster)

print('\nBartlett() test results:\n')
print('Test statistic:', format(bartlett[0], '.2f'), '\nP-value =', format(bartlett[1], '.3f'))
print('\nResults are non-significant which confirm homogeneity.\n')

# ANOVA test
print('Performing ANOVA test...\n')
anova = stats.f_oneway(street, oak, foster)
print('F-statistic:', format(anova[0], '.2f'), '\nP-value =', format(anova[1], '.3f'))

print('\nTest Results:\n')
print('Mean Air Temperature at 63rd Street:', format(mean(street), '.2f'))
print('Mean Air Temperature at Oak:', format(mean(oak), '.2f'))
print('Mean Air Temperature at Foster Street:', format(mean(foster), '.2f'))

print('\nThe air temperatures differed between the 3 weather stations.')


# Boxplot
frame2 = pd.DataFrame(list(zip(street, oak, foster)), columns = ['63rd Temps', 'Oak Temps', 'Foster Temps'])

frame2.boxplot(column = ['63rd Temps', 'Oak Temps', 'Foster Temps'])
print('See boxplot for a visual.')



################ PART B ################
print('\n\nInitiating scrubbing for part B...')


# Read the data file and assign Series object
datfile='C:\\Users\\ben_i\\Documents\\Beach_Weather_Stations_-_Automated_Sensors.csv'

frame = pd.read_csv(datfile)

count3 = len(frame) # ROW COUNT

# 1. Drop unwanted columns
frame.drop(columns = ['Barometric Pressure', 'Wet Bulb Temperature', 'Rain Intensity', 'Interval Rain',
                      'Total Rain', 'Precipitation Type', 'Wind Direction', 'Wind Speed',
                      'Maximum Wind Speed', 'Solar Radiation', 'Heading', 'Battery Life',
                      'Measurement Timestamp Label', 'Measurement ID'], axis = 1, inplace = True)


# 2. Scrub the humidity data values. Humidity is measured as a percentage value between 0 and 100.
hum = frame['Humidity'].tolist()

for i in range(0, len(frame)):
    if hum[i] < 0 or hum[i] > 100:
        hum[i] = None
        
sr = pd.Series(data = hum)
frame['Humidity'] = sr



# 3. Only entries where the Station Name column contains the values 63rd Street Weather Station, 
# Foster Weather Station, or Oak Street Weather Station
stationCheck = frame['Station Name'].tolist()

for i in range(0, len(frame)):
    if stationCheck[i] != '63rd Street Weather Station' or stationCheck != 'Oak Street Weather Station' or stationCheck[i] != 'Foster Weather Station':
        stationCheck[i] = None



# 4. Drop nans and overview of scrubbing
frame.dropna(subset = ['Humidity', 'Station Name', 'Measurement Timestamp', 
                       'Air Temperature'], inplace = True) # DROP ALL NAN ROWS

count4 = len(frame)
print('\n######## Scrubbing has been completed! ########\n')
print('Size before scrubbing:', count3)
print('Size after scrubbing:', count4)



############### Part B analysis ##############
# Quick check
mean = sr.mean()
std = sr.std()

print('\nPerforming quick check...')
if (sr.min() <= (mean - (2*std)) == False) or (sr.max() >= (mean - (2*std)) == False):
    print('\nThe distribution is non-normal.\n')
else:
    print('\nThe distribution is normal.\n')

# Skew and Kurt test
skew = sr.skew()
kurt = sr.kurt()

print('Kurtosis: ', format(kurt, '.3f'), '\nSkewness: ', format(skew, '.3f'))


skewResult = skewtest(sr, nan_policy='omit')
kurtResult = kurtosistest(sr, nan_policy='omit')

print('\nZ-scores:\n', 'Skewness -', format(skewResult[0], '.3f'), '\n Kurtosis -', format(kurtResult[0], '.3f'))

if (abs(skewResult[0]) > 3):
    print('\nNon-normality is indicated for skewness.')
else:
    print('\nPotential normality for skewness.')
if (abs(kurtResult[0]) > 3):
    print('Non-normality is detected for kurtosis.')
else:
    print('Potential normality for kurtosis.')

print('Therefore non-parametric techniques will be used.')


# Variance check
print('\nApplying variance checking between the groups...')

    # Get humidity reading for each station of interest, and put them in lists
stations = frame['Station Name'].tolist()
hum = frame['Humidity'].tolist()

street = []
oak = []
foster =[]

for i in range(0, len(frame)):
    if stations[i] == '63rd Street Weather Station':
        street.append(hum[i])
    if stations[i] == 'Oak Street Weather Station':
        oak.append(hum[i])
    else:
        foster.append(hum[i])
        

# Leven() test
levene = stats.levene(street, oak, foster)

print('\nLevene() test results:\n')
print('Test statistic:', format(levene[0], '.2f'), '\nP-value =', format(levene[1], '.3f'))
print('\nResults are non-significant which confirm homogeneity.\n')

# Kruskal-Wallis H test
print('Performing Kruskal-Wallis H test...\n')
kruskal = stats.kruskal(street, oak, foster)
print('H-statistic:', format(kruskal[0], '.2f'), '\nP-value =', format(kruskal[1], '.3f'))

# Median humidity results
print('\nTest Results:\n')
print('Median Humidity at 63rd Street:', format(median(street), '.2f'), '%')
print('Median Humidity at Oak:', format(median(oak), '.2f'), '%')
print('Median Humidity at Foster Street:', format(median(foster), '.2f'), '%')

print('\nThe median humidity differed between the 3 weather stations.')


# Boxplot
frame3 = pd.DataFrame(list(zip(street, oak, foster)), columns = 
                      ['63rd Humidity', 'Oak Humidity', 'Foster Humidity'])

frame3.boxplot(column = ['63rd Humidity', 'Oak Humidity', 'Foster Humidity'])
print('See boxplot for a visual.')

print('\n############### End of application ###############')

























