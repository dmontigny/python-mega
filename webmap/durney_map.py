import folium
import pandas as pd

map = folium.Map(location=[28.228137, -82.716516], zoom_start=6)  #, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="Dave's Map!")
fg.add_child(folium.Marker([28.228137, -82.716516], popup="I live here!", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker([29.928102, -81.435126], popup="Creta Massenge"))
fg.add_child(folium.Marker([27.7902203, -82.722427], popup="Carol Hixon"))
fg.add_child(folium.Marker([27.7902171, -82.7228409], popup="Robert White"))

data = pd.read_csv("Volcanoes_USA.txt")
print(data)

map.add_child((fg))

map.save("map1.html")

