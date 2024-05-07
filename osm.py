import osmnx as ox

p = ox.geocode_to_gdf("Gujarat,India")
p.plot()
