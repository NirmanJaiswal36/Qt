import geopandas as gpd
import matplotlib.pyplot as plt

file = gpd.read_file(r"D:\Downloads\dams-rev01-global-shp\GRanD_dams_v1_1.shp")
fig,ax = plt.subplots(figsize = (10,10))
file.plot(ax=ax)
ax.show()