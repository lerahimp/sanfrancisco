# San Francisco.

Data Mining course project based on the data sets from https://data.sfgov.org/

# The Aim

- Find patterns among pedestrian-involved accidents versus vehicle-to-vehicle accidents based on weather, road conditions, time of day, and lighting.

# Reasoning

- Be able to provide more specific recommendations to lessen traffic crashes with injuries based on whether it involves vehicle-vehicle or vehicle-pedestrian collisions.

# Dataset Used

- https://data.sfgov.org/Public-Safety/Traffic-Crashes-Resulting-in-Injury/ubvf-ztfx/about_data

# Preprocessing

Framework Used - KNIME

- CSV Reader: Read csv dataset
- Column Filter: Filter irrelevant columns (e.g., accident_year, officer_id, etc.)
- Rule-based Row Filter: Filter rows where data is "Not Stated", and group types of collisions
- String to Date&Time: Transform time of accident to date and time format
- Date&Time Part Extractor: Extract date and time
- Math Formula: Calculate minutes since midnight from when crash happened
- Column filter: Filter columns created from calculation of minutes since midnight
- Rule Engine: Group collision types and rename them, group days of the week to weekend or weekday
- Missing Value: Remove row with missing values
- Rule-based Row Filter: Filter more rows where data is "Not Stated" or "Other"
- One to Many: One-hot encoding to transform categorical data into a binary representation
- Equal Size Sampling: Make the sample size for vehicle-vehicle and vehicle-pedestrian equal
- Column Filter: Remove unnecessary rows created from one to many node
- Column Renamer: Rename columns for more consistency and readability
- CSV Writer: Write new dataset into CSV

# How to Replicate Setup

- Download dataset https://data.sfgov.org/Public-Safety/Traffic-Crashes-Resulting-in-Injury/ubvf-ztfx/about_data
- Download .knfw (KNIME) file included in the repository
- Load dataset into the CSV Reader of the .knfw file
- Final dataset required is already in the repository, however for full replication, follow steps above
- In the terminal, run 'pip install pandas numpy matplotlib scikit-learn'
- Run and execute cluster_analysis.py

# Findings

- The highest silhouette score of 0.52 was achieved with 2 clusters. This score is not ideal, but reasonable. It suggests that there may be some overlap between the clusters and increased dimensionality of data.
- Cluster 0 has an average accident time of about 844 minutes since midnight (2:04 pm), mostly occurred in clear weather, during the day, and on a weekday.
- Cluster 1 has an average accident time of about 835 minutes since midnight (1:55 pm), mostly occurred in rainy and cloudy weather, during the day, and on a weekday.
- Cluster 0 has a roughly equal split between vehicle-pedestrian and vehicle-vehicle collisions, with a little bit more vehicle-vehicle collisions.
- Cluster 1 has a higher proportion of vehicle-pedestrian collisions.

# Conclusions

- Since accidents in cluster 0 occur more in clear weather, this indicates that factors outside of weather and road conditions may be contributing to the accidents.
- In cluster 1, there is a higher proportion of vehicle-pedestrian collisions, with a lot more crashes occurring during rainy and cloudy weather. This suggests that safety measures targeted towards pedestrians in poor weather need to be improved.
- Since most of these accidents occur during the day and on a weekday, it can be assumed that this is because of rush-hour and increased presencce of vehicles on roads.
