# Packages
# system packages
import gc
import sys
import time
import warnings
import os
from collections import Counter

# non-geo numeric packages
from joblib import Parallel, delayed
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

# loading files
# latest gdf
popgridmanchester = gpd.read_file('/Users/julia/Scriptie_repo/Multihealth_J/popgridmanchester3.gpkg')

# load grid buffer gdf
bufferintersect_gdf = gpd.read_file('/Users/julia/Scriptie_repo/Multihealth_J/bufferintersect_gdf.gpkg')

# Load full manchester street network
Gproj = ox.load_graphml('/Users/julia/Scriptie_repo/Multihealth_J/network.graphml')

# get subgraphs for each grid instead of extracting the network per grid.
# use the nodes from the whole street network of Greater Manchester, calculate their intersections
# with buffer polygons and create the subgraph based on those nodes.
def get_subgraph(Gproj, Gproj_nodes, polygon):
    return Gproj.subgraph(Gproj_nodes[Gproj_nodes.intersects(polygon)].index)

# get nodes from the Gproj
Gproj_nodes = ox.graph_to_gdfs(Gproj, edges=False)

# buffer polygon variables
buffersub = bufferintersect_gdf[0:999].geometry

# use multiprocessing to split the task of calculating the subgraphs over the 8 logical cores on my pc (threads)
if __name__ == '__main__':
    start_time = time.time()
    subgraph_list = Parallel(n_jobs=-1, backend="threading")(delayed(get_subgraph)(Gproj, Gproj_nodes, polygon) for polygon in buffersub)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

# getting the basic stats of every subgraph by turning the subgraph into a gdf, turning that into 
# one polygon and getting its area
def get_subgraph_area(subgraph):
    try:
        return ox.graph_to_gdfs(subgraph, nodes=True, edges=False).unary_union.convex_hull.area
    except ValueError:
        return 0

# use multiprocessing
if __name__ == '__main__':
    start_time = time.time()
    subgraph_area = Parallel(n_jobs=-1, backend="threading")(delayed(get_subgraph_area)(subgraph) for subgraph in subgraph_list)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

# get the statistics from each subgraph and area and accounting for the errors that might occur due
# to a graph having no edges and giving a ValueError or due to the area being zero because the area
# is not able to be calculated from a graph with no edges!
def get_stats(subgraph, area):
    try:
        return ox.stats.basic_stats(subgraph, area)
    except (ValueError, ZeroDivisionError):
        return 0

# use multiprocessing
if __name__ == '__main__':
    start_time = time.time()
    subgraph_stats = Parallel(n_jobs=-1, backend="threading")(delayed(get_stats)(subgraph, area) for subgraph, area in zip(subgraph_list, subgraph_area))
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")