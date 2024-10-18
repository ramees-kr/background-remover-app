from flask import Flask, request, jsonify, send_from_directory
from rembg import remove
from PIL import Image
import io
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/remove_background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        image = Image.open(image_file)
        output = remove(image)

        # Save the processed image
        unique_filename = str(uuid.uuid4()) + '.png' 
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        output.save(output_path)

        return jsonify({'processed_image_url': f'/uploads/{unique_filename}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')