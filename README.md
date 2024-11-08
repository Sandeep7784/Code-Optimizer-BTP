# Code Optimizer

## Overview
Code Optimizer is a project aimed at optimizing code for better performance and efficiency. This repository contains both the frontend and backend components of the application.

## Prerequisites
- Node.js (for frontend)
- Python 3.x (for backend)
- Virtual environment tool (e.g., `venv` for Python)
- WSL (Windows Subsystem for Linux) if using Windows

## Frontend Setup
1. Navigate to the frontend directory:
    ```sh
    cd frontend
    ```
2. Install the necessary npm packages:
    ```sh
    npm install
    ```
3. Run the development server:
    ```sh
    npm run dev
    ```
4. The frontend will be running at `http://localhost:5173`.

## Backend Setup
1. Navigate to the backend directory:
    ```sh
    cd backend
    ```
2. Create a virtual environment:
    - On Ubuntu:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    - On Windows (using WSL with Ubuntu):
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up environment variables:
    - Create a `.env` file in the root directory
    - Add the following API key:
        ```
        GROQ_API_KEY=your_groq_api_key
        ```
    - Replace `your_groq_api_key` with your actual GROQ API key

5. Run the FastAPI backend:
    ```sh
    python main.py
    ```

6. The backend will be running at 
    ```sh
    http://localhost:8080
    ```

