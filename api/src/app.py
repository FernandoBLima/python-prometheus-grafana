from flask import Response, Flask, request
import prometheus_client
# from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge, Info
import random

import time

app = Flask(__name__)

_INF = float("inf")

graphs = {}
graphs['c'] = Counter('python_request_operations_total', 'The total number of processed requests')
graphs['h'] = Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds.', buckets=(1, 2, 5, 6, 10, _INF))
graphs['s'] = Summary('python_request_processing_seconds', 'Time spent processing request')
graphs['info'] = Info('my_build_version', 'Description of info')

@app.route("/")
def index():
    start = time.time()
    graphs['c'].inc()
    
    time.sleep(random.uniform(0, 1))
    end = time.time()

    graphs['s'].observe(end - start) 
    graphs['h'].observe(end - start)
    return "Hello World!"

@app.route("/metrics")
def requests_count():
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )