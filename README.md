# MultiHealth: multi-dimensional urban and environmental exposures and inequality for health in multiple cities.

Research regarding the effect of urban and environmental exposures on health outcomes is mostly done in high-income countries because of the abundance of available data. In this project, the aim is to create multi-dimensional urban and environmental spatial indicators applicable to health research in lower income countries.

Week 19:
- Worked on it from wednesday afternoon due to personal issues monday and tuesday.
- Tried to get the amount of intersections per grid by getting a small street network per grid centroid and then extracting the right statistic. The code should now definitely work but it is still running after 16 hours.
- Worked on getting the population density per grid bufferzone, should also work now.
- Also tried working on computational efficiency optimization, but to no avail. The 'multiprocessing' package does not work with Jupyter Notebook it seems, so I might have to use another IDE or something. I did read that putting operations in functions and applying the function the each row of the data with apply() works faster than looping through the dataset and doing operations on it that way, so I altered my code for the intersection extractions.
- Also helped Sander with code for the distance calculations.
- Will work on it this weekend to try and get more density statistics such as the intersection density per grid and possibly the street density. 
