# Solution - Part 3 Code

This file shows what students will add to `app.py` in Part 3 of the lab.

## Function to Add (After init_db function)

```python
def add_sample_data():
    """Add sample package data for testing"""
    conn = sqlite3.connect('packages.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO packages VALUES (?, ?, ?)",
              ('ABC123', 'In Transit', '2025-02-23 10:30 AM'))
    c.execute("INSERT OR IGNORE INTO packages VALUES (?, ?, ?)",
              ('XYZ789', 'Delivered', '2025-02-22 3:45 PM'))
    conn.commit()
    conn.close()
    print("Sample data added!")
```

## Modified Main Block

```python
if __name__ == '__main__':
    init_db()
    add_sample_data()  # ADD THIS LINE
    app.run(debug=True, port=5000)
```

## Complete app.py (After Part 3)

```python
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

def add_sample_data():
    """Add sample package data for testing"""
    conn = sqlite3.connect('packages.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO packages VALUES (?, ?, ?)",
              ('ABC123', 'In Transit', '2025-02-23 10:30 AM'))
    c.execute("INSERT OR IGNORE INTO packages VALUES (?, ?, ?)",
              ('XYZ789', 'Delivered', '2025-02-22 3:45 PM'))
    conn.commit()
    conn.close()
    print("Sample data added!")

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
    add_sample_data()
    app.run(debug=True, port=5000)
```

## Challenge Solutions

### Easy Challenge: Add Another Package

Add this line to `add_sample_data()`:
```python
c.execute("INSERT OR IGNORE INTO packages VALUES (?, ?, ?)",
          ('DEF456', 'Out for Delivery', '2025-02-24 8:15 AM'))
```

### Medium Challenge: Change Appearance

In `templates/index.html`, modify the result div styling:
```css
#result.success {
    background-color: #d4edda;
    border: 1px solid #c3e6cb;
    color: #155724;
    display: block;
    font-size: 20px;  /* Make text larger */
}
```

### Hard Challenge: Show All Packages

Add this route to `app.py`:
```python
@app.route('/api/all', methods=['GET'])
def get_all_packages():
    """Return all packages in the database"""
    conn = sqlite3.connect('packages.db')
    c = conn.cursor()
    c.execute("SELECT * FROM packages")
    results = c.fetchall()
    conn.close()
    
    packages = []
    for row in results:
        packages.append({
            'tracking_number': row[0],
            'status': row[1],
            'last_update': row[2]
        })
    
    return jsonify({'packages': packages})
```

Add this to `templates/index.html` (after the Track button):
```html
<button onclick="showAllPackages()">Show All Packages</button>

<script>
function showAllPackages() {
    fetch('/api/all')
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.className = 'success';
        
        let html = '<strong>All Packages:</strong><br><br>';
        data.packages.forEach(pkg => {
            html += `📦 ${pkg.tracking_number}: ${pkg.status} (${pkg.last_update})<br>`;
        });
        
        resultDiv.innerHTML = html;
    });
}
</script>
```
