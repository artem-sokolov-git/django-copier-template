#!/bin/bash

set -e

rm -rf test_project

COPIER_SETTINGS_PATH="./settings.yaml" uvx copier copy .. . \
    -d project_name=test_project \
    --trust \
    --defaults

cd test_project && \
    make rebuild && \
    make migrate && \
    make admin
