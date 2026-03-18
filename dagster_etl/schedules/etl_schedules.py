from dagster import schedule

@schedule(
    cron_schedule="0 9 * * *", 
    job_name="full_etl_job",
    execution_timezone="Europe/Berlin"
)
def daily_etl_schedule(context):
    """Schedule to run ETL daily"""
    return {}
