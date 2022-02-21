import os
import webbrowser

import pandas as pd
import geopandas
import matplotlib.pyplot as plt
import folium

folium.GeoJsonTooltip

pd.set_option("display.max_columns", 15)
pd.set_option("display.width", 1000)
pd.set_option("display.max_rows", 200)

dataset_path = os.path.join(os.getcwd(), "../data/flavors_of_cacao.csv")
chocodata = pd.read_csv(dataset_path)
chocodata['Company Location'] = chocodata['Company Location'].str.lower()

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world['name'] = world['name'].str.lower()

merge = world.merge(chocodata, how='left', left_on=["name"], right_on=["Company Location"])
company_location_counts = merge.groupby(["name"]).size().reset_index(name='counts')

map = folium.Map()
folium.Choropleth(
    geo_data=world,
    name="chocochoco",
    data=company_location_counts,
    columns=["name", "counts"],
    key_on="feature.properties.name",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Chocolate making companies",
).add_to(map)

map.save(os.path.join(os.getcwd(), "../pages/choco.html"))
webbrowser.open(os.path.join(os.getcwd(), "../pages/choco.html"))
