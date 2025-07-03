from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

LOG_FILE = "search_log.txt"

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form["query"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a") as f:
            f.write(f"{timestamp} - {query}\n")
        return render_template("search.html", message="Search saved!")
    return render_template("search.html")

@app.route("/view")
def view_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()
    else:
        logs = []
    return render_template("view.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
