# Unless explicitly stated otherwise all files in this repository are dual-licensed
# under the Apache 2.0 or BSD3 Licenses.
#
# This product includes software developed at Datadog (https://www.datadoghq.com/)
# Copyright 2022 Datadog, Inc.
import sqlite3
import logging


class SQLiteConnection:

    def __init__(self):

        self.connection = sqlite3.connect(":memory:", check_same_thread=False)
        cursor = self.connection.cursor()

        create_table_query = '''CREATE TABLE notes (id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT NOT NULL);'''
        # Execute a command: this creates a new table
        logging.info("Creating notes table.")
        try:
            cursor.execute(create_table_query)
            self.connection.commit()
            logging.info("Table created successfully in SQLite3")
            cursor.close()
        except Exception as e:
            print(e)
            self.connection.rollback()
            cursor.close()
            logging.info("Table already exists.")

    def create_note(self, note):
        try:
            cursor = self.connection.cursor()
            sql = """INSERT INTO notes(description) VALUES (?);"""
            cursor.execute(sql, (note.description,))
            self.connection.commit()
            logging.info(f"Created note with id: {note.id}")
            return cursor.lastrowid
        except Exception as e:
            logging.error(e)
            self.connection.rollback()
        finally:
            cursor.close()

    def update_note(self, note):
        try:
            cursor = self.connection.cursor()
            sql = """UPDATE notes SET description = ? WHERE id = ?"""
            cursor.execute(sql, (note.description, note.id))
            self.connection.commit()
            cursor.close()
            logging.info(f"Updated note with id: {note.id}")
            return str(note)
        except Exception as e:
            logging.error(e)
            self.connection.rollback()
            cursor.close()

    def get_notes(self, id=None):
        cursor = self.connection.cursor()
        if id:
            try:
                query = "SELECT id, description FROM notes WHERE id = ?"
                cursor.execute(query, [id])
                note = cursor.fetchone()
                cursor.close()
                return note
            except:
                cursor.close()
                logging.error(f"Couldn't get note with id: {id}")
                return None
        else:
            try:
                query = "SELECT id, description FROM notes ORDER BY id"
                cursor.execute(query)
                notes = cursor.fetchall()
                cursor.close()
                response = {}
                for note in notes:
                    response[note[0]] = note[1]
                return response
            except Exception as e:
                print(e)
                cursor.close()
                logging.error(f"Couldn't get notes")
                return None

    def delete_note(self, id):
        try:
            cursor = self.connection.cursor()
            sql = """DELETE FROM notes WHERE id = ?"""
            cursor.execute(sql, (id,))
            self.connection.commit()
            cursor.close()
            logging.info(f"Deleted note with id: {id}")
        except:
            self.connection.rollback()
            cursor.close()
