\# 🚴 Lab 02, Exercise 1: London Bike Hires Usage in Python



This lab exercise focuses on loading, cleaning, transforming, and visualizing usage patterns of the London Bike Hire scheme. We analyze 24 hours of data collected every 10 minutes from hundreds of docking stations to gain insights into public transport behavior.



The lab demonstrates critical skills in modern data science using the \*\*Pandas\*\* library for data manipulation and \*\*Matplotlib\*\* and \*\*Altair\*\* for visualization.



---



\## 💾 Data Sources



The exercise requires two local files:



1\.  \*\*`bikeStations.tsv`\*\*: A tab-separated file containing static information for each station (`id`, `name`, `lat`, `lon`).

2\.  \*\*`last24h.csv`\*\*: A CSV file containing time-series data of bike availability (`stationId`, `availableBikes`, `availableDocks`, `t`).



---



\## 🚀 Part 1: Data Loading and Transformation (Pandas)



This section focuses on preparing the raw data for analysis using core Pandas functionalities.



\### Key Steps Covered



1\.  \*\*Data Loading:\*\* Loading both `.tsv` and `.csv` files into separate Pandas DataFrames.

2\.  \*\*Data Merging:\*\* Merging the two DataFrames on the common key (`stationId`/`id`) to integrate location and name information with the time-series data.

3\.  \*\*Time Series Conversion:\*\* Converting the raw time column (`t`) into a datetime object and extracting the \*\*hour\*\* (`hr`).

4\.  \*\*Feature Engineering:\*\* Calculating a new column for total station capacity (`availableBikes + availableDocks`).

5\.  \*\*Data Aggregation:\*\* Grouping the 10-minute data by station and hour to calculate the \*\*mean number of available bikes per hour\*\*.

6\.  \*\*Pivoting/Melting:\*\* Demonstrating how to transform data between \*\*"wide"\*\* (for Matplotlib) and \*\*"long"\*\* (tidy format for Altair) structures using `pivot` and `pd.melt`.



---



\## 📈 Part 2: Comparative Data Visualization



This section compares two different Python visualization libraries: Matplotlib (which prefers wide data) and Altair (which requires tidy, long data) to visualize temporal and spatial patterns.



\### Task 2.1: Matplotlib for Time-Series Analysis



\* \*\*Plotting Time-Series:\*\* Using the \*\*wide\*\* DataFrame structure to superimpose a 24-hour timeline of available bikes for \*\*every station\*\* on a single Matplotlib plot.

\* \*\*Analysis:\*\* Answering questions regarding the use of `transpose()` and interpreting the evident temporal patterns (e.g., morning/evening peaks).

\* \*\*Refinement:\*\* Improving the plot aesthetics by adjusting line transparency and filtering for specific geographic regions (e.g., 'Kings Cross').

\* \*\*Normalization:\*\* Modifying the data to show the \*\*proportion of capacity full\*\* instead of raw bike counts.



\### Task 2.2: Altair for Time-Series Analysis



\* \*\*Tidy Data Requirement:\*\* Using the \*\*long\*\* (melted) DataFrame, which is the required format for Altair.

\* \*\*Feature Extraction:\*\* Extracting the geographic \*\*area\*\* from the station name to use as a new categorical variable.

\* \*\*Visualization:\*\* Creating a similar superimposed line plot using `alt.Chart().mark\_line()` to visualize available bikes vs. hour.



\### Task 2.3: Altair for Spatial Analysis (Glyph Maps)



\* \*\*Map Creation:\*\* Using Altair to create a \*\*spatial map\*\* where each station is represented by a circle (`mark\_circle`).

\* \*\*Visual Encoding:\*\* Encoding multiple variables onto the map:

&nbsp;   \* \*\*Position:\*\* `latitude` and `longitude`.

&nbsp;   \* \*\*Size:\*\* Station `capacity`.

&nbsp;   \* \*\*Color:\*\* `average(propFull)` (average proportion of capacity full over the 24 hours).

\* \*\*Advanced Filtering:\*\* Using a \*\*diverging color scale\*\* (Red-Blue) to highlight stations below/above 50% capacity.

\* \*\*Spatio-Temporal Faceting:\*\* Creating \*\*faceted maps\*\* grouped into 4-hour bins to observe how spatial patterns (where bikes are full vs. empty) change throughout the day.

