# AcornICS
I noticed that Acorn it does not let you check if a timetable is valid based on the enrollment cart, it also does not let you visualize it easily. This means that before we actually able to add courses from our enrollment cart we need to manually check if they are valid and will have conflicts (unless there is some better way nobody told me about). 

This is a quick and easy python script that allows you to copy/paste the enrollment cart into a text file and then this script will parse it and generate a corosponding .ics file for one week of that timetable. You can then view this .ics file to see if the timetable is valid or has conflicts. 

# Usage
1. Instal https://icspy.readthedocs.io/en/stable/ which is a dependancy and make sure python is installed
2. Open acorn and highlight one semesters worth of courses 
3. Right click and select "Copy"
4. Open "paste.txt" and paste the contents you copied from acorn
5. Run the script with "python3 main.py" while in the main folder for this project
6. Take the resulting timetable.ics and paste it into an online .ics viewer such as https://larrybolt.github.io/online-ics-feed-viewer/ 
7. Check for conflicts, adjust, and repeat until your happy

# Notes
This is perhaps some of the worst python I have ever written, I was in a rush to make my timetable on the weekend. If anyone improves the script please feel free to make amendments and pull request or fork. 

Also as another note, I only added the engineering course prefixes since I was in a rush so if you want other course prefixes just go to line 4 and add them to the set. 

# Images
![Highlhting Text on Acorn](https://ibb.co/J3rrxCP)
![Example output](https://ibb.co/VWB3wB8)

