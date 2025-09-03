Robo Speaker - Voice Assistant
---
Overview:
-
Robo Speaker is a Python-based voice assistant that performs tasks like Google searches, IP address retrieval, note-taking, and system utilities. Uses Google Search and ipify.org per their public terms for personal projects. This project showcases my skills in Python programming, API integration, file handling, and system interactions, built to demonstrate my abilities for potential employers.

Features:
-
1. Web Integration: Launches Google searches and fetches public IP address via ipify.org API.
2. System Utilities: Opens Notepad, checks battery status, and manages notes/history.
3. Text-to-Speech: Converts text to speech using Windows SAPI with adjustable speed.
Note-Taking: Saves user notes to notes.txt and reads them aloud.
4. Command History: Logs commands to history.txt, with options to view or clear.

Skills Demonstrated:
-
1. Python: API calls (requests), system programming (os, psutil), file handling.
2. Libraries: win32com.client (text-to-speech), colorama (colored console), requests, psutil.
3. Features: User-friendly voice interface, error handling, modular design.

Prerequisites:
-
1. Operating System: Windows 10/11 (required for win32com.client text-to-speech).
2. Python: Version 3.6 or higher (tested with Python 3.10).
3. Dependencies:pip install pywin32 psutil requests colorama

Usage:
-
1. Launch the program to hear: "Hello! I am your Robo Speaker."
2. Enter commands in the console:
3. time: Displays and speaks the current time (e.g., "14:05 PM").
4. date: Displays and speaks today's date (e.g., "04/09/2025").
5. open notepad: Opens Windows Notepad.
6. search <query>: Opens Google search for the query (e.g., search python).
7. battery: Reports battery percentage.
8. ip: Fetches and speaks public IP address.
9. note <text>: Saves a note to notes.txt (e.g., note Buy milk).
10. show notes: Reads and speaks all saved notes.
11. show history: Displays command history from history.txt.
12. clear history: Clears command history.
13. who are you?: Introduces Robo Speaker.
14. help: Lists available commands.
15. q or quit: Exits the program.

Commands are logged to history.txt automatically.

File Structure:
-
1. robo_speaker.py: Main script with voice assistant logic.
2. requirements.txt: Lists required Python packages.
3. notes.txt: Stores user notes (created automatically, ignored by .gitignore).
4. history.txt: Logs command history (created automatically, ignored by .gitignore).
5. .gitignore: Excludes generated files like notes.txt, history.txt, __pycache__.

Technical Details:
-
i) Platform: Windows-only due to win32com.client for SAPI voice.
ii) Libraries Used:
1. win32com.client: Text-to-speech via Windows SAPI.
2. datetime: Time and date operations.
3. os: System commands (e.g., launching Notepad).
4. webbrowser: Opens Google search in browser.
5. psutil: Checks battery status.
6. requests: Fetches IP via ipify.org API.
7. colorama: Colored console output for better UX.

iii) Error Handling: Try-except for IP fetching; robust file operations.
iv) Extensibility: Modular code structure for easy command additions.

Why This Project?
-
This project highlights my ability to:

1. Build a user-friendly voice assistant with practical features.
2. Integrate external APIs (ipify) and system utilities (psutil, os).
3. Handle files for persistent note-taking and command history.
4. Create a polished, interactive CLI with voice and color output.

Future Enhancements:
-
1. Add cross-platform support using pyttsx3 for non-Windows systems.
2. Implement voice recognition for hands-free operation.
3. Add features like weather updates or calendar integration.
4. Develop a GUI using Tkinter or PyQt for a visual interface.

Contributing:
-
Feel free to fork the repo, submit issues, or create pull requests to suggest improvements.

Notes:
-
1. Tested on Windows 10/11 with Python 3.10.
2. No sensitive data is stored; IP fetch retrieves only public IP.
3. No license is included, allowing public viewing but retaining default copyright.
