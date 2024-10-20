from flask import Flask, render_template, request, jsonify, send_file, url_for
import os
import uuid
from rembg import remove  # Using rmbg to remove the background from images

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = os.path.join("static", "processed")
print(PROCESSED_FOLDER)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

# Function to clear the contents of the specified folder
def clear_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

clear_folder(UPLOAD_FOLDER)
clear_folder(PROCESSED_FOLDER)

@app.route('/process-image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    
    # Generate a unique filename using uuid
    input_filename = f"{uuid.uuid4()}.png"
    input_filepath = os.path.join(UPLOAD_FOLDER, input_filename)
    print(input_filepath)
    
    # Save the uploaded image to the uploads folder
    file.save(input_filepath)
    
    # Process the image to remove the background
    with open(input_filepath, 'rb') as input_image:
        output_data = remove(input_image.read())  # Remove background using rmbg

    # Save the processed image to the processed folder
    output_filename = f"processed_{input_filename}"
    output_filepath = os.path.join(PROCESSED_FOLDER, output_filename)
    print(output_filepath)
    
    with open(output_filepath, 'wb') as output_image:
        output_image.write(output_data)
    
    # Return the URL of the processed image to the frontend
    processed_image_url = url_for('get_processed_image', filename=output_filename)
    print("Inside process_image: Processed image URL = " + processed_image_url)
    return jsonify({"processed_image_url": processed_image_url})

@app.route('/processed/<filename>')
def get_processed_image(filename):
    return send_file(os.path.join(PROCESSED_FOLDER, filename))

if __name__ == "__main__":
    app.run(debug=True)
