---
id: Principles of Data Science
---

## DIY Exercises - 1: Titanic Data Integration & Visualization 🚢

This section focuses on data integration and performing initial analysis by merging two distinct data sources.

### 💾 Data Sources

The analysis requires two files linked by the `TicketType` column:

| File Name | Description | Source Type | Linking Key |
| :--- | :--- | :--- | :--- |
| `passengerData.csv` | Passenger demographics (Age, Sex, Name, etc.). | CSV | `TicketType` |
| `ticketPrices.xlsx` | Ticket prices (Fare) lookup table. | Excel (`.xlsx`) | `TicketType` |

### 🚀 Tasks

#### 1. Data Loading and Preparation
* **Load CSV:** Load `passengerData.csv` into a pandas DataFrame.
* **Load Excel:** Load `ticketPrices.xlsx` into a separate pandas DataFrame.
    * *(Requires the `openpyxl` engine for pandas to read `.xlsx` files.)*

#### 2. Data Merging
* **Merge Operation:** Combine the two DataFrames into a single, comprehensive DataFrame based on the shared key: `TicketType`.

#### 3. Analysis
* **Oldest Passenger:** Identify and display the **name of the oldest passenger(s)** in the newly merged dataset.

#### 4. Visualization (Plotting)
* **Scatter Plot (Age vs. Ticket Price):** Create a scatter plot to show the relationship between **Age** (x-axis) and **Fare** (y-axis).
* **Filtered Scatter Plot:** Create a new scatter plot displaying only the subset of data meeting **all** the following criteria:
    * Passenger **Sex** is `female`.
    * Passenger **Age** is between 40 and 50 (inclusive).
    * Passenger **Fare** (Ticket Price) is greater than or equal to £40.

---

## DIY Exercises - 2: Handling Missing Values 🧩

Using the (slightly modified) Titanic survival data, this section explores how different methods of handling missing data impact the dataset's statistics and visualizations.

### 🛠 Tasks

1.  **Load Data:** Load the **modified Titanic survival data** (CSV file) into a pandas DataFrame.
2.  **Missing Counts:** Find and report the counts of missing values in each column.
3.  **Descriptive Statistics:** Compute and note the **mean** and other descriptive statistics for the numerical columns (e.g., using `.describe()`).
4.  **Imputation by Zero:**
    * Replace the missing values in the `"Age"` and `"Fare"` columns with **0**.
    * Visualize the resulting data in a scatter plot (e.g., Age vs. Fare).
5.  **Imputation by Mean:**
    * **Start with the original data again.**
    * Replace the missing values in the `"Age"` and `"Fare"` columns with the **mean** of each respective column.
    * Visualize the resulting data in a scatter plot.
6.  **Reflection:** Reflect on the differences you observe in the plots created in steps 4 and 5.

---

## DIY Exercises - 3: Data Transformations ✨

This section explores how data transformations can change the shape and range of variables, which is crucial for preparing data for many machine learning models. We will use the **WHO Tuberculosis data**.

### 🛠 Tasks

1.  **Load and Clean:** Download and load the **WHO Tuberculosis CSV data**. You may need to replace initial missing values (e.g., with 0 or the mean) before starting the transformations.
2.  **Initial Visualization:**
    * Choose a numerical column with a non-normal shape (e.g., the right-skewed `"e_prev_100k_hi"`).
    * Visualize the initial distribution using a **histogram**.
3.  **Log Transformation:**
    * Apply a **log transformation** on the chosen column (using `numpy.log`).
    * Visualize the transformed data in a histogram. **Observe and note the changes** in the distribution's shape.
4.  **Min-Max Scaling (Normalization):**
    * Select all numerical columns in the dataset.
    * Apply **Min-Max Scaling** to map all these columns to the standard range of **[0, 1]**.
5.  **Comparison:** Compare the means of the columns *before* and *after* the Min-Max Scaling transformation.
