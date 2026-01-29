import duckdb
import pandas as pd

csv_path = "/workspaces/Global-Debt-SQL-Project/SupplyChainGHGEmissionFactors_v1.3.0_NAICS_byGHG_USD2022.csv"

df = pd.read_csv(csv_path)
# connection = duckdb.connect()
# connection.register("df", df)

#print(duckdb.sql("select * from df limit 5").df())

df = df.rename(columns={
    "2017 NAICS Code": "naics_code",
    "2017 NAICS Title": "naics_title",
    "GHG": "ghg",
    "Unit": "unit",
    "Supply Chain Emission Factors without Margins": "factors_without_margins",
    "Margins of Supply Chain Emission Factors": "margins_factors",
    "Supply Chain Emission Factors with Margins": "factors_with_margins",
    "Reference USEEIO Code": "useeio_code"
})

# connection.execute("DROP VIEW IF EXISTS supply_chain_ghg")
# connection.execute("""
# CREATE VIEW supply_chain_ghg AS 
# SELECT 
#     "2017 NAICS Code" AS naics_code,
#     "2017 NAICS Title" AS naics_title,
#     "GHG" AS ghg,
#     "Unit" AS unit,
#     CAST("Supply Chain Emission Factors without Margins" AS DOUBLE) AS factors_without_margins,
#     CAST("Margins of Supply Chain Emission Factors" AS DOUBLE) AS margins_factors,
#     CAST("Supply Chain Emission Factors with Margins" AS DOUBLE) AS factors_with_margins,
#     "Reference USEEIO Code" AS useeio_code
#     FROM df;""")

print(duckdb.sql("SELECT naics_code, naics_title, ghg, unit, factors_with_margins FROM df ORDER BY factors_with_margins DESC LIMIT 25;").df())