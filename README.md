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

## 🖼️ Complete Architecture Overview

<img width="8347" height="6828" alt="Image" src="https://github.com/user-attachments/assets/c8b2aa30-9beb-4189-91d8-27ed034c4544" />

*End-to-end data pipeline architecture showing data sources, ETL process, and Dagster components*

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

Dagster Jobs <img width="1919" height="1036" alt="Image" src="https://github.com/user-attachments/assets/ca0335ff-216c-432b-8157-29196b9995b8" /> *Available jobs in the Dagster UI*

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

ETL Process Flow <img src="https://github.com/user-attachments/assets/769b9d09-a2fb-4072-ab1f-d5c88d9cd40f" width="700"> *Step-by-step execution of the
ETL pipeline*

------------------------------------------------------------------------

## 🧪 Testing

Run tests:

``` bash
pytest tests/ -v
```

------------------------------------------------------------------------

## 🖼️ Test Results

Pytest Results <img width="1381" height="293" alt="Image" src="https://github.com/user-attachments/assets/a966b132-c2bd-40e4-a4fd-51feb1207318" /> *All 7 tests passing successfully*

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

Docker Setup <img width="4263" height="2251" alt="Image" src="https://github.com/user-attachments/assets/c5856280-9f26-43a9-8d0e-e92a3449b3b3" /> *Container
orchestration with Docker*

------------------------------------------------------------------------

## 📊 Data Lineage

    users.csv → extract_users → transform_users → validate_users
    orders.csv → extract_orders → transform_orders → analytics

------------------------------------------------------------------------

## 🖼️ Data Lineage Diagram

Data Lineage <img width="4937" height="1653" alt="Image" src="https://github.com/user-attachments/assets/63bb8490-7369-4ec5-adf5-b6b2388598a6" /> *End-to-end data flow from source to
destination*

------------------------------------------------------------------------

## 🔍 Monitoring & Debugging

Use the Dagster UI to inspect job runs and logs.

------------------------------------------------------------------------

## 🖼️ Run Logs - Extract Job

Extract Users Job <img width="1919" height="1036" alt="Image" src="https://github.com/user-attachments/assets/18924f66-5850-4369-b07c-dff465f398a4" /> Run*Successful execution of
extract_users_job showing 100 users extracted*

------------------------------------------------------------------------

## 🖼️ Run Logs - Load Job

Load Users Job Run <img width="1919" height="1036" alt="Image" src="https://github.com/user-attachments/assets/0de2460e-fbe4-48df-93e1-357878459a37" /> *Successful execution of load_users_job
showing data loaded to database*

------------------------------------------------------------------------

## 🗄️ Database Verification

``` bash
docker exec -it docker-postgres-1 psql -U postgres -d postgres -c "SELECT COUNT(*) FROM users;"
```

------------------------------------------------------------------------

## 🖼️ PostgreSQL Verification

Database Results <img width="1519" height="645" alt="Image" src="https://github.com/user-attachments/assets/f2f7c204-81fb-4856-a340-7c605ebc0a0d" /> *Verified 100 users loaded with correct age
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
