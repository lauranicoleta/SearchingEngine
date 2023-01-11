import csv  # This is for reading and writing in csv file
import requests  # This is for opening a web page
import re  # This is for regular expressions
from bs4 import BeautifulSoup  # This is a library that helps with extracting data from a html file

first_part = "https://www."
last_part = "/"

# Open URLs from a CSV file
with open('websites.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=" ")

    for row in csv_reader:
        page_url = first_part + row[0] + last_part
        print(" ")
        print("Opening URL:", page_url)
        l = requests.get(page_url)
        try:
            if (l.status_code == 200):
                 # page_html = str(l.content)
                print(l.status_code)
                soup = BeautifulSoup(l.content, "html.parser")
                content = soup.getText()
                # print(content)

                match_email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', content)
                if match_email != 0:
                    for email in match_email:
                        print("Email founded: ")
                        print(email)
                else:
                      print("No emails found on this page!")

                match_phone = re.findall(
                       r'((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))',
                        content)
                if match_phone != 0:
                     for phone in match_phone:
                         print("Phone number founded: ")
                         print(phone)
                else:
                        print("No phone numbers found!")
            else:
                print("Page couldn't be found!")
        except:
            print("Oops!  The site cannot be open!")
