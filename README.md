# Package Tracker Lab

A simple Flask web application for tracking packages. Built for Introduction to Engineering - Software Engineering Unit - Day 1 Lab.

## What This App Does

This is a basic package tracking system similar to what UPS or FedEx uses. Users can:
- Enter a tracking number
- See the package status
- See when it was last updated

## Project Structure

```
package-tracker-lab/
├── app.py                  # Flask backend (Python)
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Frontend (HTML + JavaScript)
└── README.md              # This file
```

## Technologies Used

This app demonstrates the **software stack** concept by using multiple technologies working together:

- **Python 3.x** - Backend programming language
- **Flask** - Web framework (library that handles HTTP requests)
- **SQLite** - Database (stores package information)
- **HTML** - Frontend structure
- **JavaScript** - Frontend interactivity
- **CSS** - Frontend styling

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- A web browser
- Internet connection (for initial setup)

## Setup Instructions

### 1. Clone or Download

If using Git:
```bash
git clone [YOUR-REPO-URL]
cd package-tracker-lab
```

If downloading as ZIP:
- Download and unzip to your Desktop
- Open Terminal/Command Prompt
- Navigate to the folder: `cd Desktop/package-tracker-lab`

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or if that doesn't work:
```bash
pip3 install -r requirements.txt
```

This installs Flask and all its dependencies.

### 3. Run the Application

```bash
python app.py
```

Or:
```bash
python3 app.py
```

You should see:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 4. Open in Browser

Open your web browser and go to:
```
http://localhost:5000
```

Or:
```
http://127.0.0.1:5000
```

## Using the App

Currently, the database is empty. If you try to track a package, you'll see "Not found."

**In Part 3 of the lab**, you'll add sample data so the app can track packages like:
- `ABC123` - In Transit
- `XYZ789` - Delivered

## How It Works

### The Software Stack

```
┌─────────────────────┐
│   Web Browser       │  ← What you see (HTML/CSS/JavaScript)
└─────────┬───────────┘
          │ HTTP requests
┌─────────▼───────────┐
│   Flask Server      │  ← Backend logic (Python)
│      (app.py)       │
└─────────┬───────────┘
          │ SQL queries
┌─────────▼───────────┐
│  SQLite Database    │  ← Data storage (packages.db)
│   (packages.db)     │
└─────────────────────┘
```

### Request Flow

1. User enters tracking number in browser
2. JavaScript sends HTTP POST request to `/api/track`
3. Flask receives request, queries SQLite database
4. Database returns package info (or null if not found)
5. Flask sends JSON response back to browser
6. JavaScript displays result to user

## Files Explained

### app.py (Backend)
- Creates Flask web server
- Initializes SQLite database
- Defines API routes:
  - `/` - Serves the HTML page
  - `/api/track` - Accepts tracking number, returns status

### requirements.txt
- Lists Python packages needed
- Used by `pip install -r requirements.txt`

### templates/index.html (Frontend)
- HTML structure (headings, input box, button)
- CSS styling (colors, layout)
- JavaScript (handles button clicks, makes API calls)

## Common Issues

### "pip: command not found"
Try `pip3` instead of `pip`

### "Permission denied"
Add `--user` flag: `pip install -r requirements.txt --user`

### Port 5000 already in use
Something else is using port 5000. Either:
- Stop the other application
- Change the port in `app.py`: `app.run(debug=True, port=5001)`

### Browser shows "This site can't be reached"
Make sure the Flask server is running in the terminal. You should see the "Running on..." message.

## Learning Objectives

This lab demonstrates:
1. **Programming Languages** - Python, JavaScript, HTML, CSS, SQL working together
2. **Libraries/Frameworks** - Using Flask instead of writing HTTP server from scratch
3. **Databases** - Persistent storage with SQLite
4. **APIs** - Frontend communicating with backend via HTTP
5. **Client-Server Architecture** - Browser (client) talking to Flask (server)

## Next Steps

After completing the basic lab, try these challenges:
- Add more package data
- Display all packages in a list
- Add package details (weight, destination, carrier)
- Style the page differently
- Add a map showing package location

## License

This project is for educational purposes as part of the Introduction to Engineering course at Junipero Serra High School.

## Questions?

Ask your teacher for help during lab time!
