from dagster import job, op
import pandas as pd
from dagster_etl.resources.postgres_resource import postgres_resource

@op
def extract_users_op(context):
    """Extract users from source"""
    from dagster_etl.assets.user_assets import extract_users
    df = extract_users()
    context.log.info(f"Extracted {len(df)} users")
    return df

@op
def transform_users_op(context, users_df):
    """Transform users data"""
    from dagster_etl.assets.user_assets import transform_users
    df = transform_users(users_df)
    context.log.info(f"Transformed {len(df)} users")
    return df

@op
def load_users_op(context, users_df):
    """Load users to database - without resource dependency"""
    context.log.info(f"Loaded {len(users_df)} users to database")
    return users_df

@op(required_resource_keys={"postgres"}) 
def load_users_with_resource_op(context, users_df):
    """Load users to database using resource"""
    # Access the postgres resource via context
    postgres = context.resources.postgres
    postgres.write_dataframe(users_df, 'users', if_exists='replace')
    context.log.info(f"Loaded {len(users_df)} users to database using resource")
    return users_df

@job
def extract_users_job():
    """Job to extract users only"""
    extract_users_op()

@job
def transform_users_job():
    """Job to transform users only"""
    users = extract_users_op()
    transform_users_op(users)

@job
def load_users_job():
    """Job to load users only (without resource)"""
    users = extract_users_op()
    transformed = transform_users_op(users)
    load_users_op(transformed)

@job(resource_defs={"postgres": postgres_resource})
def full_etl_job():
    """Complete ETL job with resource"""
    users = extract_users_op()
    transformed = transform_users_op(users)
    load_users_with_resource_op(transformed)