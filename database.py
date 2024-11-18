# database.py
import sqlite3
from contact import Contact

DATABASE_NAME = "contacts.db"

def create_db():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            telephone TEXT NOT NULL,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_contact(contact):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO contacts (nom, prenom, telephone, email) VALUES (?, ?, ?, ?)",
              (contact.nom, contact.prenom, contact.telephone, contact.email))
    conn.commit()
    conn.close()

def update_contact(contact):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''UPDATE contacts SET nom=?, prenom=?, telephone=?, email=? WHERE id=?''',
              (contact.nom, contact.prenom, contact.telephone, contact.email, contact.id))
    conn.commit()
    conn.close()

def delete_contact(contact_id):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM contacts WHERE id=?', (contact_id,))
    conn.commit()
    conn.close()

def get_all_contacts():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    rows = c.fetchall()
    conn.close()
    return [Contact(id=row[0], nom=row[1], prenom=row[2], telephone=row[3], email=row[4]) for row in rows]

def search_contacts(query):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE nom LIKE ? OR prenom LIKE ? OR telephone LIKE ?", 
              ('%' + query + '%', '%' + query + '%', '%' + query + '%'))
    rows = c.fetchall()
    conn.close()
    return [Contact(id=row[0], nom=row[1], prenom=row[2], telephone=row[3], email=row[4]) for row in rows]
