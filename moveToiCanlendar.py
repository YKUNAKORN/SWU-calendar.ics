from datetime import datetime
from ics import Calendar, Event

# create .ics file function
def create_ics(events, filename="swu_calendar.ics"):
    calendar = Calendar()
    for event in events:
        e = Event()
        e.name = event['title']
        e.begin = datetime.strptime(event['date'], "%d/%m/%Y").strftime("%Y-%m-%d")
        e.duration = {"hours": 1}
        calendar.events.add(e)

    with open(filename, "w") as f:
        f.writelines(calendar)

# Example PDF
events = [
    {"title": "เปิดภาคการศึกษา", "date": "01/06/2567"},
    {"title": "สอบกลางภาค", "date": "15/07/2567"},
    {"title": "ปิดภาคการศึกษา", "date": "31/10/2567"},
]

# create .ics file
create_ics(events)
print("ไฟล์ .ics ถูกสร้างแล้ว!")