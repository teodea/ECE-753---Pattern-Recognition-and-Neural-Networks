import pandas as pd

# Load JSON data into DataFrame
data = pd.read_json('arxiv-metadata-oai-snapshot.json', lines=True)


#print(data.columns)                 # See all column names
#print(data.head())                  # Print the first few rows of the DataFrame
#print(data.iloc[0])                 # Print first row
#print(data.loc[0, 'title'])         # Print the value of column 'title' from first row
#print(data.loc[0, 'abstract'])      # Print the value of column 'abstract' from first row
#print(data.loc[0, 'categories'])    # Print the value of column 'categories' from first row

# Split the 'categories' strings into lists
categories_expanded = data['categories'].str.split()
unique_categories = pd.Series([item for sublist in categories_expanded for item in sublist]).unique() 
number_of_unique_categories = len(unique_categories)
#print(f"There are {number_of_unique_categories} unique categories in the dataset.")
#print(unique_categories)


filtered_data = data[['title', 'abstract', 'categories']]


