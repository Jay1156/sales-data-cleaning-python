import pandas as pd 
import numpy as np

df = pd.read_csv("data/raw/sales_data_sample.csv", encoding = "latin1")
# print(df.shape())
# print(df.info())
# print(df.isna().sum())
# print(df.isna().sum().sum())
# print(df.duplicated().sum())
df = df.drop(columns = ["Random"])
# print(df.head(7))
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

#after inspecting I found out that quantityordered has values in float and quantity ordered can never be in float 
df["quantityordered"] = df["quantityordered"].astype("int64")
# print(df["quantityordered"].dtypes)
# print(df["quantityordered"].head())

#Inspecting orderdate
# print(df["orderdate"].dtypes)
df["orderdate"] = pd.to_datetime(
    df["orderdate"],
    format = "mixed",
    dayfirst = False,
    errors = "coerce"
)
# print(df["orderdate"].dtypes)
# print(df["orderdate"].head(5))
# print((df["orderdate"].dt.month == df["month_id"]).all())
# print((df["orderdate"].dt.year == df["year_id"]).all()) ## Holds True 

# print(df["status"].unique())
df["status"] = df["status"].str.strip()

# print(df["productline"].unique())
df["productline"] = df["productline"].str.strip()

#Now msrp does not have any none vales and is int64 so it has to be already clean 
#Just checking if it has value < 0 
# print((df["msrp"] <= 0).sum())
# print((df["msrp"] <= 0).any())

df["customername"] = df["customername"].str.strip()

df["phone"] = df["phone"].str.strip()
# print(df.columns)

df["addressline1"] = df["addressline1"].str.strip()

#Now comes the complicated part, this adressline2 has 2521 nan values out of 2823 total rows 
# print(df["addressline2"].isna().sum())
df["addressline2"] = df["addressline2"].fillna("Not Applicable")
# print(df["addressline2"].head(5))

df["city"] = df["city"].str.strip()
# print(df["city"].unique())

# print(df["postalcode"].isin([0, "0"]).any())
df["postalcode"] = df["postalcode"].astype(str).str.strip().str.replace(r"\.0$", "", regex = True)

#Moving to next column 
df["country"] = df["country"].str.strip()

# print(df["state"].unique())
df["state"] = df["state"].str.strip()
abbreviations = {
    "NY" : "New York",
    "CA" : "California",
    "NJ" : "New Jersey",
    "CT"  : "Connecticut",
    "MA" : "Massachusetts",
    "PA" : "Pennsylvania",
    "NSW" : "New South Wales",
    "BC" : "British Columbia",
    "NH" : "New Hampshire",
    "NV" : "Nevada"
}
df["state"] = df["state"].replace(abbreviations).fillna("Unknown")
# print(df["state"].head(20))

df["territory"] = df["territory"].str.strip()
df["territory"] = df["territory"].fillna("NA")
# print(df["territory"].head(12))

df["contactlastname"] = df["contactlastname"].str.strip()
df["contactfirstname"] = df["contactfirstname"].str.strip()

df["dealsize"] = df["dealsize"].str.strip()

col = df.pop("contactfirstname")
idx = df.columns.get_loc("contactlastname")
df.insert(idx, "contactfirstname", col)

df["addressline1"] = df["addressline1"].str.replace("^Berguvsv.*$", "Berguvsvagen 8", regex = True)
df["contactfirstname"] = df["contactfirstname"].str.replace("^Mart.*$", "Martin", regex = True)

# print(df[df["addressline1"] == "Berguvsvagen 8"][["addressline1"]])
# print(df[df["contactfirstname"] == "Martin"][["contactfirstname"]])

# print(df.columns)

# print(df.isna().sum().sum())
# print(df.info)
df.to_csv("data/processed/sales_data_cleaned.csv", index=False)