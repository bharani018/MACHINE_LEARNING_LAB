import csv

# Read the CSV file
with open('machinelearning1.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

# Initialize the hypothesis
hypothesis = data[0][:-1]  # Assume first sample as the hypothesis

# Find the most specific hypothesis
for sample in data:
    if sample[-1] == '1':
        for i in range(len(hypothesis)):
            if sample[i] != hypothesis[i]:
                hypothesis[i] = '?'

# Print the most specific hypothesis
print('The most specific hypothesis is:', hypothesis)
