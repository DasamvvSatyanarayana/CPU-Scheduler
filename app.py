from flask import Flask, render_template, request, jsonify
from scheduler import run_scheduling_algorithms, parse_processes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    # expected: {"processes": [{"pid":"P1","arrival":0,"burst":5,"priority":2}, ...], "algorithm":"FCFS", "quantum":2}
    processes = parse_processes(data.get('processes', []))
    algorithm = data.get('algorithm', 'FCFS')
    quantum = int(data.get('quantum', 2))
    results = run_scheduling_algorithms(processes, algorithm, quantum)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
