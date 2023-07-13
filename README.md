# MultiHealth: multi-dimensional urban and environmental exposures and inequality for mental health.

# Aim and objectives
Research regarding the effect of urban and environmental exposures on health outcomes is mostly done in high-income countries because of the abundance of available data. In this project, the first aim was to create small-scale, multi-dimensional urban and environmental spatial indicators that is applicable to mental health research in lower income countries. The second objective was to assess the spatial heterogeneity of the urban and environmental spatial indicators by means of K-means cluster modeling. Lastly, the last objective was to assess the relationship between the spatial indicators and mental health. This was performed using various statistical tests and visual inspections.

# Table of Contents
- [Environment setup](#Environment-setup)
  - [Using Google Colab](#Using-Google-Colab)
  - [Using a local environment](#Using-a-local-environment)
- [Workflow elaboration](#Workflow-elaboration)
  - [Data collection](#Data-collection)
  - [Data modeling](#Data-modeling)
 
## Setting up the environment

### Running in Google Colab
When running the project in Google Colab, make sure you:

<ol>
  <li>Download the 'iso_countries.xlsx' and 'country_iso_path+'cities.xlsx' files</li>
  <li>Upload them to the main '/content' folder, to make sure the path that is created in the notebook is still correct</li>
  <li>install the following packages:</li>
  <li>
    ```python
    %pip install osmnx
    %pip install geemap
    %pip install rasterstats
    %pip install libpysal
    %pip install rioxarray
    %pip install pylandtemp
    ```
  </li>
</ol>
















