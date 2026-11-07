
# =====================================================
# PROJECT: COVID-19 GLOBAL IMPACT DASHBOARD
# =====================================================

# STEP 1: IMPORT LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# STEP 2: LOAD DATASET

df = pd.read_csv("covid_dashboard_practice_dataset.csv")

print("\n========== ORIGINAL DATASET ==========")
print(df.head())

# STEP 3: DATASET INFORMATION

print("\n========== DATASET INFORMATION ==========")
print(df.info())

print("\nTotal Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

# STEP 4: DATA CLEANING

df["date"] = pd.to_datetime(df["date"])

# Remove duplicate records
df = df.drop_duplicates()

# Handle missing values
numeric_columns = df.select_dtypes(include="number").columns
df[numeric_columns] = df[numeric_columns].fillna(0)

# STEP 5: CALCULATE NEW METRICS

df["death_percentage"] = (
    df["total_deaths"] / df["total_cases"] * 100
).fillna(0).round(2)

df["cases_per_million"] = (
    df["total_cases"] / df["population"] * 1000000
).fillna(0).round(2)

print("\n========== CLEANED DATA ==========")
print(df.head())

# STEP 6: SAVE CLEANED DATASET

df.to_csv("cleaned_covid_data.csv", index=False)

print("\nCleaned dataset saved successfully!")

# STEP 7: GLOBAL SUMMARY

latest = df.sort_values("date").groupby(
    "location", as_index=False
).tail(1)

total_cases = latest["total_cases"].sum()
total_deaths = latest["total_deaths"].sum()
total_vaccinations = latest["total_vaccinations"].sum()

print("\n========== GLOBAL SUMMARY ==========")
print("Total Cases:", total_cases)
print("Total Deaths:", total_deaths)
print("Total Vaccinations:", total_vaccinations)

# STEP 8: COUNTRY-WISE ANALYSIS

country_cases = latest.groupby("location")[
    "total_cases"
].sum()

country_deaths = latest.groupby("location")[
    "total_deaths"
].sum()

print("\n========== COUNTRY-WISE CASES ==========")
print(country_cases)

print("\n========== COUNTRY-WISE DEATHS ==========")
print(country_deaths)

# STEP 9: CASES BAR CHART

plt.figure(figsize=(9, 5))

country_cases.plot(kind="bar")

plt.title("Country-wise COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("country_cases.png")
plt.show()

# STEP 10: DEATHS BAR CHART

plt.figure(figsize=(9, 5))

country_deaths.plot(kind="bar")

plt.title("Country-wise COVID-19 Deaths")
plt.xlabel("Country")
plt.ylabel("Total Deaths")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("country_deaths.png")
plt.show()

# STEP 11: MONTHLY COVID TREND

plt.figure(figsize=(10, 5))

for country in df["location"].unique():

    country_data = df[df["location"] == country]

    plt.plot(
        country_data["date"],
        country_data["total_cases"],
        marker="o",
        label=country
    )

plt.title("Monthly COVID-19 Cases Trend")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_trend.png")
plt.show()

# STEP 12: VACCINATION COMPARISON

vaccination_data = latest.set_index("location")[
    "total_vaccinations"
]

plt.figure(figsize=(9, 5))

vaccination_data.plot(kind="bar")

plt.title("Country-wise Vaccination Comparison")
plt.xlabel("Country")
plt.ylabel("Total Vaccinations")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("vaccination_comparison.png")
plt.show()

# STEP 13: CORRELATION ANALYSIS

correlation = df[
    ["total_cases", "total_deaths", "total_vaccinations"]
].corr()

print("\n========== CORRELATION ==========")
print(correlation)

# STEP 14: FINAL PROJECT INSIGHTS

print("\n========== PROJECT INSIGHTS ==========")

print("1. Country-wise COVID cases were compared.")

print("2. Total deaths were analyzed.")

print("3. Vaccination trends were compared.")

print("4. Monthly COVID-19 case trends were visualized.")

print("5. Relationship between cases, deaths and vaccinations was examined.")

# STEP 15: FINAL MESSAGE

print("\n====================================")
print("COVID-19 ANALYSIS COMPLETED!")
print("All charts and cleaned data generated.")
print("====================================")
