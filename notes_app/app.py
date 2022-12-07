# Unless explicitly stated otherwise all files in this repository are dual-licensed
# under the Apache 2.0 or BSD3 Licenses.
#
# This product includes software developed at Datadog (https://www.datadoghq.com/)
# Copyright 2022 Datadog, Inc.
from notes_app.notes_logic import NotesLogic
from flask import Flask, request

app = Flask(__name__)

note_handler = NotesLogic()


@app.route('/')
def index():
    return "Welcome to our notes app!"


@app.route('/notes', methods=['GET'])
def get_notes():
    id = request.args.get('id')
    return note_handler.get_note(id)


@app.route('/notes', methods=['POST'])
def create_note():
    desc = request.args.get('desc')
    add_date = request.args.get('add_date')
    return note_handler.create_note(desc, add_date)


@app.route('/notes', methods=['PUT'])
def update_note():
    id = request.args.get('id')
    desc = request.args.get('desc')
    return note_handler.update_note(id, desc)


@app.route('/notes', methods=['DELETE'])
def delete_note():
    id = request.args.get('id')
    return note_handler.delete_note(id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
