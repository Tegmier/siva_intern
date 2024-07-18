import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Define the data file path
data_file = os.path.join('data', 'Top_Highest_Openings.csv')

# Read the CSV data into a DataFrame
movies = pd.read_csv(data_file)

# Visualizing the first 10 data
print(movies.head(10))

# List the columns of the data
print("List the columns in the data:")
print(movies.columns)
print("-------------------------------------------------\n")

# Visualize the distribution of Opening Weekend Gross
print("Demonstrating the opening gross data distribution:")
print(movies["Opening"].describe())
print("-------------------------------------------------\n")

plt.figure(figsize=(10, 6))
movies["Opening"].hist(bins=100)
plt.title('Distribution of Opening Weekend Gross')
plt.xlabel('Opening Weekend Gross')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Visualize the distribution of Total Gross
print("Demonstrating the total gross data distribution:")
print(movies["Total Gross"].describe())
print("-------------------------------------------------\n")

plt.figure(figsize=(10, 6))
movies["Total Gross"].hist(bins=100)
plt.title('Distribution of Total Gross')
plt.xlabel('Total Gross')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# The top 10 total gross movies
top_grossing_movies = movies.nlargest(10, 'Total Gross')
plt.figure(figsize=(10, 6))
sns.barplot(x='Total Gross', y='Release', hue='Distributor', data=top_grossing_movies, palette='viridis', dodge=False)
plt.xlabel('Total Gross')
plt.title('Top 10 Highest Grossing Movies by Distributor')
plt.legend(title='Distributor', loc='lower right')
plt.show()

# View the theater data
print("Demonstrating the theater data distribution:")
print(movies["Theaters"].describe())
print("-------------------------------------------------\n")

# The correlation between opening gross and total gross
correlation = movies['Opening'].corr(movies['Total Gross'])
print(f"The correlation between opening gross and total gross: {correlation}")
print("-------------------------------------------------\n")

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Opening', y='Total Gross', hue='Distributor', size='Theaters', sizes=(20, 200), data=movies, palette='viridis', legend=False)
plt.title('Opening Weekend Gross vs. Total Gross by Distributor')
plt.xlabel('Opening Weekend Gross')
plt.ylabel('Total Gross')
plt.grid(True)
plt.show()

# Calculate the average opening and total gross by distributor, and add the movie count
average_gross_by_distributor = movies.groupby('Distributor').agg({
    'Opening': 'mean',
    'Total Gross': 'mean',
    'Release': 'count'  # Calculate the number of movies per distributor
}).reset_index().rename(columns={'Release': 'Movie Count'})

# Exclude distributors with less than 10 movies
filtered_distributor = average_gross_by_distributor[average_gross_by_distributor['Movie Count'] >= 10]

# Select the top 10 distributors by average total gross
top10_average_gross_by_distributor = filtered_distributor.nlargest(10, 'Total Gross').reset_index(drop=True)

# Plot the average opening and total gross for the top 10 distributors
plt.figure(figsize=(14, 8))
ax = top10_average_gross_by_distributor.plot(kind='bar', x='Distributor', y=['Opening', 'Total Gross'], figsize=(14, 8), width=0.8)

# Add movie count as text annotations
for idx, row in top10_average_gross_by_distributor.iterrows():
    ax.text(idx, row['Total Gross'] + 10, f"Count: {int(row['Movie Count'])}", ha='center', va='bottom')

plt.title('Top 10 Distributors by Average Total Gross (with >= 10 movies)')
plt.xlabel('Distributor')
plt.ylabel('Gross (in billions)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Gross Type')
plt.show()

# Show the result
print("Top 10 Average Opening and Total Gross by Distributor (>= 10 movies):")
print(top10_average_gross_by_distributor)
