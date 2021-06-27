
from ics import Calendar, Event

COURSE_PREFIXES = {'ECE', 'APS', 'ENV', 'SOC'}
EVENT_TYPES = {'LEC', 'PRA', 'TUT'}
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

MONDAY_START_DATE = '2021-09-06'

def get_day(weekday):
    assert weekday in DAYS
    delta = DAYS.index(weekday)
    
    day_str = str(int(MONDAY_START_DATE[-2:]) + delta)
    
    if len(day_str) == 1:
        day_str = "0" + day_str

    return MONDAY_START_DATE[:-2] + day_str


def parse_time(val): #Of the form 3:30PM to 15:30:00
    vals = val[:-2].split(':')
    hour = int(vals[0])
    if val[-2:] == 'pm' and (hour != 12):
        hour = hour + 12
    elif val[-2:] == 'am' and (hour == 12):
        hour = 0
    hr_str = str(hour)
    if len(hr_str) == 1:
        hr_str = "0" + hr_str

    return hr_str + ":" + vals[1] + ":00"    

def get_all_events():
    fin = open('paste.txt', 'r')

    events = []    

    course_code = None
    event_type = None
    course_name = None

    for line_val in fin:
        line = line_val[:-1] #Get rid of \n
        code = line[:3]
        if code in COURSE_PREFIXES:
            course_code = line[:8]
            course_name = line
            print(" Found course " + line)
        elif code in EVENT_TYPES:
            assert course_code is not None #You may have started with an incomplete course copy / paste
            event_type = line
            print("Found event type " + event_type)
        else:
           
            vals = line.lower().split(' ')
            if vals[0] in DAYS:#It is a new event
                assert course_code is not None #You may have started with an incomplete course copy / paste
                e = Event()
                day = vals[0]
                day_str = get_day(vals[0])
                e.begin = day_str + " " + parse_time(vals[1])
                e.end = day_str + " " + parse_time(vals[3])
                e.name = course_code + " " + event_type
                e.description = course_name
                events.append(e)
                print("Found " + course_code + " " + event_type + " at " + line)
    return events

def main():
    c = Calendar()
    
    c.events.update(get_all_events())
    
    calout = open('timetable.ics', 'w')
    calout.writelines(c)
    calout.close()



if __name__ == "__main__":
    main()