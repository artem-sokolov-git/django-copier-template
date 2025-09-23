#!/bin/bash

set -e

rm -rf django_copier_template

uvx copier copy .. . \
    --trust \
    --defaults

cd django_copier_template &&
    make rebuild && \
    make first_app_app
    make check
