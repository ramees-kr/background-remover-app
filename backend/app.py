from flask import Flask, render_template, request, send_from_directory
from rembg import remove
from PIL import Image
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    processed_image_url = None
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No image part"

        image_file = request.files['image']
        if image_file.filename == '':
            return "No selected file"

        try:
            image = Image.open(image_file)
            output = remove(image)

            unique_filename = str(uuid.uuid4()) + '.png'
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            output.save(output_path)

            processed_image_url = f'/uploads/{unique_filename}'
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template('index.html', processed_image_url=processed_image_url)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')