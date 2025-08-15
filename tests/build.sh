#!/bin/bash

set -e

rm -rf test_project && uv tool run copier copy .. . \
    -d project_name=test_project \
    -d database_type=postgresql \
    -d api_framework=ninja \
    -d docker_django_port=8000 \
    --trust \
    --defaults

cd test_project && \
    make reset && \
    make migrate && \
    make logs
