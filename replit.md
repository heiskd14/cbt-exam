# JAMB CBT Examination System

## Overview
This is a Computer-Based Test (CBT) examination system built with Python and Tkinter. It simulates the JAMB (Joint Admissions and Matriculation Board) examination interface, allowing students to take practice tests in English, Mathematics, and General Paper.

## Project Type
Desktop GUI application using Python Tkinter

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
├── jamb_cbt.py         # Main application file
├── test_tk.py          # Tkinter test file
├── english.json        # English questions database
├── maths.json          # Mathematics questions database
├── general.json        # General Paper questions database
├── scores.json         # Stored exam scores (auto-generated)
└── results.csv         # Results export (if generated)
```

## Technical Details
- **Language**: Python 3.11
- **GUI Framework**: Tkinter 8.6
- **Display**: Runs in VNC (desktop environment)
- **Question Format**: JSON with question, options array, and answer
- **Scoring**: Supports both numeric and string answer matching

## Running the Application
The application runs in a VNC desktop environment:
```bash
python jamb_cbt.py
```

## Keyboard Shortcuts
- **A/B/C/D**: Select answer options
- **Left Arrow**: Previous question
- **Right Arrow**: Next question
- **S**: Submit exam

## Recent Changes
- 2025-11-21: Imported from GitHub and configured for Replit environment
- Added Python 3.11 module
- Configured VNC workflow for GUI display

## User Preferences
None specified yet.
