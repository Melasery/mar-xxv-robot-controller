#!/bin/bash

echo "Starting MAR-XXV Robot Control Server..."

# Navigate to the project directory (optional: update if needed)
cd "$(dirname "$0")"

# Activate virtual environment (if applicable)
# source venv/bin/activate  # Uncomment if using a virtual environment

# Start the FastAPI server using uvicorn
uvicorn src.server:app --host 0.0.0.0 --port 8000 --reload
