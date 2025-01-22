# Telecom Churn Analysis  
### (Power BI + SQL + Machine Learning for Churn Prediction)

## Overview
Customer churn poses a significant challenge for telecom companies. It refers to the situation where customers discontinue their subscriptions or switch to competitors. Predicting churn in advance enables businesses to take proactive steps to retain customers, thereby reducing revenue loss.

This project utilizes Power BI, SQL, and Machine Learning to analyze and predict churn, helping telecom companies develop effective customer retention strategies.

[**Power BI Dashboard Click Here**](https://app.powerbi.com/view?r=eyJrIjoiZDU1ZjA4YmMtMDhkOC00ZWU3LWJlYjYtYzIxZmQ3NGZjYTIyIiwidCI6ImQxZjE0MzQ4LWYxYjUtNGEwOS1hYzk5LTdlYmYyMTNjYmM4MSIsImMiOjEwfQ%3D%3D)

---

## Dataset
The project dataset includes a database copy for analysis and model building, available in the `dataset/dataset.sql` file.

---

## Project Structure
Below is the breakdown of the project's structure:  

### 1. **Dataset**
- `dataset.sql` contains three tables:  
  - **`stg_churn`**: Includes data on customers who churned and those who didn't.  
  - **`new_customers`**: Contains details of newly joined customers.  
  - **`prod_churn`**: This table is automatically imported when running `Churn_Rate_Analysis_EDA.ipynb` for data cleaning, EDA, and preprocessing. Avoid manually importing this table.  

### 2. **Scripts and Notebooks**
- **`db_utils.py`**: Manages the database connection setup.  
- **`Churn_Rate_Analysis_EDA.ipynb`**: Performs data cleaning, exploratory data analysis (EDA), and preprocessing.  
- **`Churn_Rate_Analysis_Model_Building.ipynb`**: Builds the machine learning model for churn prediction.  

### 3. **Dashboard**
- **`Churn Rate Analysis.pbix`**: Power BI dashboard file for visualizing churn insights.  

---

## Key Highlights
- The `prod_churn` table data is automatically loaded during EDA and preprocessing, streamlining the workflow.  
- The project integrates SQL for data preparation, Power BI for visualization, and a machine learning model for predictive analysis.  

---
