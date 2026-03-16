import pytest
import pandas as pd
from dagster_etl.assets.user_assets import extract_users, transform_users, validate_users

def test_extract_users():
    """Test user extraction"""
    df = extract_users()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert all(col in df.columns for col in ['user_id', 'name', 'email'])

def test_transform_users():
    """Test user transformation"""
    # Create sample data
    test_df = pd.DataFrame({
        'user_id': [1, 2],
        'name': ['Test1', 'Test2'],
        'email': ['TEST1@EXAMPLE.COM', 'TEST2@EXAMPLE.COM'],
        'signup_date': ['2023-01-01', '2023-01-02'],
        'country': ['us', 'uk'],
        'age': [25, 35]
    })
    
    transformed = transform_users(test_df)
    assert 'email' in transformed.columns
    assert transformed['email'].iloc[0] == 'test1@example.com'
    assert 'age_group' in transformed.columns

def test_validation():
    """Test data validation"""
    test_df = pd.DataFrame({
        'user_id': [1, 2],
        'name': ['Test1', 'Test2'],
        'email': ['test1@example.com', 'test2@example.com'],
        'signup_date': ['2023-01-01', '2023-01-02'],
        'country': ['US', 'UK'],
        'age': [25, 35],
        'age_group': ['Young', 'Young Adult'],
        'signup_year': [2023, 2023],
        'signup_month': [1, 1]
    })
    
    validated = validate_users(test_df)
    assert len(validated) == 2