from datetime import datetime, timedelta

# Change AD to BE function
def convert_buddhist_to_gregorian(year_be):
    return year_be - 543

# Create .ics files function
def create_ics(events, filename='swu_calendar.ics'):
    with open(filename, 'w') as f:
        f.write("BEGIN:VCALENDAR\n")
        f.write("VERSION:2.0\n")
        f.write("PRODID:-//SWU Calendar//NONSGML v1.0//EN\n")

        for event in events:
            # get date event and change AD to BE
            event_date = datetime.strptime(event['date'], '%d-%m-%Y')
            year_in_gregorian = convert_buddhist_to_gregorian(event_date.year)
            start_date = event_date.replace(year=year_in_gregorian)

            # create time format for iCalendar
            start = start_date.strftime('%Y%m%dT%H%M%S')
            end = (start_date + timedelta(hours=1)).strftime('%Y%m%dT%H%M%S')

            f.write("BEGIN:VEVENT\n")
            f.write(f"UID:{start}@swu-calendar.com\n")
            f.write(f"SUMMARY:{event['title']}\n")
            f.write(f"DTSTART:{start}Z\n")
            f.write(f"DTEND:{end}Z\n")
            f.write(f"LOCATION:{event['location']}\n")
            f.write("END:VEVENT\n")

        f.write("END:VCALENDAR\n")

# Example from PDF
events = [
    {'title': 'เปิดภาคเรียน', 'date': '18-07-2567', 'location': 'มหาวิทยาลัยศรีนครินทรวิโรฒ'},
    {'title': 'วันสอบกลางภาค', 'date': '15-09-2567', 'location': 'มหาวิทยาลัยศรีนครินทรวิโรฒ'}
]

# สร้างไฟล์ .ics
create_ics(events)
print("ไฟล์ .ics ถูกสร้างแล้ว!")