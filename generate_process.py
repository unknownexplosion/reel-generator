import os 
from text_to_audio import text_to_speech_file
import subprocess
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def text_to_audio(folder):
    """Generate audio from text description"""
    try:
        desc_path = f"user_uploads/{folder}/desc.txt"
        if not os.path.exists(desc_path):
            raise FileNotFoundError(f"Description file not found: {desc_path}")
            
        with open(desc_path, 'r') as f:
            text = f.read().strip()
            
        if not text:
            raise ValueError("Description text is empty")
            
        logger.info(f"Generating audio for folder: {folder}")
        text_to_speech_file(text, folder)
        return True
        
    except Exception as e:
        logger.error(f"Error generating audio for {folder}: {str(e)}")
        return False

def create_reel(folder):
    """Create video reel from images and audio"""
    try:
        input_file = f"user_uploads/{folder}/input.txt"
        audio_file = f"user_uploads/{folder}/audio.mp3"
        output_file = f"static/reels/{folder}.mp4"
        
        # Check if required files exist
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"Audio file not found: {audio_file}")
            
        # Ensure output directory exists
        os.makedirs("static/reels", exist_ok=True)
        
        # FFmpeg command with better error handling
        command = [
            'ffmpeg', '-y',  # -y to overwrite output files
            '-f', 'concat', '-safe', '0', '-i', input_file,
            '-i', audio_file,
            '-vf', 'scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black',
            '-c:v', 'libx264', '-c:a', 'aac',
            '-shortest', '-r', '30', '-pix_fmt', 'yuv420p',
            output_file
        ]
        
        logger.info(f"Creating reel for folder: {folder}")
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        if os.path.exists(output_file):
            logger.info(f"Reel created successfully: {output_file}")
            return True
        else:
            raise Exception("Output file was not created")
            
    except subprocess.CalledProcessError as e:
        logger.error(f"FFmpeg error for {folder}: {e.stderr}")
        return False
    except Exception as e:
        logger.error(f"Error creating reel for {folder}: {str(e)}")
        return False

def process_folder(folder):
    """Process a single folder to create a reel"""
    try:
        logger.info(f"Starting processing for folder: {folder}")
        
        # Generate audio
        if not text_to_audio(folder):
            return False
            
        # Create reel
        if not create_reel(folder):
            return False
            
        # Mark as done
        with open("done.txt", "a") as f:
            f.write(folder + "\n")
            
        logger.info(f"Successfully processed folder: {folder}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to process folder {folder}: {str(e)}")
        return False

def check_ffmpeg():
    """Check if FFmpeg is installed"""
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False