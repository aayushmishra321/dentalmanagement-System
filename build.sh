#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "🚀 Starting build process..."

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo "🗄️ Running database migrations..."
python manage.py migrate

echo "🔍 Running registration test..."
python test_registration.py || echo "⚠️ Registration test failed, but continuing..."

echo "✅ Build completed successfully!"
