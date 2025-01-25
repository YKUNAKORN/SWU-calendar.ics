import pdfplumber

# PDF URL data source
pdf_url = "http://edservices.op.swu.ac.th/Portals/27/File/ปฏิทินการศึกษา/ปฏิทินการศึกษา%202567%20แก้ไข.pdf?ver=KKmUvidvMgwPLHPh2epMpA%3d%3d"

# download a PDF file
import requests
response = requests.get(pdf_url)
with open("calendar_swu_2567.pdf", "wb") as f:
    f.write(response.content)

# get request data from PDF
events = []
with pdfplumber.open("calendar_swu_2567.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        # data format
        for line in text.split('\n'):
            if "วันที่" in line and "หัวข้อ" in line:
                date = line.split("วันที่:")[1].split(" ")[0].strip()
                title = line.split("หัวข้อ:")[1].strip()
                # change format
                date = date.replace("2567", "2024")  # แปลง พ.ศ. -> ค.ศ.
                events.append({'title': title, 'date': date})

print(events)