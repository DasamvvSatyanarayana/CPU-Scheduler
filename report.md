# Project Report - Intelligent CPU Scheduler Simulator

## 1. Project Overview
**Goals:** Build an interactive simulator that demonstrates CPU scheduling algorithms (FCFS, SJF, Round Robin, Priority). The simulator should accept process inputs (arrival time, burst time, priority), run selected algorithms, show Gantt charts and compute performance metrics (waiting time, turnaround time).

**Expected Outcomes:** A working web-app prototype, source code, a project report, and a clear Git revision history.

**Scope:** Core scheduling algorithms (non-preemptive FCFS/SJF/Priority, preemptive Round Robin). Visualizations are confined to a single-page web app with JSON-based backend responses.

## 2. Module-Wise Breakdown
1. **Backend (app + scheduler)**  
   - Purpose: Implement algorithms and expose API endpoints for simulation.  
   - Roles: parse inputs, execute selected algorithm, compute metrics, return JSON.

2. **Frontend (HTML/JS)**  
   - Purpose: Provide UI for input, show Gantt chart and metrics.  
   - Roles: form for processes, algorithm selection, rendering Gantt.

3. **Documentation & DevOps (report + GitHub)**  
   - Purpose: Project report, version control, and evaluation artifacts.  
   - Roles: README, report, git commit history, instructions for grading.

## 3. Functionalities
- Add/Edit/Delete processes (PID, arrival, burst, priority).
- Choose algorithm (FCFS, SJF, RR, Priority) and set quantum for RR.
- Visualize Gantt chart with time segments and idle periods.
- Show per-process metrics and overall average waiting/turnaround times.
- Export/Import sample process lists (JSON).

## 4. Technology Used
- **Programming Languages:** Python (Flask) for backend, HTML/CSS/JavaScript for frontend.
- **Libraries and Tools:** Flask, standard library only.
- **Other Tools:** Git/GitHub for revision tracking.

## 5. Flow Diagram
(Use a flow diagram tool or draw by hand — typical flow:)
1. User enters processes -> 2. Frontend sends JSON to `/simulate` -> 3. Backend runs algorithm -> 4. Backend returns Gantt + metrics -> 5. Frontend visualizes.

## 6. Revision Tracking on GitHub
- Repository Name: `intelligent-cpu-scheduler-simulator`
- GitHub Link: [Insert Link]
- See `GIT_COMMITS.md` for suggested commit messages.

## 7. Conclusion and Future Scope
- Add preemptive SJF and Priority algorithms.
- Add comparisons across algorithms with benchmark datasets.
- Add exportable reports (CSV/PDF).
- Add themes, accessibility improvements, and unit tests.

## 8. References
- Operating Systems textbooks and lecture notes on CPU scheduling.
- Online resources for Gantt chart visualizations.

## Appendix
### A. AI-Generated Project Elaboration/Breakdown Report
(Include expansion of the modules and design decisions.)  
- Backend API design: `/simulate` POST -> returns `{gantt: [...], metrics: [...], avg_waiting_time, avg_turnaround_time}`
- Data model: Process -> {pid, arrival, burst, priority}
- Gantt model: Sequence of segments -> {pid, start, end}

### B. Problem Statement
Intelligent CPU Scheduler Simulator  
Develop a simulator for CPU scheduling algorithms (FCFS, SJF, Round Robin, Priority Scheduling) with real-time visualizations. The simulator should allow users to input processes with arrival times, burst times, and priorities and visualize Gantt charts and performance metrics like average waiting time and turnaround time.

### C. Solution / Code
All project code is included in the repository files.

