import os
from flask import Flask, render_template, request, send_file
import pdfplumber
from gtts import gTTS

app = Flask(__name__)

# Ana sayfa, dosya yükleme formunu gösterecek
@app.route('/')
def index():
    return render_template('index.html')

# Yüklenen PDF dosyasını işleyip ses dosyasına dönüştüren ve indirilmesini sağlayan fonksiyon
@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf_file' not in request.files:
        return "No file part", 400

    file = request.files['pdf_file']
    if file.filename == '':
        return "No selected file", 400

    if file and file.filename.endswith('.pdf'):
        # PDF'i okuma ve metni çıkarma
        with pdfplumber.open(file) as pdf:
            pdf_text = ''
            for page in pdf.pages:
                pdf_text += page.extract_text()

        if pdf_text:
            # Metni sese dönüştürme
            tts = gTTS(text=pdf_text, lang='en')
            output_file = "output_audio.mp3"
            tts.save(output_file)

            # Kullanıcıya ses dosyasını indirme bağlantısı sağlama
            return send_file(output_file, as_attachment=True)

    return "Invalid file format", 400

if __name__ == '__main__':
    # Flask uygulamasını çalıştır
    app.run(debug=True)
