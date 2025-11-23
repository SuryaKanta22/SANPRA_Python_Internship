import pandas as pd
import re

def clean_phone_number(phone):
    """
    Normalizes phone numbers to a standard 10-digit format (XXX-XXX-XXXX) if possible.
    Returns the original string if it cannot be formatted or is invalid.
    """
    if pd.isna(phone):
        return ""
    
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', str(phone))
    
    # Handle 10-digit numbers
    if len(digits) == 10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    # Handle 11-digit numbers starting with 1 (US country code)
    elif len(digits) == 11 and digits.startswith('1'):
        return f"{digits[1:4]}-{digits[4:7]}-{digits[7:]}"
    
    return str(phone)

def main():
    with open('debug_log.txt', 'w') as f:
        f.write('Script started\n')
    print("Script started")
    input_file = 'client_data.csv'
    output_file = 'cleaned_client_data.csv'
    
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Standardize names to Title Case
        if 'Name' in df.columns:
            df['Name'] = df['Name'].astype(str).str.title()
        
        # Normalize phone numbers
        if 'Phone' in df.columns:
            df['Phone'] = df['Phone'].apply(clean_phone_number)
        
        # Check for missing emails and handle them
        # We will flag them in a new column 'Email_Status' and keep the row
        # Alternatively, we could drop them. The requirement says "check for missing emails".
        # Let's print a report and fill NaNs with empty string.
        if 'Email' in df.columns:
            missing_emails = df['Email'].isna().sum()
            print(f"Found {missing_emails} rows with missing emails.")
            df['Email'] = df['Email'].fillna('')
        
        # Output to new CSV
        df.to_csv(output_file, index=False)
        print(f"Successfully processed data. Output saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
