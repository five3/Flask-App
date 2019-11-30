#!/usr/bin/env bash
gunicorn wsgi:app -c gconfig.py