from flask import Flask, render_template, request, send_file
from des import encrypt_file, decrypt_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_file():
    action = request.form['action']
    key = request.form['key']
    uploaded_file = request.files['file']

    if not uploaded_file or not key:
        return "Vui lòng chọn file và nhập key!"

    file_data = uploaded_file.read()
    filename = uploaded_file.filename

    if action == 'encrypt':
        result_data = encrypt_file(file_data, key)
        result_filename = f'encrypted_{filename}'
    else:
        result_data = decrypt_file(file_data, key)
        result_filename = f'decrypted_{filename}'

    result_path = os.path.join(RESULT_FOLDER, result_filename)
    with open(result_path, 'wb') as f:
        f.write(result_data)

    return send_file(result_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
