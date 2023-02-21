import pandas as pd
import numpy as np
import sys

SHIFT_AMOUNT = 90 
STD_DEVIATION = 3

# in case of number std dev = 0, we have to manually assign an ipsatized value
def convert(score):
    if score == 1: return -1
    if score == 2: return -0.5
    if score == 3: return 0
    if score == 4: return 0.5
    if score == 5: return 1

# Load the data from the CSV file
data = pd.read_csv(str(sys.argv[1]))

# Drop the 'student' column, since we don't need it for this analysis
data = data.drop('student', axis=1)

# Calculate the mean and standard deviation of each survey
means = data.mean(axis=1)
stds = data.std(axis=1)

# Perform ipsatization on the data
i_data = data.copy()
for i in range(len(data)):
    for j in range(len(data.columns)):
        i_data.iloc[i, j] = (data.iloc[i, j] - means[i]) / stds[i] if stds[i] != 0 else convert(data.iloc[i, j])

# Shift mean to SHIFT_AMOUNT
shifted_data = i_data * STD_DEVIATION + SHIFT_AMOUNT

# Print the original data and the ipsatized data
print("Original data:\n", data)
print("\nIpsatized data:\n", i_data)
print("\nShifted data:\n", shifted_data)


# Calculate the mean and standard deviation of each survey after z-transformation
final_means = shifted_data.mean()
final_stds = shifted_data.std()

print("\nFinal survey mean:\n", final_means)
print("\nFinal survey std:\n", final_stds)
