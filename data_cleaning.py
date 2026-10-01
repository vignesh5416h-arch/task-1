import pandas as pd
df = pd.read_csv("data/raw/netflix_titles.csv")

print("\nFINAL DATAFRAME BEFORE CLEANING")
print("Missing values in the dataframe before cleaning:")
print(df.isnull().sum())
print("Duplicate rows in the dataframe before cleaning:")
print(df.duplicated().sum())
print("Data types of the columns in the dataframe before cleaning:")
print(df.dtypes)
print("\ndataset shape before cleaning:")
print(df.shape)



print(df.isnull().sum())
df=df.dropna()
print(df.isnull().sum())
print("NUMBER OF DUPLICATE ROWS IN THE DATAFRAME")
print(df.duplicated().sum())
print(df.columns)

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
)

print("COLUMN NAMES IN THE DATAFRAME AFTER CLEANING")
#print(df.columns)

#print(df["type"].unique())

df['type'] = df['type'].str.strip().str.title()

#print(df["type"].unique())
df["release_year"] = df["release_year"].astype(int)
#print(df.dtypes)

#print(df["date_added"].dtype)

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

#print(df["date_added"].dtype)

df["date_added"] = df["date_added"].fillna(pd.Timestamp("2020-01-01"))



print("\nFINAL DATAFRAME AFTER CLEANING")
print("Missing values in the dataframe after cleaning:")
print(df.isnull().sum())
print("Duplicate rows in the dataframe after cleaning:")
print(df.duplicated().sum())
print("Data types of the columns in the dataframe after cleaning:")
print(df.dtypes)
print("\ndataset shape after cleaning:")
print(df.shape)



df.to_csv("data/cleaned/netflix_titles_cleaned.csv", index=False)


print("\n cleaned data saved to 'data/cleaned/netflix_titles_cleaned.csv'")