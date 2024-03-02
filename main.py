# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd

# Since the file is an image, we cannot directly read the data from it.
# We would normally use OCR (Optical Character Recognition) to extract the text from an image,
# but that capability isn't available in this environment.

# We'll create a placeholder DataFrame with a similar structure to perform the analysis.
# The user must replace this with the actual data extracted from the image using OCR software.
data = {
    'XAxis': [0.06147764, 0.0611123, 0.06088585, 0.06060662, 0.06054281],
    'YAxis': [0.4709898, 0.4695622, 0.4681808, 0.4668556, 0.46595],
    'ZAxis': [0.2530193, 0.2528221, 0.2523402, 0.2516597, 0.2510194]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the standard deviation and variance for each axis
std_dev = df.std()
variance = df.var()

(std_dev, variance)