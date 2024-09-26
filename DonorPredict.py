import pandas as pd

# Read the Excel file into a DataFrame
filePath = /LastMile/TestExcel.xlsx

# Read the Excel file into a DataFrame
df = pd.read_excel(filePath)

#Reads in the date column to a DataFrame
dateDF = pd.read_excel(filePath, usecols=['AI'])

#Renames the column from AI to Date
df.rename(columns={'AI': 'Date'}, inplace = True)

# Converts the Date DataFrame to datetime
df['Date'] = pd.to_datetime(df['Date'])

#Defines the specific date to filter by
specificDate = pd.to_datetime('2024-05-15')

# Display the DataFrame
print(dateDF)
