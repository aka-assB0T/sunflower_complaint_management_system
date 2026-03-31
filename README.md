# Sunflower

Sunflower is a desktop based complaint management system built with Python, Tkinter, and SQLite.
It was originally developed as a university project and provides a simple interface for submitting complaints and viewing complaint records through an admin login.

## Features

1. Submit complaints through a GUI form
2. Store complaint data in SQLite
3. View submitted complaints in a table
4. Separate user submission page and admin view page
5. Image based landing screen

## Tech Stack

1. Python
2. Tkinter
3. SQLite
4. Pillow

## Project Structure

```text
sunflower_github_ready/
├── assets/
│   └── a.png
├── main.py
├── complaintListing.py
├── configdb.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

1. Clone the repository
2. Open the project folder in terminal
3. Install dependencies
4. Run the main file

```bash
pip install -r requirements.txt
python main.py
```

## Database Note

The app automatically creates the `complaintDB.db` database file when it runs.
Because of that, the database file does not need to be uploaded to GitHub.
This is also safer if the file contains test data or personal information.

## Default Admin Login

```text
Username: u1
Password: 123
```

For a public GitHub repository, it is better to mention that these credentials are only for demo use.

## Important Cleanup Before Publishing

1. Do not upload your local database file if it contains real entries
2. Use the relative image path version of the app so it works on other computers
3. Mention that this was a university learning project
4. Add screenshots in the repository later if you want the repo to look better

## Suggested GitHub Description

A basic complaint management system built with Python, Tkinter, and SQLite as a university project.

## Suggested Topics

```text
python tkinter sqlite desktop-app complaint-management university-project
```

## Future Improvements

1. Input validation
2. Secure admin authentication
3. Edit and delete complaint records
4. Search and filter complaints
5. Better UI styling and layout
6. Export complaints to CSV or PDF

## Disclaimer

This project is shared for learning and portfolio purposes.
