import pandas as pd

# Load the dataset
def load_data(file_path):
    return pd.read_csv(file_path)

# Clean formatting of specified columns
def fix_formatting(df, columns_to_clean):
    for col in columns_to_clean:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: x.strip('"') if pd.notna(x) else x)
    return df

# Main cleaning pipeline
def clean_data(df):
    # Drop unnecessary columns
    df = df.drop('country_code', axis=1)

    # Convert created_at to datetime
    df['created_at'] = pd.to_datetime(df['created_at'])

    # Fill missing cities with 'Unknown'
    df['city'] = df['city'].fillna('Unknown')

    # Clean specific columns
    columns_to_clean = ['furnished', 'total_size', 'registration_possible', 'washing_machine', 'tv', 'balcony', 'garden', 'terrace']
    df = fix_formatting(df, columns_to_clean)

    # Convert total_size to numeric
    df['total_size'] = pd.to_numeric(df['total_size'], errors='coerce')

    # Remove invalid rows
    df = df[~((df['city'] == 'Unknown') & df['category'].isna())]
    df = df[~((df['category'].isin(['Shared Room', 'Private Room'])) & ((df['price'] < 150) | (df['price'] > 1500)))]
    df = df[~(df['price'] < 150)]

    # Adjust total_size for specific conditions
    df['adjusted_size'] = df.apply(
        lambda row: row['total_size'] / 10 if (row['price'] < 1000 and 100 < row['total_size'] < 1000 and row['category'] != 'Shared Room')
        else (row['total_size'] / 100 if (row['price'] < 1000 and row['total_size'] > 1000 and row['category'] != 'Shared Room')
        else row['total_size']),
        axis=1
    )

    # Remove rows with invalid adjusted sizes and extreme prices
    df = df[~(df['adjusted_size'] < 0) | df['adjusted_size'].isnull()]
    df = df[~(df['price'] > 15000)]

    return df

# Save the cleaned dataset to a new CSV file
def save_data(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_file = "ha_data_assessement.csv"
    output_file = "fixed.csv"

    # Execute the cleaning process
    data = load_data(input_file)
    cleaned_data = clean_data(data)
    save_data(cleaned_data, output_file)

    print(f"Data cleaning completed. Cleaned data saved to {output_file}.")