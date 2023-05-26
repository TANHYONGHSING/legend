import pandas as pd
# create a sample DataFrame
df = pd.DataFrame({'name': ['John', 'Mary', 'Peter'],'age': [28, 35, 42],'country': ['USA', 'Canada', 'Australia']})
# write the DataFrame to a CSV file
df.to_csv('sample.csv', index=False)