import pytest
import pandas as pd
import numpy as np
from dagster_etl.assets.order_assets import extract_orders, transform_orders, user_order_analytics

def test_extract_orders():
    """Test order extraction"""
    df = extract_orders()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert all(col in df.columns for col in ['order_id', 'user_id', 'order_date', 'amount', 'status'])
    assert df['amount'].between(10, 500).all()

def test_transform_orders():
    """Test order transformation"""
    # Create sample data
    test_df = pd.DataFrame({
        'order_id': [1, 2, 3],
        'user_id': [1, 1, 2],
        'order_date': ['2024-01-01', '2024-02-01', '2024-03-01'],
        'amount': [50.0, 200.0, 500.0],
        'status': ['completed', 'completed', 'cancelled']
    })
    
    transformed = transform_orders(test_df)
    
    # Check transformations
    assert 'order_year' in transformed.columns
    assert 'order_month' in transformed.columns
    assert 'order_quarter' in transformed.columns
    assert 'order_category' in transformed.columns
    
    # Check cancelled orders are filtered out
    assert len(transformed) == 2 
    assert transformed['order_category'].iloc[0] == 'Small'
    assert transformed['order_category'].iloc[1] == 'Medium'

def test_transform_orders_empty():
    """Test order transformation with empty dataframe"""
    empty_df = pd.DataFrame(columns=['order_id', 'user_id', 'order_date', 'amount', 'status'])
    transformed = transform_orders(empty_df)
    assert len(transformed) == 0

def test_user_order_analytics():
    """Test user order analytics"""
    # Create mock users data
    users_df = pd.DataFrame({
        'user_id': [1, 2, 3],
        'name': ['User1', 'User2', 'User3'],
        'email': ['user1@test.com', 'user2@test.com', 'user3@test.com'],
        'age_group': ['Young', 'Adult', 'Senior']
    })
    
    # Create mock orders data
    orders_df = pd.DataFrame({
        'order_id': [1, 2, 3, 4],
        'user_id': [1, 1, 2, 3],
        'amount': [100, 200, 300, 400],
        'order_category': ['Small', 'Medium', 'Large', 'Large']
    })
    
    result = user_order_analytics(validate_users=users_df, transform_orders=orders_df)
    
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 3
    assert all(col in result.columns for col in ['user_id', 'total_orders', 'total_spent', 'avg_order_value'])
    
    # Check calculations
    user1 = result[result['user_id'] == 1].iloc[0]
    assert user1['total_orders'] == 2
    assert user1['total_spent'] == 300
    assert user1['avg_order_value'] == 150