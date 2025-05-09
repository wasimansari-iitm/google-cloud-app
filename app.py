from flask import Flask, request, render_template, redirect, jsonify
from google.cloud import storage
import pymysql
import random
import os

app = Flask(__name__)

# Environment variables (to be configured in Cloud Run)
DB_HOST = os.environ['DB_HOST']  # Cloud SQL Unix socket path
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']
DB_BUCKET = os.environ['DB_BUCKET']  # Cloud Storage bucket name

# Connect to Cloud SQL
def get_connection():
    return pymysql.connect(
        unix_socket=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

# Upload image to Cloud Storage and return public URL
def upload_file(source_file, dest_name):
    client = storage.Client()
    bucket = client.bucket(DB_BUCKET)
    blob = bucket.blob(f'images/{dest_name}')
    blob.upload_from_file(source_file)
    blob.make_public()
    return blob.public_url

# Generate unique filename for image
def generate_image_name(base):
    suffix = random.randint(100000, 999999)
    return f"{base}_{suffix}.jpg"

# Home route - display all journal entries
@app.route('/', methods=['GET'])
def get_journals():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM blogs ORDER BY created_at DESC;')
    posts = cursor.fetchall()
    conn.close()
    return render_template('blogs.html', blogs=posts), 200

# Create new entry - form + POST
@app.route('/blogs', methods=['GET', 'POST'])
def create_blog():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')
        image = request.files.get('image')

        if not title or not content or not author or not image:
            return jsonify({'error': 'Missing required fields'}), 400

        image_name = generate_image_name(author)
        image_url = upload_file(image, image_name)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO blogs (title, image_url, content, author)
            VALUES (%s, %s, %s, %s);
        ''', (title, image_url, content, author))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('create_blogs.html')

# Run locally (only for testing)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)