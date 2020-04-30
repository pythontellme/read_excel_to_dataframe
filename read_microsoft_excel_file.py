import pandas as pd

# Read data from xls file into dataframe
df_pop = pd.read_excel('population.xls', skiprows=3 )

# Print out dataframe
print(df_pop)