from flask import Flask, render_template, request
import os
from asscii import image_to_ascii

app = Flask(__name__)

# Create a directory for uploads (if it doesn't exist)
UPLOAD_FOLDER = 'the/path/you/want'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    ascii_art = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Save the image with a unique filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            ascii_art = image_to_ascii(file_path)
    return render_template('in.html', ascii_art=ascii_art)


if __name__ == '__main__':
    app.run(debug=True)
