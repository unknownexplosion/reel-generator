# Deployment Guide

## 🚀 Hosting Options

### 1. Heroku (Recommended for Full Features)

```bash
# Install Heroku CLI
# Create Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set ELEVENLABS_API_KEY=your_actual_api_key

# Deploy
git push heroku main
```

### 2. Railway

1. Go to [Railway.app](https://railway.app)
2. Connect your GitHub repository
3. Add environment variable: `ELEVENLABS_API_KEY`
4. Deploy automatically

### 3. Render

1. Go to [Render.com](https://render.com)
2. Create new Web Service from GitHub
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python app.py`
5. Add environment variable: `ELEVENLABS_API_KEY`

### 4. Vercel (Limited - No FFmpeg)

```bash
npm i -g vercel
vercel --prod
```

**Note:** Vercel doesn't support FFmpeg, so video processing won't work.

## 🔧 Environment Variables Required

- `ELEVENLABS_API_KEY`: Your ElevenLabs API key
- `PORT`: Automatically set by hosting platforms
- `FLASK_ENV`: Set to `production` for live deployment

## 📋 Pre-deployment Checklist

- ✅ ElevenLabs API key configured
- ✅ FFmpeg available on hosting platform
- ✅ Python 3.9+ supported
- ✅ File upload/storage permissions
- ✅ Environment variables set

## 🌐 Demo Limitations

For public demos without API keys:
- Audio generation will use silent fallback
- Video processing still works
- UI and download features fully functional