# Dagster ETL Project

## 🎯 Project Overview

A production-ready ETL pipeline built with **Dagster, Docker, and
PostgreSQL** demonstrating modern data engineering practices.

------------------------------------------------------------------------

## Author
**Mahmoud Najmeh**  
<img src="https://avatars.githubusercontent.com/u/78208459?u=c3f9c7d6b49fc9726c5ea8bce260656bcb9654b3&v=4" width="200px" style="border-radius: 50%;">

------------------------------------------------------------------------

## 🖼️ Architecture Diagram

Component Architecture <img width="7584" height="1148" alt="Image" 
src="https://github.com/user-attachments/assets/c22267e0-cd90-42ef-9c68-455cc2aad4d4" />

------------------------------------------------------------------------

## 📊 Architecture Components

### Core Technologies

-   **Orchestration:** Dagster (Assets, Ops, Jobs, Schedules)
-   **Database:** PostgreSQL 14
-   **Containerization:** Docker & Docker Compose
-   **Data Processing:** Pandas, SQLAlchemy
-   **Testing:** Pytest

### Pipeline Flow

Source → Extract → Transform → Validate → Load → Analytics

------------------------------------------------------------------------

## 🏗️ Project Structure

    dagster-etl-project/
    ├── dagster_etl/
    │   ├── assets/
    │   │   ├── user_assets.py
    │   │   └── order_assets.py
    │   ├── jobs/
    │   │   └── user_jobs.py
    │   ├── resources/
    │   │   └── postgres_resource.py
    │   └── schedules/
    │       └── daily_schedule.py
    ├── tests/
    │   ├── test_assets.py
    │   └── test_order_assets.py
    ├── docker/
    │   ├── docker-compose.yml
    │   └── Dockerfile
    ├── data/
    │   ├── input/
    │   └── output/
    └── requirements.txt

------------------------------------------------------------------------

## 🖼️ Asset Dependency Graph

Asset Dependencies <img width="2163" height="1885" alt="Image" src="https://github.com/user-attachments/assets/e87fc06d-43a5-48dd-9da0-47fcb762b3a2" />*How your data
assets depend on each other*

------------------------------------------------------------------------

## 🚀 Quick Start

### Prerequisites

-   Python 3.9+
-   Docker & Docker Compose
-   PostgreSQL client (optional)

------------------------------------------------------------------------

## 🧑‍💻 Local Development Setup

### Clone and Setup Environment

``` bash
git clone <your-repo>
cd dagster-etl-project

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

------------------------------------------------------------------------

### Environment Configuration

Create a `.env` file:

    POSTGRES_CONNECTION_STRING=postgresql://postgres:postgres@localhost:5432/postgres
    DAGSTER_HOME=/path/to/dagster_home

------------------------------------------------------------------------

## 🐳 Run with Docker

``` bash
cd docker
docker-compose up -d
```

Access: - Dagster UI → http://localhost:3000 - PostgreSQL →
localhost:5432

------------------------------------------------------------------------

## 📋 Available Jobs

  Job Name              Description                Status
  --------------------- -------------------------- --------
  extract_users_job     Extract users from CSV     ✅
  transform_users_job   Transform user data        ✅
  load_users_job        Load users to PostgreSQL   ✅
  full_etl_job          Complete ETL pipeline      ✅

------------------------------------------------------------------------

## 🖼️ Job Overview

![Dagster Jobs](m3.png) *Available jobs in the Dagster UI*

------------------------------------------------------------------------

## ⏰ Schedules

Daily ETL execution

    Schedule: 0 9 * * *
    Job: full_etl_job

------------------------------------------------------------------------

## 📈 Data Assets

### User Pipeline

-   extract_users
-   transform_users
-   validate_users
-   load_users

### Order Pipeline

-   extract_orders
-   transform_orders
-   user_order_analytics

Output:

    data/output/user_metrics_*.csv

------------------------------------------------------------------------

## 🖼️ Execution Flow

![ETL Process Flow](Execution%20Flow.png) *Step-by-step execution of the
ETL pipeline*

------------------------------------------------------------------------

## 🧪 Testing

Run tests:

``` bash
pytest tests/ -v
```

------------------------------------------------------------------------

## 🖼️ Test Results

![Pytest Results](m.png) *All 7 tests passing successfully*

------------------------------------------------------------------------

## 🐳 Docker Architecture

Network:

    dagster-network (bridge)

Containers:

-   dagster-webserver
-   dagster-daemon
-   postgres

Volumes:

-   postgres_data
-   dagster_home
-   ./data

------------------------------------------------------------------------

## 🖼️ Docker Network Architecture

![Docker Setup](Docker%20Network%20Architecture.png) *Container
orchestration with Docker*

------------------------------------------------------------------------

## 📊 Data Lineage

    users.csv → extract_users → transform_users → validate_users
    orders.csv → extract_orders → transform_orders → analytics

------------------------------------------------------------------------

## 🖼️ Data Lineage Diagram

![Data Lineage](Data%20Lineage.png) *End-to-end data flow from source to
destination*

------------------------------------------------------------------------

## 🔍 Monitoring & Debugging

Use the Dagster UI to inspect job runs and logs.

------------------------------------------------------------------------

## 🖼️ Run Logs - Extract Job

![Extract Users Job Run](m1.png) *Successful execution of
extract_users_job showing 100 users extracted*

------------------------------------------------------------------------

## 🖼️ Run Logs - Load Job

![Load Users Job Run](m2.png) *Successful execution of load_users_job
showing data loaded to database*

------------------------------------------------------------------------

## 🗄️ Database Verification

``` bash
docker exec -it docker-postgres-1 psql -U postgres -d postgres -c "SELECT COUNT(*) FROM users;"
```

------------------------------------------------------------------------

## 🖼️ PostgreSQL Verification

![Database Results](m4.png) *Verified 100 users loaded with correct age
distribution*

------------------------------------------------------------------------

## 🛠️ Common Operations

Materialize assets:

``` bash
dagster asset materialize --select '*' -m dagster_etl
```

Run ETL job:

``` bash
dagster job execute -m dagster_etl -j full_etl_job
```

Docker logs:

``` bash
docker-compose logs -f
```

Cleanup:

``` bash
docker-compose down -v
```
