# Intelligent CPU Scheduler Simulator

A lightweight CPU scheduling simulator with real-time visualizations (Gantt chart) and performance metrics for FCFS, SJF, Round Robin, and Priority Scheduling.

## What you'll find
- A Flask-based backend (`app.py`) implementing scheduling algorithms.
- A frontend (`templates/index.html`, `static/main.js`) that allows inputting processes and visualizes Gantt charts.
- `scheduler.py` contains scheduling implementations and metrics calculation.
- `report.md` contains project overview, module breakdown, execution plan, and appendix with code references.

## How to run (local)
1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   python app.py
   ```
3. Open `http://127.0.0.1:5000` in your browser.

## GitHub Workflow (suggested)
- Create a repository and push these files.
- Suggested branches: `feature/ui`, `feature/algorithms`, `feature/visualization`.
- Make at least 7 meaningful commits (examples in `GIT_COMMITS.md`).

