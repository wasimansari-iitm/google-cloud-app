# 📝 Blog App on Google Cloud 🚀

Welcome to the **Blog App** — a simple yet powerful journal-style application deployed on **Google Cloud Run** 🌐. Users can create and view blog posts with image uploads, thanks to seamless integration with multiple Google Cloud services.

🔗 **Live App:** [Visit the Blog App](https://blog-app-699175796072.asia-south2.run.app)

---

## 🌟 Features

- 🖼 Upload blog posts with images
- 🧑‍💻 Add your name, title, and content
- 📚 View all posts in reverse chronological order

---

## 🛠 Google Cloud Skills Demonstrated

### 1. ☁️ **Google Cloud Run**
- Deployed the Flask app as a containerized service using **Cloud Run**
- Automatically scaled with HTTP traffic
- Secured via HTTPS out-of-the-box

### 2. 🗃 **Google Cloud SQL**
- Used **Cloud SQL (MySQL)** for persistent and structured storage of blog entries
- Accessed using **Unix socket** connection from the backend securely

### 3. 🧺 **Google Cloud Storage**
- Uploaded and stored blog images in **Cloud Storage buckets**
- Generated public URLs for images to embed them in posts

### 4. 🔐 **Environment Variables**
- Used secure environment variables in Cloud Run to store DB and bucket configs

---

## 🧰 Tech Stack

- `Python` 🐍
- `Flask` 🔥
- `Google Cloud SQL (MySQL)` 🐬
- `Google Cloud Storage` 🧺
- `Google Cloud Run` 🚀
- `HTML + CSS` for frontend templating 🎨

---

## 🧪 Run Locally (for testing)

```bash
export DB_HOST='your-cloud-sql-unix-socket-path'
export DB_USER='your-db-user'
export DB_PASSWORD='your-db-password'
export DB_NAME='your-db-name'
export DB_BUCKET='your-bucket-name'

python app.py
```

---

## 📦 Deploying to Cloud Run (Overview)

- Dockerize the Flask app 🐳
- Push to Google Container Registry 📤
- Deploy with gcloud run deploy 🌍
- Configure environment variables 🔧

---

## 🙌 Acknowledgements

- Thanks to Google Cloud for providing such amazing tools for building and deploying apps at scale.

- Many thanks to Mr. Adarsh Madre (adarsh@study.iitm.ac.in) for amazing webinar on "Understanding of Google Cloud Platform" [GitHub](https://github.com/Adarsh7448/cloud-gcp)

---