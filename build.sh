#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# --- Start of corrected Tailwind setup ---
# Change directory to the static_src folder
cd theme/static_src

# Install Node.js dependencies from package.json
npm install

# Change back to the project root
cd ../../

# Run the Django Tailwind build command from the project root
python manage.py tailwind build

# --- End of corrected Tailwind setup ---

# Collect static files and run migrations
python manage.py collectstatic --noinput
python manage.py migrate
