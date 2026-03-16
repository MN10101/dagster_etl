from dagster import Definitions, load_assets_from_modules
from dagster_etl.assets import user_assets, order_assets
from dagster_etl.resources.postgres_resource import postgres_resource
from dagster_etl.jobs.etl_jobs import (
    extract_users_job,
    transform_users_job,
    load_users_job,
    full_etl_job
)
from dagster_etl.schedules.etl_schedules import daily_etl_schedule

# Load all assets
all_assets = load_assets_from_modules([user_assets, order_assets])

# Define the Dagster repository
defs = Definitions(
    assets=all_assets,
    resources={
        "postgres": postgres_resource,
    },
    jobs=[
        extract_users_job,
        transform_users_job,
        load_users_job,
        full_etl_job,
    ],
    schedules=[daily_etl_schedule],
)