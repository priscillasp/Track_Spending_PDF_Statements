import pandas as pd
import os

# Function to read a new CSV file and append it to the existing master CSV file
def update_spending_data(new_csv_path, master_csv_path):
    # Read the new data
    new_data = pd.read_csv(new_csv_path)
    
    # If the master CSV file exists, read it
    if os.path.exists(master_csv_path):
        master_data = pd.read_csv(master_csv_path)
        # Concatenate the new data with the master data
        updated_data = pd.concat([master_data, new_data])
    else:
        # If the master CSV file doesn't exist, the new data is the updated data
        updated_data = new_data
    
    # Convert the 'Date' column to datetime format, specifying the format
    updated_data['Date'] = pd.to_datetime(updated_data['Date'], format='%m/%d/%Y')
    
    # Sort the data by the 'Date' column
    updated_data = updated_data.sort_values(by='Date')
    
    # Convert the 'Date' column back to the original format
    updated_data['Date'] = updated_data['Date'].dt.strftime('%m/%d/%Y')

    # Save the updated data back to the master CSV file
    updated_data.to_csv(master_csv_path, index=False)
    print(f"Updated master CSV file saved to {master_csv_path}")

# Paths to the new CSV file and the master CSV file
new_csv_path = '/Users/priscillamorales/Desktop/CodeSpace/Finances/transaction_may.csv's # Replace with your new CSV file path
master_csv_path = '/Users/priscillamorales/Desktop/CodeSpace/Finances/master_transaction.csv'  # Replace with your master CSV file path

# Update the master CSV file with the new data
update_spending_data(new_csv_path, master_csv_path)
