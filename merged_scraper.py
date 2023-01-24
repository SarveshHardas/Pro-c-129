import pandas as pd

dwarf_planet_df_1 = pd.read_csv("scraped_data.csv")
new_planet_df_1 = pd.read_csv("new_scraped_data.csv")

dwarf_planet_df_1.head()
new_planet_df_1.head()

print(dwarf_planet_df_1)
print(new_planet_df_1)

new_planet_df_1.drop(columns=['mass','distance'], inplace = True)
new_planet_df_1.head()

headers = ["brown_dwarf","constellation","right_ascension","declination","app_mag","distance","spectral_type",
            "mass","radius","discovery_year","Star_names","Distance","Mass","Radius","Luminosity"]
final_planet_df = pd.DataFrame(columns=headers)
final_planet_df = pd.merge(dwarf_planet_df_1,new_planet_df_1)
final_planet_df.head()
print("merged data...")
print(final_planet_df)

final_planet_df.shape
final_planet_df.to_csv("final_scraped_data.csv",index=True, index_label="id")
