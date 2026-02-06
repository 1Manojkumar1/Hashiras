# CurrHub: AI-Powered Curriculum Generator

[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/1Manojkumar1/Hashiras)

CurrHub is a Generative AI-powered platform designed to help educators and academic institutions create future-ready, industry-aligned curricula in minutes. The application streamlines the entire development process, from generating high-level program structures to creating detailed syllabi and identifying learning resources.

## Features

-   **AI Curriculum Generation**: Leverages Google's Gemini model to produce comprehensive, semester-wise academic programs with detailed weekly topics, learning outcomes, and professional rationales.
-   **Smart Fallback System**: A robust, multi-layered generation engine ensures consistent output:
    1.  **Database-First**: Instantly retrieves pre-built curricula from a local JSON database for popular domains.
    2.  **Template-Based**: Generates structured curricula for any domain using a flexible templating system.
    3.  **AI Generation**: Calls the Gemini API for novel or highly specific requests.
    4.  **Rule-Based Fallback**: A sophisticated fallback mechanism generates a relevant, high-quality curriculum if the AI service is unavailable.
-   **Industry-Academic Gap Analyzer**: Compares a given curriculum against a real-world job description to identify skill gaps, analyze coverage, and suggest actionable improvements.
-   **Dynamic Syllabus Generator**: Instantly creates detailed, unit-wise syllabi for any course within a generated curriculum, complete with learning outcomes and reference books.
-   **Curriculum Flowchart Visualizer**: Automatically generates and displays an interactive Mermaid.js flowchart to visualize course dependencies and program structure.
-   **AI-Curated Resource Hub**: Fetches and organizes high-quality learning resources (MOOCs, books, YouTube playlists) for any course, providing a complete learning pathway.
-   **Integrated Chatbot Assistant**: An AI-powered chatbot (`CurrBot`) assists users with questions about curricula, course structures, and academic standards.
-   **Modern Web Interface**: A clean, responsive UI built with FastAPI, Jinja2 templates, and vanilla JavaScript, featuring a dark/light theme toggle.

## Architecture

The application is built on a Python backend using the FastAPI framework and a dynamic frontend. The core curriculum generation logic in `ai_engine.py` follows a prioritized, fault-tolerant sequence:

1.  **Database Lookup**: The system first attempts to find a matching curriculum in the `curriculum_database.json` file for the fastest response.
2.  **Template Generation**: If no direct match is found, it checks `curriculum_templates.py` to generate a curriculum from a pre-defined domain template. This covers a wide range of academic fields with a consistent structure.
3.  **Gemini AI Call**: For unique or specialized domains not covered by the database or templates, the system constructs a detailed prompt and queries the Google Gemini API to generate a bespoke curriculum.
4.  **Smart Fallback Generation**: If the API call fails (e.g., due to rate limits or errors), a rule-based `generate_mock_fallback` function is triggered. This function intelligently maps the requested domain to a broader category (e.g., 'AI', 'Business', 'Health') and procedurally generates a detailed and realistic curriculum, ensuring the user always receives a useful result.

Auxiliary features like the Gap Analyzer, Syllabus Generator, and Resource Hub are powered by the OpenRouter API, using `gpt-4o-mini` to provide intelligent, context-aware responses.

## Technology Stack

-   **Backend**: Python, FastAPI
-   **AI / LLMs**: Google Gemini, OpenRouter API (GPT-4o-mini)
-   **Frontend**: HTML, CSS, JavaScript
-   **Templating**: Jinja2
-   **Visualization**: Mermaid.js
-   **Deployment**: Uvicorn

## Setup and Installation

To run CurrHub locally, follow these steps:

1.  **Clone the Repository**
    ```sh
    git clone https://github.com/1manojkumar1/Hashiras.git
    cd Hashiras
    ```

2.  **Create a Virtual Environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```sh
    pip install fastapi uvicorn python-dotenv google-generativeai requests
    ```

4.  **Configure Environment Variables**
    Create a file named `.env` in the root directory and add your API keys. You can get keys from the [Google AI Studio](https://aistudio.google.com/app/apikey) and [OpenRouter.ai](https://openrouter.ai/keys).

    ```env
    # For core curriculum generation
    GOOGLE_API_KEY="your_google_api_key_here"

    # For chatbot, gap analysis, syllabus, and resource features
    OPENROUTER_API_KEY="your_openrouter_api_key_here"

    # Optional: You can use separate keys for each feature
    # If not provided, they will default to OPENROUTER_API_KEY
    GAP_API_KEY="your_openrouter_api_key_here"
    SYLLABUS_API_KEY="your_openrouter_api_key_here"
    RESOURCE_API_KEY="your_openrouter_api_key_here"
    ```

5.  **Run the Application**
    ```sh
    uvicorn main:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`.

## Usage Guide

-   **Generate a Curriculum**: Navigate to the `/generate` page, fill in the form with your desired program details, and click "Generate Curriculum".
-   **Analyze a Skill Gap**: Go to the `/gap` page. Paste a curriculum summary and a job description into the respective text areas and click "Analyze Gap".
-   **Interact with Features**: On the generated curriculum page, you can:
    -   Click **View Flowchart** to see a visual representation of the program structure.
    -   Click the **Syllabus** button on any course card to generate a detailed, unit-wise syllabus.
    -   Click the **Resources** button to get a curated list of MOOCs, books, and YouTube playlists for that course.
-   **Use the Chatbot**: Click the floating chat icon on any page to open `CurrBot` and ask questions about different academic programs.