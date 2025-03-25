#!/bin/bash

alembic upgrade head

uvicron app.main:app --reload