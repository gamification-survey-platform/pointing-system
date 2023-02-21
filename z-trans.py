import pandas as pd
import numpy as np
import sys

SHIFT_AMOUNT = 90 
STD_DEVIATION = 3

# Load the data from the CSV file
data = pd.read_csv(str(sys.argv[1]))

# Drop the 'student' column, since we don't need it for this analysis
data = data.drop('student', axis=1)

# Calculate the mean and standard deviation of each survey
means = data.mean()
stds = data.std()

# Perform z-transformation on the data
z_data = (data - means) / stds

# Shift mean to 90
shifted_data = z_data * STD_DEVIATION + SHIFT_AMOUNT

# Print the original data and the z-transformed data
print("Original data:\n", data)
print("\nZ-transformed data:\n", z_data)
print("\nShifted data:\n", shifted_data)

# Calculate the mean and standard deviation of each survey after z-transformation
final_means = shifted_data.mean()
final_stds = shifted_data.std()

print("\nFinal survey mean:\n", final_means)
print("\nFinal survey std:\n", final_stds)
