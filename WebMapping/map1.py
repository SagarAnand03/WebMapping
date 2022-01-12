import folium
import pandas

data =pandas.read_csv("Volcano.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 100 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58 , -99.09], zoom_start = 6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcano")
#using for loop to make 2 or more marker 

for lt, ln, el in zip(lat,lon,elev):
    
    #fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+"m",icon=folium.Icon(color_producer(el))))
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius = 6 ,popup=str(el)+"m",fill_color = color_producer(el) , color = 'grey' , fill_opacity =0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data =open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005']< 1000000 else'orange'if 1000000 <= x['properties']['POP2005']< 2000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


#map.add_child(folium.Marker(location=[37.2 , -97.1],popup="hi i am a marker",icon=folium.Icon('red')))


map.save("map1.html")
