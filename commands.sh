#!/usr/bin/env bash

python -m unittest

coverage run --source=app
coverage report -m

export FLASK_APP=telegram_bot.bot.py
flask run
