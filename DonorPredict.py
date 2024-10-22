import pandas as pd

# Read in an input of a date
dateInput = input("Enter the date (YYYY-MM-DD): ")

# Read the Excel file into a DataFrame
filePath = "Last Mile Food Rescues_rescue overview.csv"

# Read the Excel file into a DataFrame
df = pd.read_csv(filePath, low_memory=False)

# Reads in the date column to a DataFrame
dateDF = pd.read_csv(filePath, usecols=["rescue_date"])

# Converts the Date DataFrame to datetime
df["rescue_date"] = pd.to_datetime(df["rescue_date"])

# Method that takes the date input and filters results


def filterByDate(dateInput):
    # Defines the specific date to filter by
    specificDate = pd.to_datetime(dateInput)

    # Creates a new DataFrame with results matching the inputed date
    filteredRows = df[df["rescue_date"] == specificDate]

    return filteredRows


# Creates a new DataFrame using the filterByDate method
filteredRows = filterByDate(dateInput)

# Display the DataFrame
print(filteredRows)
