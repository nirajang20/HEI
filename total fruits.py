import pandas as pd

def process_csv(input_file, output_file):
    """
    Read a CSV file, perform calculations, and save with new 'total_fruits' column.
    Caps the 'total_fruits' values at a maximum of 5 (no lower limit).
    
    Args:
        input_file (str): Path to the input CSV file
        output_file (str): Path to save the processed CSV file
    """
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Perform the calculations
    df['total_fruits'] = ((df['F_TOTAL'] / (df['kcal'] / 1000)) / 0.8) * 5
    
    # Cap values at 5 (no lower limit)
    df['total_fruits'] = df['total_fruits'].where(df['total_fruits'] <= 5, 5)
    
    # Round to 2 decimal places
    df['total_fruits'] = df['total_fruits'].round(2)
    
    # Save to new CSV file
    df.to_csv(output_file, index=False)
    print(f"Processed file saved to {output_file}")

# Example usage
if __name__ == "__main__":
    input_csv = "/Users/marsguy/Desktop/Research/CH HEI/FPED_CH_KCAL.csv"
    output_csv = "/Users/marsguy/Desktop/Research/CH HEI/FPED_CH_KCAL-total_fruits.csv"
    process_csv(input_csv, output_csv)