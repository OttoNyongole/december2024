import pyreadstat
import pandas as pd

# Replace 'input.sav' with your file path
df, meta = pyreadstat.read_sav("input.sav")

# Save as CSV (replace 'Output.csv' with desired name)
df.to_csv("Output.csv", index=False)
print("File converted successfully!")