"""
Data Download Script
This downloads the French Motor Insurance dataset
"""

import pandas as pd
from sklearn.datasets import fetch_openml
import os

print("Starting data download...")
print("This might take 5-10 minutes depending on your internet speed.")
print("")

# Create data folder if it doesn't exist
os.makedirs('data', exist_ok=True)

# Download Frequency data (how many claims happened)
print("📥 Downloading FREQUENCY data (677,991 policies)...")
freq_data = fetch_openml(data_id=41214, as_frame=True, parser='auto')
df_freq = freq_data.frame

print(f"✅ Frequency data downloaded: {len(df_freq):,} rows")
print("")

# Download Severity data (how much each claim cost)
print("📥 Downloading SEVERITY data...")
sev_data = fetch_openml(data_id=41215, as_frame=True, parser='auto')
df_sev = sev_data.frame

print(f"✅ Severity data downloaded: {len(df_sev):,} rows")
print("")

# Save to CSV files
print("💾 Saving data to CSV files...")
df_freq.to_csv('data/freq_data.csv', index=False)
df_sev.to_csv('data/sev_data.csv', index=False)

print("")
print("=" * 60)
print("🎉 SUCCESS! Data downloaded and saved!")
print("=" * 60)
print("")
print("Files saved to:")
print(f"  - data/freq_data.csv ({len(df_freq):,} rows)")
print(f"  - data/sev_data.csv ({len(df_sev):,} rows)")
print("")
print("What's in this data:")
print("  - IDpol: Policy ID number")
print("  - ClaimNb: Number of claims (0, 1, 2, etc.)")
print("  - Exposure: Fraction of year the policy was active")
print("  - Area: Type of area (A, B, C, D, E, F)")
print("  - VehPower: Vehicle power/performance level")
print("  - VehAge: Age of the vehicle")
print("  - DrivAge: Age of the driver")
print("  - BonusMalus: Bonus-malus level (no-claims discount)")
print("  - VehBrand: Vehicle brand")
print("  - VehGas: Fuel type (Diesel or Regular)")
print("  - Density: Population density where driver lives")
print("  - Region: Geographic region in France")
print("")
print("For severity data:")
print("  - ClaimAmount: Total claim amount in Euros")
print("")
print("You can now move to the next step!")
