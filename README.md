# VidSnapAI - AI Reel Generator

A modern web application for creating stunning Instagram reels using AI technology.

## Features

- 🎬 AI-powered video editing
- 🎵 Smart music integration
- 🔗 Seamless clip stitching
- 📱 Modern responsive design
- 🎨 Glassmorphism UI effects

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5, Custom CSS
- **Icons**: Font Awesome

## Installation

### Quick Setup (Recommended)
```bash
git clone https://github.com/yourusername/ai-reel-generator.git
cd ai-reel-generator
./install.sh
```

### Manual Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-reel-generator.git
cd ai-reel-generator
```

2. Install FFmpeg:
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

3. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Configure environment:
```bash
# Copy .env file and add your ElevenLabs API key
cp .env.example .env
# Edit .env and add: ELEVENLABS_API_KEY=your_actual_api_key
```

6. Run the application:
```bash
python app.py
```

7. Open your browser and navigate to `http://localhost:8000`

## Usage

1. Visit the homepage to learn about features
2. Click "Create Reel" to start generating content
3. Browse the gallery to see examples
4. Upload your videos and let AI do the magic!

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

### Common Issues

**1. FFmpeg not found**
```bash
# Install FFmpeg first
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Linux
```

**2. ElevenLabs API errors**
- Get API key from [ElevenLabs](https://elevenlabs.io/)
- Add to `.env` file: `ELEVENLABS_API_KEY=your_key`
- Check API quota/credits

**3. File upload issues**
- Check file size (max 100MB)
- Supported formats: JPG, PNG, GIF, MP4, AVI, MOV, WEBM
- Ensure proper file permissions

**4. Reel not generating**
- Check logs in terminal
- Verify all dependencies installed
- Ensure `user_uploads` and `static/reels` directories exist

**5. Port already in use**
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

### Getting Help
- Check the logs in terminal for detailed error messages
- Ensure all dependencies are installed correctly
- Verify FFmpeg installation: `ffmpeg -version`

## Contact

Your Name - [@yourusername](https://twitter.com/yourusername)

Project Link: [https://github.com/yourusername/ai-reel-generator](https://github.com/yourusername/ai-reel-generator)