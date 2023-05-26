
# ### Packages
# system packages
import sys
import time
import warnings
import os
from collections import Counter

# non-geo numeric packages
import multiprocessing.pool as mp
import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import product, combinations
import pandas as pd

# network and OSM packages
import networkx as nx
import osmnx as ox
city_geo = ox.geocoder.geocode_to_gdf

# Earth engine packages
import ee
import geemap

# General geo-packages
import fiona
from rasterstats import zonal_stats
from pyproj import CRS
import libpysal
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
import rioxarray
import geopandas as gpd
import shapely
from shapely import geometry
from shapely.geometry import Point, MultiLineString, LineString, Polygon, MultiPolygon

# latest gdf
popgridmanchester = gpd.read_file('\Scriptie_repo\MultiHealth_J\popgridmanchester3.gpkg')

# load grid buffer gdf
bufferintersect_gdf = gpd.read_file('C:/Scriptie_repo/MultiHealth_J/bufferintersect_gdf.gpkg')

# Load full manchester street network
Gproj = ox.load_graphml('/Scriptie_repo/MultiHealth_J/network.graphml')

# get subgraphs for each grid instead of extracting the network per grid.
# use the nodes from the whole street network of Greater Manchester, calculate their intersections
# with buffer polygons and create the subgraph based on those nodes.
def get_subgraph(Gproj, Gproj_nodes, polygon):
    return Gproj.subgraph(Gproj_nodes[Gproj_nodes.intersects(polygon)].index)

# get nodes from the Gproj
Gproj_nodes = ox.graph_to_gdfs(Gproj, edges=False)

# buffer polygon variables
buffersub = bufferintersect_gdf[0:9999]
vars = buffersub['geometry']

# use multiprocessing to split the task of calculating the subgraphs over the 8 logical cores on my pc (threads)
if __name__ == '__main__':
    with mp.ThreadPool(8) as p:
        start_time = time.time()
        subgraph_list = p.starmap(get_subgraph, ((Gproj, Gproj_nodes, polygon) for polygon in vars))
        p.close()
        p.join()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")