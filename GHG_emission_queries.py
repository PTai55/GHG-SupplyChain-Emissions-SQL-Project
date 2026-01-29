import duckdb
import pandas as pd

csv_path = "/workspaces/Global-Debt-SQL-Project/SupplyChainGHGEmissionFactors_v1.3.0_NAICS_byGHG_USD2022.csv"

df = pd.read_csv(csv_path)