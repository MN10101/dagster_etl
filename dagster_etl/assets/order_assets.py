from dagster import asset
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

@asset
def extract_orders():
    """
    Extract order data
    """
    # Generate sample order data
    n_orders = 500
    data = {
        'order_id': range(1, n_orders + 1),
        'user_id': np.random.randint(1, 101, n_orders),
        'order_date': [datetime.now() - timedelta(days=np.random.randint(0, 365)) 
                       for _ in range(n_orders)],
        'amount': np.random.uniform(10, 500, n_orders).round(2),
        'status': np.random.choice(['completed', 'pending', 'cancelled'], n_orders, 
                                   p=[0.7, 0.2, 0.1])
    }
    
    df = pd.DataFrame(data)
    df.to_csv('data/input/orders.csv', index=False)
    return df

@asset
def transform_orders(extract_orders):
    """
    Transform order data
    """
    df = extract_orders.copy()
    
    # Add derived columns
    df['order_year'] = pd.to_datetime(df['order_date']).dt.year
    df['order_month'] = pd.to_datetime(df['order_date']).dt.month
    df['order_quarter'] = pd.to_datetime(df['order_date']).dt.quarter
    
    # Categorize orders by amount
    df['order_category'] = pd.cut(df['amount'], 
                                  bins=[0, 50, 200, 500], 
                                  labels=['Small', 'Medium', 'Large'])
    
    # Filter out cancelled orders for analysis
    df_valid = df[df['status'] != 'cancelled'].copy()
    
    return df_valid

@asset
def user_order_analytics(validate_users, transform_orders):
    """
    Join users and orders for analytics
    """
    users = validate_users
    orders = transform_orders
    
    # Merge datasets
    analytics = pd.merge(orders, users, on='user_id', how='inner')
    
    # Calculate metrics
    user_metrics = analytics.groupby('user_id').agg({
        'order_id': 'count',
        'amount': ['sum', 'mean']
    }).round(2)
    
    user_metrics.columns = ['total_orders', 'total_spent', 'avg_order_value']
    user_metrics = user_metrics.reset_index()
    
    # Save to CSV
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = f'data/output/user_metrics_{timestamp}.csv'
    user_metrics.to_csv(output_path, index=False)
    
    print(f"✅ Analytics generated: {output_path}")
    print(f"📊 Total users with orders: {len(user_metrics)}")
    print(f"💰 Average spend per user: ${user_metrics['avg_order_value'].mean():.2f}")
    
    return user_metrics