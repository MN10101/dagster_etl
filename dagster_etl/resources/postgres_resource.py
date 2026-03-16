from dagster import resource
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

class PostgresResource:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.engine = None

    def connect(self):
        """Create database connection"""
        self.engine = create_engine(self.connection_string)
        return self.engine

    def execute_query(self, query):
        """Execute SQL query"""
        if not self.engine:
            self.connect()
        with self.engine.connect() as conn:
            return pd.read_sql(query, conn)

    def write_dataframe(self, df, table_name, if_exists='replace'):
        """Write DataFrame to PostgreSQL with debug info"""
        print("="*50, flush=True)
        print("🚨🚨🚨 WRITE_DATAFRAME IS DEFINITELY BEING CALLED! 🚨🚨🚨", flush=True)
        print("="*50, flush=True)
        print(f"🔥 Table name: {table_name}", flush=True)
        print(f"🔥 Rows: {len(df)}", flush=True)
        print(f"🔥 Columns: {df.columns.tolist()}", flush=True)
        print(f"🔥 First row: {df.iloc[0].to_dict()}", flush=True)
        
        # Make sure we're connected
        if not self.engine:
            print("⚡ Connecting to database...", flush=True)
            self.connect()
        
        print(f"🔍 Attempting to write {len(df)} rows to table '{table_name}'", flush=True)
        print(f"🔍 Database: {self.engine.url.database}", flush=True)
        print(f"🔍 Host: {self.engine.url.host}", flush=True)

        # Try to list existing tables first
        try:
            existing = pd.read_sql("SELECT tablename FROM pg_tables WHERE schemaname='public'", self.engine)
            print(f"📋 Existing tables before write: {existing['tablename'].tolist()}", flush=True)
        except Exception as e:
            print(f"⚠️ Could not list tables: {e}", flush=True)

        # Write the data
        print(f"⚡ About to execute to_sql...", flush=True)
        try:
            result = df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)
            print(f"⚡ to_sql returned: {result}", flush=True)
        except Exception as e:
            print(f"❌ to_sql failed: {e}", flush=True)
            raise e

        # Verify it was written
        try:
            after = pd.read_sql("SELECT tablename FROM pg_tables WHERE schemaname='public'", self.engine)
            print(f"📋 Existing tables after write: {after['tablename'].tolist()}", flush=True)
        except Exception as e:
            print(f"⚠️ Could not list tables after write: {e}", flush=True)

        # Try to read it back
        try:
            test_read = pd.read_sql(f"SELECT COUNT(*) FROM {table_name}", self.engine)
            print(f"✅ Verified {test_read.iloc[0,0]} rows in {table_name}", flush=True)
        except Exception as e:
            print(f"❌ Verification failed: {e}", flush=True)

        print(f"✅ Written {len(df)} rows to {table_name}", flush=True)

@resource
def postgres_resource(init_context):
    """Resource for PostgreSQL connection"""
    # Get connection string from environment or use default
    connection_string = os.getenv(
        'POSTGRES_CONNECTION_STRING',
        'postgresql://postgres:postgres@localhost:5432/postgres'
    )
    resource = PostgresResource(connection_string)
    resource.connect() 
    return resource