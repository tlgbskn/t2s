import pdfplumber as pp
from gtts import gTTS
import os

# Function to process PDF to audio
def pdf_to_audio(pdf_file, output_audio, language='en'):
    pdf_text = ''
    try:
        with pp.open(pdf_file) as pdf:
            # Iterate over all pages in the PDF
            for page_num, page in enumerate(pdf.pages, start=1):
                page_text = page.extract_text()
                if page_text:
                    pdf_text += page_text
                    print(f"Extracted text from page {page_num}")
                else:
                    print(f"Warning: No text found on page {page_num}")
        
        if pdf_text:
            # Convert extracted text to speech
            tts = gTTS(text=pdf_text, lang=language)
            tts.save(output_audio)
            print(f"Audio saved as {output_audio}")
        else:
            print("No text extracted from the PDF.")
    
    except FileNotFoundError:
        print(f"Error: The file {pdf_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
pdf_file = 'deneme2.pdf'  # Replace with your PDF file path
output_audio = 'audio_book.mp3'
language = 'en'  # Change the language if necessary

pdf_to_audio(pdf_file, output_audio, language)
