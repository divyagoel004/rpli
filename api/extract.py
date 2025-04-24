
from flask import Flask, request
import pdfplumber
from io import BytesIO
import requests

app = Flask(__name__)

@app.route('/extract', methods=['POST'])
def extract_pdf_text():
    data = request.json
    url = data['url']
    pdf_data = requests.get(url).content
    with pdfplumber.open(BytesIO(pdf_data)) as pdf:
        text = "\n".join((page.extract_text() or "") for page in pdf.pages)
    return {'text': text[:1000]}  # First 1000 characters

if __name__ == '__main__':
    app.run()
