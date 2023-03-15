import pandas as pd
import numpy as np
import sys

MAX = 100
MIN = 80
# in case of number std dev = 0, we have to manually assign an ipsatized value
def convert(score):
    if score == 1: return -1
    if score == 2: return -0.5
    if score == 3: return 0
    if score == 4: return 0.5
    if score == 5: return 1

def min_max_scale(data):
    min_value = min(data)
    max_value = max(data)
    normalized_data = []
    for value in data:
        normalized_value = (value - min_value) / (max_value - min_value)
        normalized_data.append(normalized_value)
    return normalized_data

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

# Print the original data and the ipsatized data
print("Original data:\n", data)
print("\nIpsatized data:\n", i_data)

# Calculate the means of each survey as their score 
i_means = i_data.mean()
i_stds = i_data.std()

print("\nIpsatized survey mean:\n", i_means)
print("\nIpsatized survey std:\n", i_stds)

# Normalize the scores
normalized_means = min_max_scale(i_means)
print("\nNormalized means:\n", normalized_means)


# Convert scores to desired range
range = MAX - MIN
final_means = [score * range + MIN for score in normalized_means]

print("\nFinal survey mean:\n", final_means)
