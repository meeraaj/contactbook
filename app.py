from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# PostgreSQL connection setup
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        user="contact_user",
        password="xp",
        database="contacts"
    )
    return conn

# Route to view all contacts
@app.route('/all_contacts')
def all_contacts():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts')
    contacts = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('all_contacts.html', contacts=contacts)

# Route to search contact by name
@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    if request.method == 'POST':
        name = request.form['name']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM contacts WHERE name = %s', (name,))
        contacts = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('search_name.html', contacts=contacts)
    return render_template('search_name.html')

# Route to search contact by phone
@app.route('/search_phone', methods=['GET', 'POST'])
def search_phone():
    if request.method == 'POST':
        phone = request.form['phone']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM contacts WHERE phone = %s', (phone,))
        contacts = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('search_phone.html', contacts=contacts)
    return render_template('search_phone.html')

# Route to search contact by email
@app.route('/search_email', methods=['GET', 'POST'])
def search_email():
    if request.method == 'POST':
        email = request.form['email']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM contacts WHERE email = %s', (email,))
        contacts = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('search_email.html', contacts=contacts)
    return render_template('search_email.html')

# Route to delete contact by name
@app.route('/delete_name', methods=['GET', 'POST'])
def delete_name():
    if request.method == 'POST':
        name = request.form['name']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM contacts WHERE name = %s', (name,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('all_contacts'))
    return render_template('delete_name.html')

# Route to add a new contact
@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO contacts (name, phone, email, address) VALUES (%s, %s, %s, %s)',
            (name, phone, email, address)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('all_contacts'))
    return render_template('add_contact.html')

# Home route
@app.route('/')
def index():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
