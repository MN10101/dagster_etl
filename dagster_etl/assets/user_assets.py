from dagster import asset
import pandas as pd
import numpy as np
from datetime import datetime
import random

@asset
def extract_users():
    """
    Simulate extracting user data from an API or CSV
    """
    # Simulate reading from a CSV or API
    try:
        df = pd.read_csv('data/input/users.csv')
    except FileNotFoundError:
        # Create sample data if file doesn't exist
        data = {
            'user_id': range(1, 101),
            'name': [f'User_{i}' for i in range(1, 101)],
            'email': [f'user{i}@example.com' for i in range(1, 101)],
            'signup_date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
            'country': np.random.choice(['US', 'UK', 'CA', 'AU', 'DE'], 100),
            'age': np.random.randint(18, 70, 100)
        }
        df = pd.DataFrame(data)
        df.to_csv('data/input/users.csv', index=False)
    
    return df

@asset
def transform_users(extract_users):
    """
    Clean and transform user data
    """
    df = extract_users.copy()
    
    # Data cleaning
    df['email'] = df['email'].str.lower()
    df['country'] = df['country'].str.upper()
    
    # Add derived columns
    df['age_group'] = pd.cut(df['age'], 
                             bins=[0, 25, 35, 50, 100], 
                             labels=['Young', 'Young Adult', 'Adult', 'Senior'])
    
    df['signup_year'] = pd.to_datetime(df['signup_date']).dt.year
    df['signup_month'] = pd.to_datetime(df['signup_date']).dt.month
    
    # Handle missing values
    df.fillna({'age': df['age'].median()}, inplace=True)
    
    return df

@asset
def validate_users(transform_users):
    """
    Validate transformed data
    """
    df = transform_users.copy()
    
    # Validation checks
    assert df['user_id'].is_unique, "User IDs must be unique"
    assert (df['age'] >= 18).all(), "All users must be 18 or older"
    assert df['email'].str.contains('@').all(), "Invalid email format"
    
    # Log validation results
    print(f"✅ Validation passed: {len(df)} users processed")
    print(f"📊 Age distribution:\n{df['age_group'].value_counts()}")
    
    return df