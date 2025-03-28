import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analyze_sales_data(file_path):
    """
    Analyzes sales data from a CSV file and creates simple visualizations.
    
    Parameters:
    file_path (str): Path to the CSV file containing sales data
    """
    try:
        # Load the data
        print("Loading sales data...")
        sales_data = pd.read_csv(file_path)
        
        # Display basic information about the dataset
        print("\nData Overview:")
        print(f"Total records: {len(sales_data)}")
        print(f"Columns: {', '.join(sales_data.columns)}")
        
        # Check if common sales columns exist
        required_columns = ['date', 'product', 'amount']
        missing_columns = [col for col in required_columns if col.lower() not in [c.lower() for c in sales_data.columns]]
        
        if missing_columns:
            print(f"\nWarning: Missing expected columns: {', '.join(missing_columns)}")
            print("Please ensure your CSV has date, product, and amount columns (column names may differ)")
            return
            
        # Map the actual column names to expected column names
        date_col = next((col for col in sales_data.columns if 'date' in col.lower()), None)
        product_col = next((col for col in sales_data.columns if 'product' in col.lower() or 'item' in col.lower()), None)
        amount_col = next((col for col in sales_data.columns if 'amount' in col.lower() or 'sales' in col.lower() or 'revenue' in col.lower()), None)
        
        # Basic statistics
        print("\nSales Statistics:")
        print(f"Total sales: ${sales_data[amount_col].sum():,.2f}")
        print(f"Average sale: ${sales_data[amount_col].mean():,.2f}")
        print(f"Highest sale: ${sales_data[amount_col].max():,.2f}")
        print(f"Lowest sale: ${sales_data[amount_col].min():,.2f}")
        
        # Sales by product
        product_sales = sales_data.groupby(product_col)[amount_col].sum().sort_values(ascending=False)
        print("\nTop 5 Products by Sales:")
        for product, amount in product_sales.head(5).items():
            print(f"{product}: ${amount:,.2f}")
            
        # Visualizations
        print("\nCreating visualizations...")
        
        # 1. Bar chart of top products
        plt.figure(figsize=(10, 6))
        product_sales.head(5).plot(kind='bar')
        plt.title('Top 5 Products by Sales')
        plt.xlabel('Product')
        plt.ylabel('Total Sales ($)')
        plt.tight_layout()
        plt.savefig('top_products.png')
        
        # 2. Time series of daily sales (if date column exists)
        if date_col:
            # Convert to datetime
            sales_data[date_col] = pd.to_datetime(sales_data[date_col])
            
            # Group by date and calculate daily sales
            daily_sales = sales_data.groupby(sales_data[date_col].dt.date)[amount_col].sum()
            
            plt.figure(figsize=(12, 6))
            daily_sales.plot(kind='line')
            plt.title('Daily Sales Over Time')
            plt.xlabel('Date')
            plt.ylabel('Total Sales ($)')
            plt.tight_layout()
            plt.savefig('daily_sales.png')
        
        print("\nAnalysis complete! Visualizations saved as:")
        print("- top_products.png")
        if date_col:
            print("- daily_sales.png")
            
    except Exception as e:
        print(f"Error analyzing sales data: {e}")

# Example usage
if __name__ == "__main__":
    file_path = input("Enter the path to your sales data CSV file: ")
    analyze_sales_data(file_path)
