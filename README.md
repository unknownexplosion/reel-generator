# VidSnapAI - AI Reel Generator

A modern web application for creating stunning Instagram reels using AI technology.

## ✨ Features

- 🎬 AI-powered video editing
- 🎵 Smart audio generation with ElevenLabs
- 🔗 Seamless clip stitching
- 📱 Modern glassmorphism UI
- ⬇️ Direct download functionality
- 🎨 Text overlay fallback system

## 🚀 Quick Start

### Local Development
```bash
git clone https://github.com/unknownexplosion/reel-generator.git
cd reel-generator
./install.sh
```

### Environment Setup
```bash
cp .env.example .env
# Edit .env and add your ElevenLabs API key
```

### Run Application
```bash
python app.py
# Visit: http://localhost:8000
```

## 🌐 Live Demo

**Repository**: https://github.com/unknownexplosion/reel-generator

**Deploy on Railway**: 
1. Fork this repository
2. Connect to Railway.app
3. Add `ELEVENLABS_API_KEY` environment variable
4. Deploy automatically

## 📋 Requirements

- Python 3.9+
- FFmpeg
- ElevenLabs API key (optional - has fallback)

## 🎯 How It Works

1. **Upload** images/videos
2. **Add** description text
3. **Generate** AI voice narration
4. **Create** professional reel
5. **Download** instantly

## 🔧 Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Audio**: ElevenLabs API
- **Video**: FFmpeg processing
- **UI**: Bootstrap 5 + Custom CSS

## 📱 Features

- ✅ Modern responsive design
- ✅ File upload with validation
- ✅ Real-time processing
- ✅ Download functionality
- ✅ Gallery view
- ✅ Error handling
- ✅ Fallback systems

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open Pull Request

## 📄 License

MIT License - see LICENSE file for details.