#!/usr/bin/env bash
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Explicitly install Node.js and npm for the current build
# This is more reliable than relying on the system-wide install from render.yaml
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt-get update && apt-get install -y nodejs

# Change directory to the static_src folder
cd theme/static_src

# Install Node.js dependencies from package.json
npm install

# Change back to the project root
cd ../../

# Explicitly set NPM_BIN_PATH for the following commands
export NPM_BIN_PATH=$(which npm)
python manage.py tailwind build

# Collect static files and run migrations
python manage.py collectstatic --noinput
python manage.py migrate
