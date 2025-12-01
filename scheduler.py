import copy
from typing import List, Dict, Any

def parse_processes(raw):
    # Ensure pids and numeric fields
    procs = []
    for i, p in enumerate(raw, start=1):
        pid = p.get('pid') or f'P{i}'
        arrival = float(p.get('arrival', 0))
        burst = float(p.get('burst', 1))
        priority = int(p.get('priority', 0))
        procs.append({'pid': pid, 'arrival': arrival, 'burst': burst, 'priority': priority})
    # sort by arrival for deterministic behavior
    return sorted(procs, key=lambda x: x['arrival'])

def compute_metrics(processes, gantt):
    # processes: list with pid, arrival, burst
    # gantt: list of segments {'pid','start','end'}
    completion = {}
    for seg in gantt:
        completion[seg['pid']] = seg['end']
    metrics = []
    total_wt = 0
    total_tat = 0
    for p in processes:
        pid = p['pid']
        arrival = p['arrival']
        burst = p['burst']
        comp = completion.get(pid, arrival)
        tat = comp - arrival
        wt = tat - burst
        metrics.append({'pid': pid, 'arrival': arrival, 'burst': burst, 'completion': comp, 'turnaround': tat, 'waiting': wt})
        total_wt += wt
        total_tat += tat
    n = len(processes) or 1
    avg_wt = total_wt / n
    avg_tat = total_tat / n
    return metrics, avg_wt, avg_tat

def run_scheduling_algorithms(processes, algorithm='FCFS', quantum=2):
    # dispatcher
    procs = copy.deepcopy(processes)
    if algorithm.upper() == 'FCFS':
        gantt = fcfs(procs)
    elif algorithm.upper() == 'SJF':
        gantt = sjf_non_preemptive(procs)
    elif algorithm.upper() == 'RR' or algorithm.upper() == 'ROUNDROBIN':
        gantt = round_robin(procs, quantum)
    elif algorithm.upper() == 'PRIORITY':
        gantt = priority_non_preemptive(procs)
    else:
        return {'error': 'Unknown algorithm'}
    metrics, avg_wt, avg_tat = compute_metrics(processes, gantt)
    return {'gantt': gantt, 'metrics': metrics, 'avg_waiting_time': avg_wt, 'avg_turnaround_time': avg_tat}

# Algorithms
def fcfs(processes: List[Dict[str,Any]]):
    time = 0
    gantt = []
    for p in processes:
        if time < p['arrival']:
            # idle period
            gantt.append({'pid': 'IDLE', 'start': time, 'end': p['arrival']})
            time = p['arrival']
        start = time
        end = start + p['burst']
        gantt.append({'pid': p['pid'], 'start': start, 'end': end})
        time = end
    return gantt

def sjf_non_preemptive(processes: List[Dict[str,Any]]):
    procs = sorted(processes, key=lambda x: x['arrival'])
    time = 0
    gantt = []
    remaining = procs[:]
    while remaining:
        # pick arrived with smallest burst
        arrived = [p for p in remaining if p['arrival'] <= time]
        if not arrived:
            # jump to next arrival
            next_arrival = min(remaining, key=lambda x: x['arrival'])
            gantt.append({'pid': 'IDLE', 'start': time, 'end': next_arrival['arrival']})
            time = next_arrival['arrival']
            arrived = [p for p in remaining if p['arrival'] <= time]
        # choose min burst
        cur = min(arrived, key=lambda x: x['burst'])
        start = time
        end = start + cur['burst']
        gantt.append({'pid': cur['pid'], 'start': start, 'end': end})
        time = end
        remaining.remove(cur)
    return gantt

def round_robin(processes: List[Dict[str,Any]], quantum=2):
    time = 0
    gantt = []
    queue = []
    remaining = {p['pid']: p['burst'] for p in processes}
    arrivals = sorted(processes, key=lambda x: x['arrival'])
    idx = 0
    # load initial arrivals
    while idx < len(arrivals) or queue:
        while idx < len(arrivals) and arrivals[idx]['arrival'] <= time:
            queue.append(arrivals[idx])
            idx += 1
        if not queue:
            # idle until next arrival
            if idx < len(arrivals):
                gantt.append({'pid':'IDLE','start':time,'end':arrivals[idx]['arrival']})
                time = arrivals[idx]['arrival']
                continue
            else:
                break
        cur = queue.pop(0)
        pid = cur['pid']
        run = min(quantum, remaining[pid])
        start = time
        end = start + run
        gantt.append({'pid': pid, 'start': start, 'end': end})
        time = end
        remaining[pid] -= run
        # enqueue any new arrivals that came while running
        while idx < len(arrivals) and arrivals[idx]['arrival'] <= time:
            queue.append(arrivals[idx])
            idx += 1
        # requeue if still remaining
        if remaining[pid] > 0:
            # update arrival time to current time for round-robin ordering
            queue.append({'pid': pid, 'arrival': time, 'burst': remaining[pid], 'priority': cur.get('priority',0)})
    return gantt

def priority_non_preemptive(processes: List[Dict[str,Any]]):
    procs = sorted(processes, key=lambda x: x['arrival'])
    time = 0
    gantt = []
    remaining = procs[:]
    while remaining:
        arrived = [p for p in remaining if p['arrival'] <= time]
        if not arrived:
            next_arrival = min(remaining, key=lambda x: x['arrival'])
            gantt.append({'pid':'IDLE','start':time,'end':next_arrival['arrival']})
            time = next_arrival['arrival']
            arrived = [p for p in remaining if p['arrival'] <= time]
        # choose highest priority (lower number = higher priority)
        cur = min(arrived, key=lambda x: (x['priority'], x['arrival']))
        start = time
        end = start + cur['burst']
        gantt.append({'pid': cur['pid'], 'start': start, 'end': end})
        time = end
        remaining.remove(cur)
    return gantt
