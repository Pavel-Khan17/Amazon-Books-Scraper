import pandas as pd

# Read CSV and save as Excel
df = pd.read_csv('audible_best_sellers.csv', names=['Book Name', 'Author', 'Rating', 'Number of Ratings', 'Price', 'Book Image Link'])
df.to_excel('audible_best_sellers.xlsx', index=False)