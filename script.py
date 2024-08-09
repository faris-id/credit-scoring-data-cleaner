import pandas as pd
import re

def clean_data(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Clean Annual_Income
    def clean_annual_income(value):
        cleaned_value = re.sub(r'[^0-9.]', '', str(value))
        return float(cleaned_value) if cleaned_value else None

    df['Annual_Income'] = df['Annual_Income'].apply(clean_annual_income)
    df = df.dropna(subset=['Annual_Income'])

    # Clean Num_of_Loan
    def clean_num_of_loan(value):
        cleaned_value = re.sub(r'[^0-9]', '', str(value))
        cleaned_value = int(cleaned_value) if cleaned_value.isdigit() else None
        return cleaned_value if cleaned_value is not None and 0 <= cleaned_value <= 100 else None

    df['Num_of_Loan'] = df['Num_of_Loan'].apply(clean_num_of_loan)
    df = df.dropna(subset=['Num_of_Loan'])

    # Clean Num_of_Delayed_Payment
    def clean_num_of_delayed_payment(value):
        if pd.isna(value) or value == '':
            return 0
        cleaned_value = re.sub(r'[^0-9]', '', str(value))
        return int(cleaned_value) if cleaned_value.isdigit() else 0

    df['Num_of_Delayed_Payment'] = df['Num_of_Delayed_Payment'].apply(clean_num_of_delayed_payment)

    # Clean Changed_Credit_Limit
    def clean_changed_credit_limit(value):
        try:
            return float(value)
        except ValueError:
            return None

    df['Changed_Credit_Limit'] = df['Changed_Credit_Limit'].apply(clean_changed_credit_limit)
    df = df.dropna(subset=['Changed_Credit_Limit'])

    # Clean Outstanding_Debt
    def clean_outstanding_debt(value):
        cleaned_value = re.sub(r'[^0-9.]', '', str(value))
        return float(cleaned_value) if cleaned_value else None

    df['Outstanding_Debt'] = df['Outstanding_Debt'].apply(clean_outstanding_debt)
    df = df.dropna(subset=['Outstanding_Debt'])

    # Clean Amount_invested_monthly
    df['Amount_invested_monthly'] = df['Amount_invested_monthly'].apply(clean_outstanding_debt)
    df = df.dropna(subset=['Amount_invested_monthly'])

    # Clean Monthly_Balance
    df['Monthly_Balance'] = df['Monthly_Balance'].apply(clean_outstanding_debt)
    df = df.dropna(subset=['Monthly_Balance'])

    # Clean Age
    def clean_age(value):
        cleaned_value = re.sub(r'[^0-9-]', '', str(value))
        cleaned_value = int(cleaned_value) if cleaned_value.lstrip('-').isdigit() else None
        return cleaned_value if cleaned_value is not None and 0 <= cleaned_value <= 100 else None

    df['Age'] = df['Age'].apply(clean_age)
    df = df.dropna(subset=['Age'])

    # Save the cleaned data to a new CSV file
    df.to_csv(output_file, index=False)

# Example usage:
input_file = 'test_original.csv'  # Replace with your input CSV file path
output_file = 'test_cleaned.csv'  # Replace with your desired output CSV file path

clean_data(input_file, output_file)
