from flask import Flask, render_template, request, jsonify
from utils.Model import PDFReader, GeminiModel
from werkzeug.utils import secure_filename
import os
import tempfile

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/extract', methods=['POST'])
def extract():
    file = request.files.get('pdf_file')
    if not file:
        return jsonify({'error': 'No file or text uploaded'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    reader = PDFReader(file_path, gemini_key_path='private/gemini.key')
    text_content = reader.get_content()
    
    return jsonify({'text': text_content,})

@app.route('/api/summarize', methods=['POST'])
def summarize():
    lang = request.form.get('language', 'Vietnamese')
    limit = request.form.get('summary_length', 'Long (~200 words)')

    cv_text = request.form.get('cv_text', '').strip()
    if cv_text:
        reader = GeminiModel(key_path='private/gemini.key')
        
        summary = reader.summary(cv_text, lang, limit)
        
        return jsonify({
            'summary': summary,
            'match_analysis': 'Matching will be implemented.'
        })

    file = request.files.get('pdf_file')
    if not file:
        return jsonify({'error': 'No file or text uploaded'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    reader = PDFReader(file_path, gemini_key_path='private/gemini.key')
    summary = reader.summary(lang, limit)

    return jsonify({
        'summary': summary,
        'match_analysis': 'Matching will be implemented.'
    })

def match_analysis():
    pass

if __name__ == '__main__':
    app.run(debug=True)
