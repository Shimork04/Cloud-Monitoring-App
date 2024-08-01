#  monitoring applicaiton
import psutil   # library for checking cpu utilization
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

# function that will check and show cpu and memory utilization percentage
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        Message = "Warning: High CPU Utilization detected. Please Scale up!"
        Message = "Warning: High Memory Utilization detected. Please Scale up!"
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=Message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')