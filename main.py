import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('life_expectancy_db.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info()) 

import pandas as pd
import matplotlib.pyplot as plt

# Remove trailing and leading whitespaces from column names
df.columns = df.columns.str.strip()

# Filter the data to only include rows where 'Country' is equal to 'Brazil'
df_brazil = df[df['Country'] == 'Brazil']

# Calculate descriptive statistics for 'Life expectancy', 'GDP', and 'percentage expenditure' columns
desc_stats = df_brazil[['Life expectancy', 'GDP', 'percentage expenditure']].describe()
desc_stats = desc_stats.round(2)

# Print the descriptive statistics
print("Estatísticas Descritivas para o Brasil (2000-2015):\n")
print(desc_stats.to_markdown(numalign="left", stralign="left"))

# Export descriptive statistics to CSV
desc_stats.to_csv('desc_stats_brazil.csv', index=True)

# Create a line plot for life expectancy, GDP, and percentage expenditure over the years
df_brazil_melted = df_brazil.melt('Year', ['Life expectancy', 'GDP', 'percentage expenditure'])
plt.figure(figsize=(10, 6))
for label, df_group in df_brazil_melted.groupby('variable'):
    plt.plot(df_group['Year'], df_group['value'], marker='o', label=label)
plt.title('Brasil: Expectativa de Vida, PIB per capita e Gastos com Saúde (2000-2015)')
plt.xlabel('Year')
plt.ylabel('Valores')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('line_plot_brazil_life_expectancy_gdp_health_expenditure.png')

# Show the plot
plt.show()

# Calculate the mean of 'Life expectancy', 'GDP', and 'percentage expenditure' by country
country_means = df.groupby('Country')[['Life expectancy', 'GDP', 'percentage expenditure']].mean()

# Sort the DataFrame by 'Life expectancy' in descending order
country_means_sorted = country_means.sort_values(by='Life expectancy', ascending=False)

# Print the top 10 countries
print("\nTop 10 países por expectativa de vida média (2000-2015):\n")
print(country_means_sorted.head(10).round(2).to_markdown(numalign="left", stralign="left"))

# Print the bottom 10 countries
print("\nÚltimos 10 países por expectativa de vida média (2000-2015):\n")
print(country_means_sorted.tail(10).round(2).to_markdown(numalign="left", stralign="left"))

# Export top and bottom 10 countries to CSV
country_means_sorted.head(10).round(2).to_csv('top_10_countries_life_expectancy.csv', index=True)
country_means_sorted.tail(10).round(2).to_csv('bottom_10_countries_life_expectancy.csv', index=True)
