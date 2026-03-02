# Package Tracker - A simple Flask web application
# Introduction to Engineering - Software Engineering Unit - Day 1 Lab

from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    """Create the packages table if it doesn't exist"""
    conn = sqlite3.connect('packages.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS packages
                 (tracking_number TEXT PRIMARY KEY, 
                  status TEXT, 
                  timestamp TEXT)''')
    conn.commit()
    conn.close()
    print("Database initialized!")

# TODO: Students will add the add_sample_data() function here in Part 3

@app.route('/')
def home():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/track', methods=['POST'])
def track_package():
    """
    API endpoint to track a package by tracking number.
    Receives JSON with tracking_number, returns status and timestamp.
    """
    tracking_num = request.json.get('tracking_number')
    
    # Query the database
    conn = sqlite3.connect('packages.db')
    c = conn.cursor()
    c.execute("SELECT * FROM packages WHERE tracking_number=?", (tracking_num,))
    result = c.fetchone()
    conn.close()
    
    if result:
        return jsonify({
            'status': result[1], 
            'last_update': result[2]
        })
    else:
        return jsonify({
            'status': 'Not found', 
            'last_update': 'N/A'
        })

if __name__ == '__main__':
    init_db()
    # TODO: Students will call add_sample_data() here in Part 3
    app.run(debug=True, port=5050)
