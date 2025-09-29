#!/bin/bash

echo "Starting AgenticAI - The Next Generation Product"
echo "================================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    exit 1
fi

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing Python dependencies..."
    pip install -r requirements.txt
fi

# Start the application
echo "Starting the application..."
echo "Access the application at: http://localhost:8080"
echo "API documentation available in README.md"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py