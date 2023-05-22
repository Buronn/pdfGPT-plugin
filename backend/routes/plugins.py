import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

from flask import request, Blueprint, send_from_directory, jsonify
from werkzeug.datastructures import FileStorage

import functions.pdf as pdf

plugins = Blueprint("plugins", __name__)


@plugins.route("/pdf/load", methods=["POST"])
def load_pdf():
    try:
        data = request.get_json()
        url = data.get('pdf_url')
        if not url:
            return jsonify({"error": "URL not specified"}), 400
        pdf.download_pdf(url, 'corpus.pdf')
        pdf.load_recommender('corpus.pdf')
        return jsonify({"message": "PDF loaded"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@plugins.route("/pdf/query", methods=["POST"])
def query_pdf():
    try:
        data = request.get_json()
        question = data.get('query')
        url = data.get('pdf_url')
        if not question or not url:
            return jsonify({"error": "Question or URL not specified"}), 400
        pdf.download_pdf(url, 'corpus.pdf')
        pdf.load_recommender('corpus.pdf')
        openAI_key = pdf.load_openai_key()
        answer = pdf.generate_answer(question, openAI_key)
        return jsonify({"results": [answer]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@plugins.route('/.well-known/<path:path>', methods=['GET'])
def serve_file(path):
    return send_from_directory('static', path)


@plugins.route('/<path:path>', methods=['GET'])
def serve_file2(path):
    return send_from_directory('static', path)
