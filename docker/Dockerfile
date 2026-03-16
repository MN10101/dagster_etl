FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set environment variables
ENV DAGSTER_HOME=/app/dagster_home
ENV PYTHONPATH=/app

# Create dagster home directory and logs subdirectory
RUN mkdir -p $DAGSTER_HOME && \
    mkdir -p $DAGSTER_HOME/logs && \
    echo "storage:" > $DAGSTER_HOME/dagster.yaml && \
    echo "  postgres:" >> $DAGSTER_HOME/dagster.yaml && \
    echo "    postgres_url: postgresql://postgres:postgres@postgres:5432/postgres" >> $DAGSTER_HOME/dagster.yaml && \
    echo "compute_logs:" >> $DAGSTER_HOME/dagster.yaml && \
    echo "  module: dagster.core.storage.local_compute_log_manager" >> $DAGSTER_HOME/dagster.yaml && \
    echo "  class: LocalComputeLogManager" >> $DAGSTER_HOME/dagster.yaml && \
    echo "  config:" >> $DAGSTER_HOME/dagster.yaml && \
    echo "    base_dir: /app/dagster_home/storage" >> $DAGSTER_HOME/dagster.yaml

# Expose port
EXPOSE 3000

# Command
CMD ["dagster-webserver", "-h", "0.0.0.0", "-p", "3000"]
