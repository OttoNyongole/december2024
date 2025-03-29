import pyreadstat
import pandas as pd

# Replace 'input.sav' with your file path
df, meta = pyreadstat.read_sav("NdolaDataset (2).sav")

# Save as CSV (replace 'NdolaDataset.csv' with desired name)
df.to_csv("NdolaDataset.csv", index=False)
print("File converted successfully!")