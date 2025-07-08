from flask import Flask, render_template, request, jsonify
from utils.Model import PDFReader
from werkzeug.utils import secure_filename
import os
import tempfile

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    file = request.files.get('file')
    lang = request.form.get('language', 'vie')
    limit = request.form.get('limit', '500')
    api_key = request.form.get('api_key', '')

    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    reader = PDFReader(file_path, gemini_key_path='private/gemini.key', lang=lang)
    if api_key:
        reader._PDFReader__ai.set_key(api_key)
    summary = reader.summary(limit)
    text_content = reader.get_content()

    return jsonify({
        'summary': summary,
        'text': text_content
    })

if __name__ == '__main__':
    app.run(debug=True)
