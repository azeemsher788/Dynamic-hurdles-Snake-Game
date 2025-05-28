#!/bin/bash

# Setup script for Snake Game dependencies
echo "Setting up dependencies for Snake Game..."

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    if [ -f /etc/debian_version ]; then
        # Debian/Ubuntu
        echo "Detected Debian/Ubuntu system"
        echo "Installing tkinter (requires sudo)..."
        sudo apt-get update
        sudo apt-get install -y python3-tk
    elif [ -f /etc/fedora-release ]; then
        # Fedora
        echo "Detected Fedora system"
        echo "Installing tkinter (requires sudo)..."
        sudo dnf install -y python3-tkinter
    else
        echo "Unsupported Linux distribution. Please install python3-tk manually."
        echo "See README.md for instructions."
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    echo "Detected macOS"
    if command -v brew >/dev/null 2>&1; then
        echo "Installing tkinter via Homebrew..."
        brew install python-tk
    else
        echo "Homebrew not found. Please install Homebrew first, then run this script again."
        echo "Or install python-tk manually. See README.md for instructions."
    fi
else
    echo "Unsupported operating system. Please install tkinter manually."
    echo "See README.md for instructions."
fi

# Install Python package dependencies
echo "Installing Python package dependencies..."
pip install -r requirements.txt

echo "Setup complete! You should now be able to run the Snake Game."