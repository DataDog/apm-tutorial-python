# Unless explicitly stated otherwise all files in this repository are dual-licensed
# under the Apache 2.0 or BSD3 Licenses.
#
# This product includes software developed at Datadog (https://www.datadoghq.com/)
# Copyright 2022 Datadog, Inc.
from notes_app.notes_helper import NotesHelper
from notes_app.note import Note
from notes_app.database.sqllite_connection import SQLiteConnection
from notes_app.database.postgres_connection import PostgresConnection
import requests
import os

CALENDAR_HOST = os.getenv('CALENDAR_HOST', 'localhost')


class NotesLogic:

    def __init__(self):
        self.nh = NotesHelper()
        if os.getenv('DB_HOST') is not None:
            self.db = PostgresConnection()
        else:
            self.db = SQLiteConnection()

    def get_note(self, id):
        if id:
            note = self.db.get_notes(id)
            if not note:
                return "Note does not exist"
            return str(Note(id=note[0], description=note[1]))
        else:
            notes = self.db.get_notes()
            self.nh.long_running_process()
            self.nh.another_process()
            return notes

    def create_note(self, desc, add_date=None):
        if add_date:
            if add_date.lower() == "y":
                try:
                    self.nh.another_process()
                    note_date = requests.get(f"http://{CALENDAR_HOST}:9090/calendar")
                    note_date = note_date.text
                    desc = desc + " with date " + note_date
                    print(desc)
                except Exception as e:
                    print(e)
                    raise IOError("Cannot reach calendar service.")
        note = Note(description=desc, id=None)
        note.id = self.db.create_note(note)
        return str(note)

    def update_note(self, id, desc):
        note = Note(desc, id)
        return self.db.update_note(note)

    def delete_note(self, id):
        self.db.delete_note(id)
        return "Deleted"
