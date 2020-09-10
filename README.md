## Class Project on analyzing data from a variety of sources to solve realistic problems from science, engineering, and business
#### Carbon Dioxide Emissions over 40 Years in the U.S.
#### Spring 20

## Get two data files online
1. Get the population data [NST-EST2015-01.xlsx](https://web.archive.org/web/20160130223507/http:/www.census.gov:80/popest/data/state/totals/2015/index.html) 

Under the title, Annual Estimates of the Resident Population for the United States, Regions, States, and Puerto Rico: April 1, 2010 to July 1, 2015 (NST-EST2015-01), you can find a link to download a .xlsx file (18K). The link to the .csv file was removed so I decided to use .xlsx file.

2. Get the CO2 emission data [EMISS.txt](https://www.eia.gov/opendata/bulkfiles.php#d-use-common-core-and-extensible-metadata) 

On the “Latest bulk download files:” section, you can find “CO2 Emissions” where you can download the data as a .zip file and contains a single .txt file (6.4 MB) of the same name. 

Have both files downloaded in the same folder as the two python files `project.py` and `mlproject.py`. 


## Python modules and library you need to install
> pandas

> matplotlib.pyplot

> numpy

> json

> sklearn


## Instructions
Run python files on your terminal:

> python `project.py`: Two graphs addressing the 1st and the 2nd research problems will be saved on the same folder named **WA_trans_ind.png** and **US_fuels.png**. It also prints out numerical results for the 2nd problem on your terminal. 

> python `mlproject.py`: The graphs addressing the 3rd research problem will be saved on the same folder named **mse_maxtreedepth.png**. It also calculates and prints the test mean squared error based on the the chosen max tree depth determined by the graph.
