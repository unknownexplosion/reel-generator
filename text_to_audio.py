
import os
import uuid
import subprocess
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from config import ELEVENLABS_API_KEY

 
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def text_to_speech_file(text: str, folder: str) -> str:
    try:
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
            
        if not folder:
            raise ValueError("Folder cannot be empty")
            
        # Check if API key is configured
        if not ELEVENLABS_API_KEY or ELEVENLABS_API_KEY == "your_api_key_here":
            raise ValueError("ElevenLabs API key not configured")
        
        # Calling the text_to_speech conversion API with detailed parameters
        response = client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2_5", # use the turbo model for low latency
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
                speed=1.0,
            ),
        )

        # Ensure directory exists
        folder_path = f"user_uploads/{folder}"
        os.makedirs(folder_path, exist_ok=True)
        
        # Generating file path
        save_file_path = os.path.join(folder_path, "audio.mp3")

        # Writing the audio to a file
        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)

        print(f"{save_file_path}: Audio file saved successfully!")
        return save_file_path
        
    except Exception as e:
        print(f"Error in text_to_speech_file: {str(e)}")
        # Create a fallback silent audio file
        fallback_path = create_fallback_audio(folder)
        return fallback_path

def create_fallback_audio(folder: str) -> str:
    """Create a silent audio file as fallback"""
    try:
        folder_path = f"user_uploads/{folder}"
        os.makedirs(folder_path, exist_ok=True)
        save_file_path = os.path.join(folder_path, "audio.mp3")
        
        # Create 5 seconds of silence using FFmpeg
        command = [
            'ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=22050',
            '-t', '5', '-c:a', 'mp3', save_file_path
        ]
        subprocess.run(command, capture_output=True, check=True)
        print(f"Fallback silent audio created: {save_file_path}")
        return save_file_path
    except Exception as e:
        print(f"Failed to create fallback audio: {str(e)}")
        raise e


# text_to_speech_file("Hey I am a good boy and its the python course", "ac9a7034-2bf9-11f0-b9c0-ad551e1c593a")