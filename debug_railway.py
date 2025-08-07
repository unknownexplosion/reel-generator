#!/usr/bin/env python3

import os
import subprocess
import sys

def debug_railway_environment():
    """Debug Railway deployment environment"""
    print("🔍 Railway Environment Debug")
    print("=" * 50)
    
    # Check Python version
    print(f"Python version: {sys.version}")
    
    # Check FFmpeg
    try:
        result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
        print("✅ FFmpeg is available")
        print(f"FFmpeg version: {result.stdout.split()[2] if result.stdout else 'Unknown'}")
    except FileNotFoundError:
        print("❌ FFmpeg not found")
    
    # Check directories
    dirs_to_check = ['user_uploads', 'static', 'static/reels']
    for dir_name in dirs_to_check:
        if os.path.exists(dir_name):
            print(f"✅ Directory exists: {dir_name}")
        else:
            print(f"❌ Directory missing: {dir_name}")
            try:
                os.makedirs(dir_name, exist_ok=True)
                print(f"✅ Created directory: {dir_name}")
            except Exception as e:
                print(f"❌ Failed to create {dir_name}: {e}")
    
    # Check environment variables
    env_vars = ['ELEVENLABS_API_KEY', 'PORT', 'FLASK_ENV']
    for var in env_vars:
        value = os.environ.get(var)
        if value:
            if var == 'ELEVENLABS_API_KEY':
                print(f"✅ {var}: {value[:10]}...")
            else:
                print(f"✅ {var}: {value}")
        else:
            print(f"❌ {var}: Not set")
    
    # Check file permissions
    try:
        test_file = 'test_write.txt'
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        print("✅ File write permissions: OK")
    except Exception as e:
        print(f"❌ File write permissions: {e}")
    
    print("=" * 50)

if __name__ == "__main__":
    debug_railway_environment()