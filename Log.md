|Week|Progress
|-|-
|17|Read the provided papers to get familiar with the topic and its context.
|18|- Familiarized myself with OSMNX to work with street networks and retrieve geometries such as bus stops and restaurants.
||- Retrieved the population for 100 by 100 meter grid cells of Greater Manchester by using GEE and OSMNX and using and altering functions from Bart Breekveldt and Finn Wink.
|19|- Worked on it from wednesday afternoon due to personal issues monday and tuesday.
||- Tried to get the amount of intersections per grid by getting a small street network per grid centroid and then extracting the right statistic.
||- The code should now definitely work but it is still running after 16 hours.
||- three-way intersections seemed to be false when calculated with 'basic_stats', but not with 'count_streets_per_node'.
||- Worked on getting the population density per grid bufferzone.
||- Also tried working on computational efficiency optimization, but to no avail. The 'multiprocessing' package does not work with Jupyter Notebook it seems, so I might have to use another IDE or something. 
||- I did read that putting operations in functions and applying the function the each row of the data with apply() works faster than looping through the dataset and doing operations on it that way, so I altered my code for the intersection extractions.
||- Also helped Sander with code for the distance calculations.
||- Will work on it this weekend to try and get more density statistics such as the intersection density per grid and possibly the street density. 
||- population density not working yet, getting negative sums of population per some bufferzones.
||- got the three-way-intersections after 68 hours of execution time, intersection density working now too.
||- street density almost done too, but they seem to be inflated when looking at the 'street_density_km' from ox.stats.basic_stats.
|20|- Updated the construction of the population grid by implementing the right CRS and reprojecting the extracted GeoTIFF for the city_grids_format ||function. Updated the population density, but still getting some negative values due to no-data within buffers. Also updated the network density measures. Besides getting the right area of the network now, density values are still unrealistic.
||- Still having trouble removing the parts from the buffers that overlap with regions containing no population data.
||- The other densities such as the intersection density and street density should be done this weekend.
||- Also working on retrieving more distance variables this weekend.
||- After hours of trying, nearest_node optimalisation done for distance calculations and for the truncation needed to get the street network.
||- I vectorized the code instead of using for-loop iterations. Speed is MUCH faster now.
||- Worked on optimizing the retrieval of street networks via truncation, however, retrieval via truncation seems to be slower than retrieval via the 'ox.graph_from_point' function, no matter what I try.
||- Will also enhance this log tomorrow to make it look better.
||- Spent hours on vectorization optimalisation for distance calculations to for example bus stops. It is MUCH faster now. 100K rows in 26 mins on my crappy ||macbook.
||- Truncation still not, will work on optimizing tomorrow again.
|21|- Finally fixed the distance calculation optimalisations with vectorization and faster loops.
||- Working on optimizing the retrieval of street networks per grid. Truncation is not the play so am focusing on getting the networks per polygon or point.
||- Also trying another CRS (32630) for the population statistics, due to the population size and area per grid bufferzone still looking a bit unrealistic at a lot of points. 
||- CRS 32630 made no difference, so leaving CRS 27700.
||- Finally made lots of progress of extracting the street networks per grid in a relatively fast and efficient way. Now extracting subgraphs from the whole street network.
||- The statistics and area per street network also work. However, the density statistics are still not realistic.
||- Finally got the multiprocessing to work. I created a python venv on my desktop and used VS Code as i had to use regular .py files for multiprocessing to work.
||- Now also got multiprocessing to work with the package multiprocess. It still seems to be not 100% consistent so it might have to do with the IPython kernel.
||- Will run the multiprocesses tomorrow (monday) on the whole dataset, as getting subgraphs and subgraph statistics will now finally be doable time-wise.
|22|- As it turned out, multiprocessing did not work consistently and still does not. The weird thing is that the kernel crashes when initializing the parallelization with all cores, but does not when i start off with less cores and then after that initialize it with all cores. It does not matter whether I use joblib or multiprocessing.
||- Fixed it now temporarily by initializing a parallelization process with 2 threads for just one row before applying it to the whole dataframe. For some reason this initialization is enough. I suppose the 'workers' just have to be initialized somewhat, although this is not present in the documentation or anywhere online. 
||- I am letting the script run the whole day to retrieve the statistics for each grid street network. I will further work on extracting the NDVI and LST values and I will also work on further optimizing the code since the multiprocessing does not seem to work for the distance calculations.
||- Got the multiprocessing working for the distance calculations. I had to parallelize the gpd.distance for the nearest bus stop for each grid polygon.
||- Finally got all the network basic statistics. Converted them to a dataframe, removed the statistics with too many missing values and lastly concatenated them with the main geodataframe. Extracting the NDVI, LST and DEM values should be easy, however I need to find out how to get the mean values of them over a period of time. GEE makes only that part not so easy. 
||- Finally got the average NDVI image of Greater Manchester. Hours upon hours I was figuring out how to get country boundary geometries, clip a GEE image collection with said country, get its mean value (since its a collection over time) and make the exported GEOTIFF file contain values. Getting the country boundaries was eventually done by finding the 'FAO GAUL: Global Administrative Unit Layers 2015, Country Boundaries' dataset and filtering out the UK by means of its GAUL country code. Getting the GEOTIFF to contain values was horrible as it turned out I just had to set the CRS and scale. Because apparently, when you reduce an image collection to a mean for example, the resulting single mean image has a default projection that has 1-degree pixel size in WGS84 EPSG:4326. Also started working on the LST. Will continue that tomorrow as things should go smoothly now.
||- Extracted NDVI, LST and DEM GEOTIFF files and values. Calculated their means per grid bufferzone and added the means to the main geodataframe. Will add NightLight later and will also try to bring in network stats for the rows that have none due to either not having networks or false network area calculations. Hopefully tomorrow the clustering will be done too.
||-  Finished adding all the variables and merged with the distance variables that Sander did. Also tried adding network statistics for the rows that did have none due to not having nearby street networks or no viable area, but this did not help so those rows remain NaN.
|23|- Spatially constrained hierarchical clustering start with a subset of variables of interest.
||- Running into hierarchical clustering problems as it seems that it is not suitable for the totality of our dataset, since hierarchical clustering needs O(n²) memory and O(n³) runtime. Even with 32GB RAM I encounter memory errors. Will try to possibly subset.
||- The hierarchical clustering problems keep persisting. We can try to subset the data to avoid memory issues. We could subset by the variables that have a low correlation together to minimize multicollinearity. Furthermore, now with the added network stats, clustergram with k-means also shows less consistent clusters when looking at the clustergram graph. Will continue tomorrow.
||- Clustering with the spatial hierarchical model works and does not result in memory errors. Also done K-means with clustergram and gaussian mixture with clustergram. Also finalized all the performance metrics. Now working with the calinski-harabasz and davies-bouldin scores, since the silhouette score took hours to compute. I spent a lot of time to possibly parallelize the code but to no avail. At this point I find it very hard to determine which is the best model due to the performance metrics being not really helpful and the plots of the clusters also not helping. It might be best to subset the data, but I have little experience and knowledge about the consequences of this and how to then join the findings. I will continue tomorrow as my brain is pretty fried at this point in time.
||- Cleaner script from the previous clustering script, now with both GMM and Kmeans plots with 9 clusters and removes the rest. 
||- Now did a spatial join with the health dataset, calculated the cluster majority and diversity (not shannon, needs to be done). Lastly visualized them neatly. 
||- Updated version with shannon entropy, health outcome plots and a correlation table between the cluster majority and diversity and health outcome data. 
||- Added kruskal-wallis tests for the nominal cluster majority variable due to it being nominal so not suited for correlations. To get some insights I wanted to see the distributions of the health outcomes for each of the cluster majority values. Also added contingency tables for further inspection.
||- Added histogram density plots for all of the clustervariables within Kmeans cluster 0 and 4, and GMM clusters 0 and 6. This is because I found that pre-mortality and morbidity are highest in Kmeans cluster 0 and in GMM cluster 6, and that mental health issues are highest in Kmeans cluster 4 and GMM cluster.
||- Now also added regular distribution plots to compare with.
||- Now also added additional cluster 2 to the histograms due to cluster 2 also showing higher pre-mortality and morbidity values.
|24|- Did 7, 9 and 11 cluster analyses for both GMM and KMeans. I did both because I did find GMM to contain more convincing mental health results for 9 clusters than K-means. But the main problem is that for 7 and 11 clusters, both models produce majority cluster labels to which not even 5 neighborhoods are attributed to which are not very useful.
||- As for the writing, I will continue and finish the introduction tomorrow. I had some troubles with hayfever attacks yesterday and today (and the past weekend..), and I had to take my cat to the vet today due to him having a bladder infection, together this took quite some time (and quite some energy) unfortunately.
