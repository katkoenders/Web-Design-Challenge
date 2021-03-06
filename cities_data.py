import pandas as pd
import os
# File to Load (Remember to Change These)
file_to_load = os.path.join("WebVizualizations","Resources","cities.csv")
# Read Purchasing File and store into Pandas data frame
cities_data = pd.read_csv(file_to_load)
print(cities_data)
cities_data.to_html('table.html', index=False, classes=['table','table-striped','table-hover'])