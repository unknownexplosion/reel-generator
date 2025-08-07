# 🚀 Live Hosting Instructions

## Your Repository: https://github.com/unknownexplosion/reel-generator

## Quick Deploy on Railway (Recommended)

1. **Go to Railway**: https://railway.app
2. **Sign in** with GitHub
3. **New Project** → **Deploy from GitHub repo**
4. **Select**: `unknownexplosion/reel-generator`
5. **Add Environment Variable**:
   - Key: `ELEVENLABS_API_KEY`
   - Value: `sk_681c93af660add9a3312c3e0a59a855bf3ac6a3e3d22ca81`
6. **Deploy** - Railway will automatically build and deploy!

## Alternative: Heroku

```bash
# Install Heroku CLI first
heroku create reel-generator-app
heroku config:set ELEVENLABS_API_KEY=sk_681c93af660add9a3312c3e0a59a855bf3ac6a3e3d22ca81
git push heroku main
```

## Alternative: Render

1. Go to https://render.com
2. **New** → **Web Service**
3. Connect GitHub: `unknownexplosion/reel-generator`
4. Settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
5. Add Environment Variable: `ELEVENLABS_API_KEY`

## 🎯 Expected Result

Your live app will have:
- ✅ Modern UI with glassmorphism effects
- ✅ File upload functionality
- ✅ AI voice generation
- ✅ Video reel creation
- ✅ Download feature
- ✅ Responsive gallery

## 📱 Share Your Live App

Once deployed, you'll get a URL like:
- Railway: `https://your-app.railway.app`
- Heroku: `https://reel-generator-app.herokuapp.com`
- Render: `https://reel-generator.onrender.com`