Simulation Runner/Analyzer
Design a system to run and analyze the results of simulations with the following constraints:
A simulation runtime takes as input:
An AV stack runtime. The code that we are testing against (a binary).
A 'scene', ie a test definition that describes what is being tested (eg an AV driving down the Embarcadero at 10:00AM with no/minimal traffic) and how to analyze results (eg did the AV perform as expected at stop signs/lights?).
Zero or more artifacts. These might be used to hydrate the simulation with information that it needs to run (for eg sensor data from a real world drive of the AV). These can be large (on the order of gigabytes).
A simulation returns:
A binary pass/fail result (did the simulation run without errors?).
A collection of scores. A score is a name/value pair where the value is a float between 0 and 1. This is used to understand the performance of a particular AV maneuver/activity (eg safe_stops).
Zero or more artifacts that describe the results of the simulation. These can be large (on the order of gigabytes). For example, a simulation might return an artifact containing telemetry (eg speed) on a 'per-tick' (eg per ms) basis.
Simulations generally run on GPU servers. For cost/capacity reasons we have a limited number of machines that we can run GPU workloads on (5k servers).
Functional Requirements
I need the ability to:
Run a collection of simulations in the cloud.
Analyze the scores from a simulation over time (eg last 30 days).
Analyze the scores from a simulation run relative to its previous run (score different over last 30 days).
Analyze aggregate information (MIN/MAX/AVG/SUM) of a score over the last 30 days.
Analyze the raw results (eg speed per ms) of a simulation.


Non Functional Requirements
Scale:
2 million simulations/day, with peak volume of 500k requested simulations.
2 / 10 ^ 5 = 20 request per sec
500k -> scale out (message queue, worker)
Ingest 50 million simulation results (scores) per day, with peak ingest throughput of 10 million results.
Write heavy -> NoSQL 
Retention:
We need to retain at least one quarter of simulation results.
S3, object store, quarterly scheduled  jobs to clean up
Offline analyze:
Hadoop, mapreduce, (cron jobs)
Online analyze:
spark
Search:
Elastic


—-----------------





