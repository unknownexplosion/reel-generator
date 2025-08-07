from flask import Flask, render_template, request, jsonify, send_from_directory
import uuid
from werkzeug.utils import secure_filename
import os
import threading
import time
from generate_process import process_folder

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', 'mov', 'webm'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = str(uuid.uuid1())
    
    if request.method == "POST":
        try:
            rec_id = request.form.get("uuid")
            desc = request.form.get("text", "")
            
            if not desc.strip():
                return jsonify({"error": "Description is required"}), 400
            
            # Create upload directory
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
            os.makedirs(upload_path, exist_ok=True)
            
            # Save description
            with open(os.path.join(upload_path, "desc.txt"), "w") as f:
                f.write(desc)
            
            # Process uploaded files
            input_files = []
            for key in request.files:
                file = request.files[key]
                if file and file.filename and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(upload_path, filename)
                    file.save(file_path)
                    input_files.append(filename)
            
            if not input_files:
                return jsonify({"error": "No valid files uploaded"}), 400
            
            # Create input.txt for FFmpeg
            with open(os.path.join(upload_path, "input.txt"), "w") as f:
                for filename in input_files:
                    f.write(f"file '{filename}'\nduration 3\n")
            
            # Start background processing
            threading.Thread(target=process_folder, args=(rec_id,), daemon=True).start()
            
            return jsonify({"success": True, "message": "Reel creation started!", "id": rec_id})
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    try:
        reels_dir = "static/reels"
        if not os.path.exists(reels_dir):
            os.makedirs(reels_dir)
        reels = [f for f in os.listdir(reels_dir) if f.endswith('.mp4')]
        return render_template("gallery.html", reels=reels)
    except Exception as e:
        return render_template("gallery.html", reels=[], error=str(e))

@app.route("/status/<reel_id>")
def check_status(reel_id):
    reel_path = f"static/reels/{reel_id}.mp4"
    if os.path.exists(reel_path):
        return jsonify({"status": "completed", "url": f"/static/reels/{reel_id}.mp4"})
    else:
        return jsonify({"status": "processing"})

@app.route("/download/<filename>")
def download_reel(filename):
    try:
        return send_from_directory('static/reels', filename, as_attachment=True, download_name=f"reel_{filename}")
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    # Ensure required directories exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs("static/reels", exist_ok=True)
    
    # Get port from environment variable or default to 8000
    port = int(os.environ.get('PORT', 8000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(debug=debug, host='0.0.0.0', port=port)