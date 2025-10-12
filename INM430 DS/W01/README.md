---
id: Principles of Data Science
---

# Week 01: DIY Python & NumPy Exercises

## Part 1: Elementary Python Tasks (CSV File Handling)

These tasks focus on reading and processing data from a chosen CSV file using core Python features (no external libraries like Pandas initially).

### 1. File Reading and Counting
* Count the total **number of rows** in the CSV file (excluding the header).

### 2. Column Average Calculation (Loop-based)
* Pick a column containing numeric data (e.g., `"e_prev_num_lo"`).
* Calculate the **average value** for this column using a standard Python `for` loop (not a built-in library function like `avg()`).

### 3. Conditional Average Calculation
* Repeat the average calculation from **step 2**, but this time, find the averages specifically for the years **1990** and **2011**.
* Note any observed difference between the two yearly averages.

---

## Part 2: Data Manipulation with NumPy and Matplotlib

These tasks focus on array creation, mathematical operations, and basic visualization using the **NumPy** and **Matplotlib** libraries.

### 1. NumPy Array Creation
* Create an array of integers ranging from **5 to 15** (inclusive).
* Create an array containing **7 evenly spaced numbers** between 0 and 23 (inclusive/exclusive as appropriate).
* Generate an **artificial NumPy array** with values between **-1 and 1** that follows a **uniform data distribution**.

### 2. Data Visualization
* Visualize one of the generated arrays in a **histogram** using `matplotlib`.

### 3. Euclidean Distance
* Create **two random NumPy arrays** each with **10 elements**.
* Calculate the **Euclidean distance** between these two arrays using basic arithmetic operators (addition, subtraction, multiplication) and the NumPy square root function (`numpy.sqrt`).
