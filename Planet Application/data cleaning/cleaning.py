from os import access
import pandas as pd

df = pd.read_csv("data.csv")

del df["pl_orbpererr1"]
del df["pl_orbper"]        


df = df.rename({
    "pl_hostname":"solar_system_name",
    "pl_discmethod":"planet_discovery_method"
},axis = "columns")


df.to_csv("final.csv")