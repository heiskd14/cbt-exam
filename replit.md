# JAMB CBT Examination System

## Overview
This is a Computer-Based Test (CBT) examination system built with Python and Flask. It simulates the JAMB (Joint Admissions and Matriculation Board) examination interface, allowing students to take practice tests in English, Mathematics, and General Paper.

## Project Type
Web application using Python Flask

## Key Features
- Student registration with name and registration number
- Three subjects: English, Mathematics, General Paper
- 30 randomized questions per subject from question banks
- 60-minute exam timer
- Built-in calculator
- Navigation between questions with keyboard shortcuts
- Question number grid showing answered/unanswered status
- Automatic scoring and results display
- Answer correction/review screen
- Score persistence (saved to scores.json)

## Project Structure
```
.
├── app.py              # Flask web application
├── jamb_cbt.py         # Original Tkinter version (legacy)
├── templates/          # HTML templates
│   ├── base.html
│   ├── registration.html
│   ├── exam.html
│   ├── results.html
│   └── correction.html
├── static/             # Static assets
│   ├── css/style.css
│   └── js/exam.js
├── english.json        # English questions database
├── maths.json          # Mathematics questions database
├── general.json        # General Paper questions database
└── scores.json         # Stored exam scores (auto-generated)
```

## Technical Details
- **Language**: Python 3.11
- **Web Framework**: Flask 3.1.2
- **Frontend**: HTML, CSS, JavaScript
- **Question Format**: JSON with question, options array, and answer
- **Scoring**: Supports both numeric and string answer matching
- **Port**: 5000

## Running the Application
The application runs as a web server accessible in your browser:
```bash
python app.py
```
Then access it at the provided URL in the webview panel.

## Keyboard Shortcuts
- **A/B/C/D**: Select answer options
- **Left Arrow**: Previous question
- **Right Arrow**: Next question
- **S**: Submit exam

## Recent Changes
- 2025-11-21: Converted from Tkinter desktop app to Flask web application
  - Created Flask backend with routes for registration, exam, results, and correction
  - Built responsive web interface with HTML/CSS/JavaScript
  - Implemented real-time timer and calculator features
  - Configured to run on port 5000 with webview
  - Maintains all original features (keyboard shortcuts, question navigation, scoring)

## User Preferences
None specified yet.
