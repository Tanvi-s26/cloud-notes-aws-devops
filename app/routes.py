from flask import Blueprint, request, jsonify
from app.models import add_note, get_notes

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({
        "message": "Cloud Notes API is running 🚀",
        "endpoints": ["/add-note", "/notes", "/status"]
    })


@main.route('/status')
def status():
    return jsonify({
        "status": "OK",
        "message": "Service is healthy"
    })


@main.route('/add-note', methods=['POST'])
def create_note():
    data = request.get_json()

    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({"error": "Missing data"}), 400

    note = add_note(title, content)

    return jsonify({
        "message": "Note added successfully",
        "note": note
    })


@main.route('/notes')
def list_notes():
    return jsonify({
        "notes": get_notes()
    })