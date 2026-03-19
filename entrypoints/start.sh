#!/bin/bash

echo "Applying migrations to alembic..."
alembic upgrade head

echo "Adding seed data..."
python -m src.app.infra.connection_engines.sqla.seed

echo "Starting FastAPI server..."
exec uvicorn src.app.presentation.rest.main:app --host 0.0.0.0 --port 8008