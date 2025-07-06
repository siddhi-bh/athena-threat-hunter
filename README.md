# ATHENA – Threat Log Analysis Dashboard

**ATHENA** is a simple and beginner-friendly threat hunting dashboard. It helps detect suspicious patterns in system log files, such as failed login attempts, use of `sudo`, or risky permissions like `chmod 777`. Built using Python (FastAPI) for the backend and React (Vite) for the frontend, it’s designed to help students and learners understand basic log analysis.

---

## Features

- Detects suspicious log entries
- Upload `.log` files and analyze them in real time
- Displays file name and upload timestamp
- Option to export only the suspicious entries
- Clean and responsive UI

---

## How It Works

1. You upload a `.log` file through the interface.
2. The backend scans each line for common patterns:
   - `Failed password`
   - `sudo`
   - `chmod 777`
3. Suspicious lines are extracted and displayed in the dashboard.

---

## Tech Stack

- **Frontend**: React (Vite), JavaScript, Axios
- **Backend**: Python, FastAPI, Uvicorn
- **Styling**: Basic CSS, no external frameworks

---

## Getting Started (Run Locally)

### 1. Clone the Repository

```bash
git clone https://github.com/siddhi-bh/athena-threat-hunter.git
cd athena-threat-hunter

Backend Setup (Python)
bash

cd backend
pip install -r requirements.txt
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000

 Frontend Setup (React)
bash

cd ../frontend
npm install
npm run dev
The app will run at http://localhost:5173

Folder Structure
bash

athena-threat-hunter/
├── backend/     # FastAPI backend logic
├── frontend/    # React frontend interface
├── docker/      # Docker setup (optional)
├── .gitignore
├── README.md

Contributing
This project is open to suggestions or improvements. Feel free to fork it, open an issue, or submit a pull request.

