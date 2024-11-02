# contact.py

import psycopg2

# PostgreSQL database connection setup
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        user="contact_user",
        password="your_password",
        database="contacts_db"
    )
    return conn

def add_contact(name, phone, email, address):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO contacts (name, phone, email, address) VALUES (%s, %s, %s, %s)',
        (name, phone, email, address)
    )
    conn.commit()
    cur.close()
    conn.close()

def delete_contact(contact_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM contacts WHERE id = %s', (contact_id,))
    conn.commit()
    cur.close()
    conn.close()

def search_contact(name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts WHERE name = %s', (name,))
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
