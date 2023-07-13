# MultiHealth: multi-dimensional urban and environmental exposures and inequality for mental health.

# Aim and objectives
Research regarding the effect of urban and environmental exposures on health outcomes is mostly done in high-income countries because of the abundance of available data. In this project, the first aim was to create small-scale, multi-dimensional urban and environmental spatial indicators that is applicable to mental health research in lower income countries. The second objective was to assess the spatial heterogeneity of the urban and environmental spatial indicators by means of K-means cluster modeling. Lastly, the last objective was to assess the relationship between the spatial indicators and mental health. This was performed using various statistical tests and visual inspections.

# Table of Contents
- [Environment setup](#Environment-setup)
  - [Using a local environment](#Using-a-local-environment)
  - [Using Google Colab](#Using-Google-Colab)
- [Workflow elaboration](#Workflow-elaboration)
  - [Data collection](#Data-collection)
  - [Data modeling](#Data-modeling)
 
## Environment setup

### Using a local environment
When running the project in a local environment, make sure you:

<ol>
  <li>Create an empty working directory for the 'gridcreation.ipynb' and healthenvironment_relation.ipynb' notebook files and the 'iso_countries.xlsx' and 'country_iso_path+'cities.xlsx' files</li>
  <li>Download the required environment YAML file from the repository and install it by opening the windows command prompt or mac terminal and execute the following command:
  
  ```
  conda env create -f multihealth-env.yml
  ```
 
  </li>
  <li>Activate the newly created conda environment by executing the following command: 
  
  ```
  conda activate multihealth-env
  ```

  </li>
  <li>Alternatively, if you are not a fan of conda and know how to work with a local Python virtual environment, you can use the requirements.txt file from the repository for the installation of the required packages and put this file in the created working directory. Then, open a command prompt or a mac terminal, navigate to the working directory by executing this command:
  
  ```
  cd path/to/working/directory
  ```

Then, to install the required packages from the text file, execute this command:
  
  ```
  pip install -r requirements.txt
  ```

  </li>
</ol>

### Using Google Colab
When running the project in Google Colab, make sure you:

<ol>
  <li>Download the 'iso_countries.xlsx' and 'country_iso_path+'cities.xlsx' files from this repository</li>
  <li>Upload them to the main '/content' folder, to make sure the path that is created in the notebook is still functional</li>
  <li>Install the following packages before importing the listed packages in the notebook:
    
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
















