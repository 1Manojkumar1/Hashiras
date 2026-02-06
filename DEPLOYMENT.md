# 🚀 Deploying CurrHub

This guide will help you deploy the CurrHub application to the web so others can access it. We recommend **Render** or **Railway** for the easiest experience.

## Option 1: Deploy on Render (Recommended)

Render is a cloud provider that offers a free tier for web services.

1.  **Push your code to GitHub**
    - Ensure your project is in a GitHub repository.
    - Make sure `requirements.txt` and `Procfile` are in the root directory (we've created these for you!).

2.  **Sign up for Render**
    - Go to [render.com](https://render.com) and sign up/login with GitHub.

3.  **Create a New Web Service**
    - Click **"New +"** -> **"Web Service"**.
    - Connect your GitHub repository.

4.  **Configure Settings**
    - **Name**: `currhub-demo` (or any name)
    - **Region**: Closest to you (e.g., Singapore, Oregon)
    - **Runtime**: `Python 3`
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
    - **Plan**: Free

5.  **Environment Variables (CRITICAL)**
    - Scroll down to "Environment Variables" and click **"Add Environment Variable"**.
    - Add all keys from your local `.env` file:
        - `GOOGLE_API_KEY`: `your_key_value`
        - `OPENROUTER_API_KEY`: `your_key_value`
        - `SYLLABUS_API_KEY`: `your_key_value`
        - `RESOURCE_API_KEY`: `your_key_value`
        - `GAP_API_KEY`: `your_key_value`

6.  **Deploy**
    - Click **"Create Web Service"**.
    - Render will build your app. Once done, you'll get a URL like `https://currhub-demo.onrender.com`.

---

## Option 2: Run with Docker

If you prefer using Docker containers:

1.  **Create a Dockerfile** (if not present) with this content:
    ```dockerfile
    FROM python:3.9-slim
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    COPY . .
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    ```

2.  **Build the Image**
    ```bash
    docker build -t currhub .
    ```

3.  **Run the Container**
    ```bash
    docker run -p 8000:8000 --env-file .env currhub
    ```

---

## Troubleshooting

-   **502 Bad Gateway / Application Error**: usually means the Start Command is wrong. Ensure it is `uvicorn main:app --host 0.0.0.0 --port $PORT`.
-   **API Errors**: Double-check your Environment Variables in the cloud dashboard. They must match your `.env` exactly.
