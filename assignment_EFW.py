import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
csv_file_path = "C:/Users/annad/Desktop/datasteward/datasteward/EFWperc_data.csv"
df = pd.read_csv(csv_file_path, delimiter=';')

# see of the import worked: 
print(df)

percentiles = ['2.5', '5', '10', '25', '50', '75', '90', '95', '97.5']
weeks = df['week']

# Plotting
plt.figure(figsize=(10, 6))

for percentile in percentiles:
    values = df[percentile]

    # Smooth the line using numpy
    smooth_values = np.interp(np.arange(len(values)), np.arange(len(values)), values)

    # Plotting the smooth line for each percentile
    plt.plot(weeks, smooth_values, label=f'{percentile}th percentile')

# Set labels and title
plt.xlabel('Gestational Week')
plt.ylabel('Estimated Fetal Weight (EFW)')
plt.title('EFW Percentiles Across Gestational Weeks')
plt.legend()
plt.grid(True)

# User input for gestational age and estimated fetal weight
user_week = float(input('Enter gestational age (rounded in weeks; range 14-40): '))
user_weight = float(input('Enter estimated fetal weight (g): '))

# Plotting user input as a red dot
plt.scatter(user_week, user_weight, color='red', label='User Input')


# Determine the percentile group for the entered estimated fetal weight
percentile_groups = ['5', '50', '95']
percentile_labels = ['<5 percentile', '5-95 percentile', '>95 percentile']

# Find the percentile group for the entered gestational age
user_percentile = None
for i, (lower, upper) in enumerate(zip(percentile_groups[:-1], percentile_groups[1:])):
    if user_weight < df[lower].iloc[df.index[df['week'] == user_week][0]]:
        user_percentile = percentile_labels[i]
        break
    elif user_weight <= df[upper].iloc[df.index[df['week'] == user_week][0]]:
        user_percentile = percentile_labels[i + 1]
        break

# Set user_percentile to the last label if still None
if user_percentile is None:
    user_percentile = percentile_labels[-1]

# Annotate the graph with the user's percentile information below the graph
plt.figtext(0.5, 0.01, f"Your baby's EFW is estimated to be {user_percentile}", ha='center', color='red')

# Show the plot
plt.show()
