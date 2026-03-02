# Teacher Setup Guide - Package Tracker Lab

## Quick Start - Testing the App Yourself

1. **Navigate to the project folder:**
   ```bash
   cd package-tracker-lab
   ```

2. **Install Flask:**
   ```bash
   pip install -r requirements.txt
   ```
   (or `pip3 install -r requirements.txt`)

3. **Run the app:**
   ```bash
   python app.py
   ```
   (or `python3 app.py`)

4. **Open browser to:** `http://localhost:5000`

5. **Test it:**
   - Try tracking "ABC123" - should show "Not found" (database is empty)
   - Stop the server (CTRL+C)
   - Uncomment the solution code in SOLUTION.md or manually add sample data
   - Run again
   - Now "ABC123" should show "In Transit"

---

## Pushing to GitHub

### Option 1: Create New Repository on GitHub

1. Go to github.com and create a new repository (e.g., "package-tracker-lab")
2. DON'T initialize with README (we already have one)
3. Copy the repository URL

4. In your terminal:
   ```bash
   cd package-tracker-lab
   git init
   git add .
   git commit -m "Initial commit - Package Tracker Lab"
   git branch -M main
   git remote add origin [YOUR-REPO-URL]
   git push -u origin main
   ```

### Option 2: Using GitHub Desktop

1. Open GitHub Desktop
2. File → Add Local Repository
3. Select the package-tracker-lab folder
4. Click "Publish repository"
5. Make sure "Keep this code private" is UNCHECKED (so students can clone it)

---

## Sharing with Students

### Method 1: Direct Clone URL
Give students the clone URL:
```
https://github.com/[your-username]/package-tracker-lab.git
```

Students will use:
```bash
git clone https://github.com/[your-username]/package-tracker-lab.git
```

### Method 2: ZIP Download
Students can download as ZIP from GitHub:
1. Go to your repository
2. Click green "Code" button
3. Click "Download ZIP"

---

## Files Included

```
package-tracker-lab/
├── app.py              # Flask backend (students will modify in Part 3)
├── requirements.txt    # Dependencies (Flask)
├── templates/
│   └── index.html     # Frontend
├── .gitignore         # Excludes .db files and Python cache
├── README.md          # Student-facing documentation
└── SOLUTION.md        # Teacher reference (what students will add)
```

**Note:** SOLUTION.md is included in the repo but students are unlikely to look at it unless they're stuck. You can remove it if you prefer.

---

## Pre-Class Checklist

- [ ] Test the app on your computer (make sure it runs)
- [ ] Test on school computers (check Python version, pip availability)
- [ ] Push to GitHub and test cloning
- [ ] Assign pre-reading document as homework (optional but recommended)
- [ ] Print/post the lab handout
- [ ] Verify students can access GitHub (not blocked by school firewall)

---

## During Class - Common Student Issues

### "git: command not found"
- Have ZIP download ready as backup
- Students can download manually from GitHub

### "pip: command not found"
- Try `pip3`
- Check Python installation with `python --version`

### Port 5000 already in use
- Have students change port in app.py to 5001, 5002, etc.
- Or find and kill the process using port 5000

### Browser can't reach localhost:5000
- Check Flask is running (should see messages in terminal)
- Try 127.0.0.1:5000 instead of localhost:5000
- Check firewall settings

---

## Troubleshooting Python Installation

If Python isn't installed on school computers:

**Windows:**
- Download from python.org
- Check "Add Python to PATH" during installation

**Mac:**
- Should have Python 3 pre-installed
- Check with: `python3 --version`

**Linux:**
- Usually pre-installed
- If not: `sudo apt install python3 python3-pip`

---

## Time Management

- **Part 1 (10 min):** Download and run - should be quick since students know bash
- **Part 2 (10 min):** Investigation - most time spent here
- **Part 3 (10 min):** Adding code - straightforward with clear instructions
- **Part 4 (5 min):** Challenges - for early finishers
- **Wrap-up (5 min):** Discussion

**Pro tip:** Have the solution ready on your computer so you can show students who get stuck.

---

## Post-Lab

Students should understand:
- How multiple languages work together (Python, JavaScript, HTML, SQL)
- What libraries/frameworks are (Flask)
- What databases do (SQLite)
- The client-server model

This sets up perfectly for Day 2 when you discuss Software Engineering practices!

---

## Questions?

This is Kevin's contact if you need to reach him: [You can add this]

Good luck with the lab! The students will love seeing a real web app come to life.
