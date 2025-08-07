#!/bin/bash

echo "🎬 Setting up AI Reel Generator..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if FFmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  FFmpeg not found. Installing..."
    
    # Detect OS and install FFmpeg
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if command -v brew &> /dev/null; then
            brew install ffmpeg
        else
            echo "❌ Please install Homebrew first: https://brew.sh/"
            exit 1
        fi
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        sudo apt update && sudo apt install -y ffmpeg
    else
        echo "❌ Please install FFmpeg manually for your OS"
        exit 1
    fi
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing Python dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p user_uploads
mkdir -p static/reels
mkdir -p static/songs

# Create done.txt if it doesn't exist
touch done.txt

echo "✅ Installation complete!"
echo ""
echo "🚀 To start the application:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Set your ElevenLabs API key in .env file"
echo "3. Run: python app.py"
echo ""
echo "🌐 Then visit: http://localhost:8000"