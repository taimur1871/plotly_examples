import numpy as np
import pandas as pd

# set coordinate range
max_lat = 41.986046
min_lat = 41.056583
max_long = -89.766294
min_long = -92.238217

# random data
fake_data = []

for i in range(10):
    rand_lat = np.random.uniform(min_lat, max_lat)
    rand_long = np.random.uniform(min_long, max_long)
    rand_dist = np.random.uniform(2500.00, 5500.00)
    well_name = 'well' + str(i)
    fake_data.append((well_name, rand_long, rand_lat, rand_dist))

df = pd.DataFrame(fake_data)
df.rename({0:'Well', 1:'Longitude', 2:'Latitude', 3:'Distance'}, axis=1, inplace=True)