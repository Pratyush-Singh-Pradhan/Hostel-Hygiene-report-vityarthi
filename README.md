# Hostel-Hygiene-report-vityarthi
# Hostel Hygiene Report System (Python CLI Project)

This is a small Python program I made to help manage hygiene complaints inside a hostel. 
Normally, students tell a warden or write something down somewhere, and half the time the issue 
gets forgotten. So I thought it would be easier if there’s a simple way to log a complaint and 
store it properly.

The program runs in the terminal (no fancy interface) and lets a student file a hygiene complaint. 
All entries get saved in a JSON file so nothing gets lost. The admin option lets you read 
everything that has been submitted.

---

## What the program lets you do

- Students can submit a hygiene-related complaint  
- Complaints get saved automatically  
- Admin can see the entire list of complaints  
- Everything is stored in a small JSON file  
- Completely offline and easy to run  

---

## Running the program

Make sure you have Python 3 installed.  
Then just run:
After that, a menu will appear and the program is self-explanatory.

---

## Files included

`hostel_hygiene.py` — main program  
`complaints.json` — gets created automatically once a complaint is submitted  
`statement.md` — short explanation of the project  
`README.md` — this file  

---

## Possible improvements later

- Add password for admin  
- Switch from JSON to SQLite  
- Make a GUI version (Tkinter)  
- Export complaints to PDF or Excel  

This is intended to be simple and easy to understand, especially for beginners in Python programming.
