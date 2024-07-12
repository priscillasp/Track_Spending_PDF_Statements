# Convert PDF to CSV and Analyze Spending

This repository helps you extract transaction data from PDF bank statements, process it, and save it to a CSV file. The CSV file is then cleaned and analyzed to categorize income and spending. The process involves three main steps:

1. **Convert PDF to CSV**: Extract transaction data from a PDF bank statement and save it to a CSV file.
2. **Update Master Transaction CSV**: Append new transaction data to a master CSV file and sort the data by date.
3. **Analyze Spending**: Visualize and analyze your overall spending habits using a Jupyter notebook.

## Requirements

- Python 3.11.8
- PyPDF2
- pandas
- matplotlib
- seaborn
- Jupyter Notebook

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/priscillasp/Track_Spending_PDF_Statements.git
    cd Track_Spending_PDF_Statements
    ```

2. Install the required packages:
    ```
    pip install PyPDF2 pandas matplotlib seaborn jupyter
    ```

## Usage

### Step 1: Convert PDF to CSV

1. Open the Jupyter notebook `Convert_PDF_to_CSV.ipynb`.
2. Import your bank statement PDF by replacing the placeholder in the notebook with the path to your PDF file.
3. Update the category if else loops to match your bank statement information. 
3. Run all cells in the notebook to process the PDF, clean the data, and analyze spending.
4. The processed data will be saved as a CSV file and visualizations will be generated to summarize spending by category.

### Step 2: Update Master Transaction CSV

1. Place your new bank statement CSV file in the project directory.
2. Run the `update_transactions.py` script to update the master transaction CSV file.

#### Example Usage

1. Open a terminal and navigate to the project directory.
2. Run the following command:
    ```sh
    python update_transactions.py path_to_your_new_statement.csv path_to_your_master_statement.csv
    ```
    Replace `path_to_your_new_statement.csv` with the actual path to your new statement CSV file, and `path_to_your_master_statement.csv` with the actual path to your master transaction CSV file.

The script will:
- Read the new transaction data.
- Append it to the master transaction CSV file.
- Sort the transactions by date.
- Save the updated master transaction CSV file.

### Step 3: Analyze Spending

1. Open the `spending_analysis.ipynb` Jupyter notebook.
2. Run the notebook cells to generate visualizations and insights into your spending habits.

#### Example Usage

1. Open a terminal and navigate to the project directory.
2. Run the following command to start Jupyter Notebook:
    ```sh
    jupyter notebook
    ```
3. In the Jupyter Notebook interface, open `spending_analysis.ipynb`.
4. Execute the cells to see various visualizations and summaries of your spending data.

## File Descriptions

### Convert_PDF_to_CSV.ipynb
A Jupyter notebook that extracts transaction data from a PDF bank statement, processes it, and saves it to a CSV file. The notebook also visualizes the processed data using a pie chart to show spending by category.

### update_transactions.py
A Python script that updates the master transaction CSV file with new transaction data. It ensures that the dates are in the correct format (`mm/dd/yyyy`) and sorts the transactions by date.

### spending_analysis.ipynb
A Jupyter notebook that analyzes your spending data. It includes visualizations such as:
- Total Spending by Category (Bar Plot)
- Monthly Spending Trend (Bar Plot)
- Top 10 Largest Expenses (Bar Plot)
- Spending by Category (Pie Chart)
- Summary Statistics (Total Spending, Average Spending, Highest Single Expense)

